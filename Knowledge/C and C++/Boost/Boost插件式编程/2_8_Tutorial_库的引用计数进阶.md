# 2_8_Tutorial_库的引用计数进阶

使用`boost::dll:import`引入的函数或变量, 持有一个动态库的引用, 
而import出来的对象是没有这个指向动态库的引用的, 
这个问题在Boost.DLL层无法解决, 但可以自己解决这个问题, 如下例:

## 定义/实现接口
定义一个新的API接口
```C++
//文件example/tutorial8/refcounting_api.hpp
#include "../tutorial_common/my_plugin_api.hpp"
#include <boost/filesystem/path.hpp>

class my_refcounting_api: public my_plugin_api {
public:
    // Returns path to shared object that holds a plugin.
    // Must be instantiated in plugin.
    virtual boost::filesystem::path location() const = 0;
};
```

这个接口只是增加了一个返回库位置的抽象方法
实现此接口:
```C++
//文件refcounting_plugin.hpp
#include "refcounting_api.hpp"
#include <boost/dll/alias.hpp> // for BOOST_DLL_ALIAS

my_refcounting_api* create(); // defined in plugin
BOOST_DLL_ALIAS(create, create_refc_plugin)
//]
```

```C++
// 文件example/tutorial8/refcounting_plugin.cpp
#include "refcounting_plugin.hpp"
#include <boost/dll/runtime_symbol_info.hpp> // for this_line_location()

namespace my_namespace {

class my_plugin_refcounting : public my_refcounting_api {
public:
    // Must be instantiated in plugin
    boost::filesystem::path location() const {
        return boost::dll::this_line_location(); // location of this plugin
    }
    std::string name() const {
        return "refcounting";
    }
    // ...
};

} // namespace my_namespace

// Factory method. Returns *simple pointer*!
my_refcounting_api* create() {
    return new my_namespace::my_plugin_refcounting();
}
```

上面的代码中, 和工厂方法的插件有两处不同,
1, 增加了一个location方法, 调用`boost::dll::this_line_location()'返回当前库地址
2, 工厂方法create返回的是一个普通指针, 而不是智能指针share_ptr

下面写一个函数, 让它能够将新创建的my_refcounting_api实体 绑定到 动态库中
``` C++
//文件refcounting_plugin.hpp
#include <boost/shared_ptr.hpp>
#include <boost/make_shared.hpp>
#include <boost/dll/shared_library.hpp>

struct library_holding_deleter {
    boost::shared_ptr<boost::dll::shared_library> lib_;

    void operator()(my_refcounting_api* p) const {
        delete p;
    }
};

inline boost::shared_ptr<my_refcounting_api> bind(my_refcounting_api* plugin) {
    // getting location of the shared library that holds the plugin
    boost::filesystem::path location = plugin->location();

    // `make_shared` is an efficient way to create a shared pointer
    boost::shared_ptr<boost::dll::shared_library> lib
        = boost::make_shared<boost::dll::shared_library>(location);

    library_holding_deleter deleter;
    deleter.lib_ = lib;

    //这句是给share_ptr指定了析构时的删除器deleter, 而不是简单的delete
    return boost::shared_ptr<my_refcounting_api>(
        plugin, deleter
    );
}
```

实例化插件接口
```C++
//放在文件refcounting_api.hpp中
#include <boost/dll/import.hpp>
#include <boost/function.hpp>
inline boost::shared_ptr<my_refcounting_api> get_plugin(
    boost::filesystem::path path, const char* func_name)
{
    typedef my_refcounting_api*(func_t)();
    boost::function<func_t> creator = boost::dll::import_alias<func_t>(
        path,
        func_name,
        boost::dll::load_mode::append_decorations   // will be ignored for executable
    );

    // `plugin` does not hold a reference to shared library. If `creator` will go out of scope, 
    // then `plugin` can not be used.
    my_refcounting_api* plugin = creator();

    // Returned variable holds a reference to 
    // shared_library and it is safe to use it.
    return bind( plugin );

    // `creator` goes out of scope here and will be destroyed.
}
```

## 加载插件
### 动态加载插件
```C++
//放在文件refcounting_api.hpp中
#include <iostream>
#include "refcounting_api.hpp"

int main(int argc, char* argv[]) {

    boost::shared_ptr<my_refcounting_api> plugin = get_plugin(
        boost::filesystem::path(argv[1]) / "refcounting_plugin",
        "create_refc_plugin"
    );

    std::cout << "Plugin name: " << plugin->name()
              << ", \nlocation: " << plugin->location()
              << std::endl;
}
```

输出:
```
Plugin name: refcounting,
location: "/libs/dll/librefcounting_plugin.so"
```

### 静态加载插件
``` C++
#include <boost/dll/runtime_symbol_info.hpp> // program_location()
#include <iostream>
#include "refcounting_plugin.hpp"

int main() {
    boost::shared_ptr<my_refcounting_api> plugin = get_plugin(
        boost::dll::program_location(),
        "create_refc_plugin"
    );

    std::cout << "Plugin name: " << plugin->name()
              << ", \nlocation: " << plugin->location()
              << std::endl;
}
```

输出为:
``` 
Plugin name: refcounting,
location: "/tutorial8_static"

```
