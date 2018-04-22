# 2_1_Tutorial_插件基础
定义接口:
``` C++
//文件example/tutorial_common/my_plugin_api.hpp
#include <string>

class my_plugin_api {
public:
   virtual std::string name() const = 0;
   virtual float calculate(float x, float y) = 0;

   virtual ~my_plugin_api() {}
};
```

定义一个用于工作的实体, 继承自刚才的 my_plugin_api类
``` C++
//文件example/tutorial1/my_plugin_sum.cpp
#include <boost/config.hpp> // for BOOST_SYMBOL_EXPORT
#include "../tutorial_common/my_plugin_api.hpp"

namespace my_namespace {

class my_plugin_sum : public my_plugin_api {
public:
    my_plugin_sum() {
        std::cout << "Constructing my_plugin_sum" << std::endl;
    }

    std::string name() const {
        return "sum";
    }

    float calculate(float x, float y) {
        return x + y;
    }

    ~my_plugin_sum() {
        std::cout << "Destructing my_plugin_sum ;o)" << std::endl;
    }
};

// Exporting `my_namespace::plugin` variable with alias name `plugin`
// (Has the same effect as `BOOST_DLL_ALIAS(my_namespace::plugin, plugin)`)
extern "C" BOOST_SYMBOL_EXPORT my_plugin_sum plugin;
my_plugin_sum plugin;

} // namespace my_namespace
```

调用动态库
``` C++
#include <boost/dll/import.hpp> // for import_alias
#include <iostream>
#include "../tutorial_common/my_plugin_api.hpp"

namespace dll = boost::dll;

int main(int argc, char* argv[]) {

    boost::filesystem::path lib_path(argv[1]);          // argv[1] contains path to directory with our plugin library
    boost::shared_ptr<my_plugin_api> plugin;            // variable to hold a pointer to plugin variable
    std::cout << "Loading the plugin" << std::endl;

    plugin = dll::import<my_plugin_api>(          // type of imported symbol is located between `<` and `>`
        lib_path / "my_plugin_sum",                     // path to the library and library name
        "plugin",                                       // name of the symbol to import
        dll::load_mode::append_decorations              // makes `libmy_plugin_sum.so` or `my_plugin_sum.dll` from `my_plugin_sum`
    );

    std::cout << "plugin->calculate(1.5, 1.5) call:  " << plugin->calculate(1.5, 1.5) << std::endl;
}
```

输出结果为:
```
Loading the plugin
Constructing my_plugin_sum
plugin->calculate(1.5, 1.5) call:  3
Destructing my_plugin_sum ;o)
```


