# 2_2_Tutorial_工厂方法
上面2_1中的例子中, 导入的plugin只有单一的实体, 当需要多个plugin实体时, 会发生问题, 可以使用如下的工厂方法:

```C++
#include <boost/dll/alias.hpp> // for BOOST_DLL_ALIAS   
#include "../tutorial_common/my_plugin_api.hpp"

namespace my_namespace {

class my_plugin_aggregator : public my_plugin_api {
private:
    float aggr_;
    my_plugin_aggregator() : aggr_(0) {}    //私有构造, 不允许外接直接构造此类对象

public:
    std::string name() const {
        return "aggregator";
    }

    float calculate(float x, float y) {
        aggr_ += x + y;
        return aggr_;
    }

    // Factory method 工厂方法
    static boost::shared_ptr<my_plugin_aggregator> create() {
        return boost::shared_ptr<my_plugin_aggregator>(
            new my_plugin_aggregator()
        );
    }
};

//关联工厂方法
BOOST_DLL_ALIAS(
    my_namespace::my_plugin_aggregator::create, // <-- this function is exported with...
    create_plugin                               // <-- ...this alias name
)

} // namespace my_namespace
```

调用此工厂方法创建对象
```C++
#include <boost/dll/import.hpp> // for import_alias
#include <boost/function.hpp>
#include <iostream>
#include "../tutorial_common/my_plugin_api.hpp"

namespace dll = boost::dll;

int main(int argc, char* argv[]) {

    boost::filesystem::path shared_library_path(argv[1]);               // argv[1] contains path to directory with our plugin library
    shared_library_path /= "my_plugin_aggregator";
    typedef boost::shared_ptr<my_plugin_api> (pluginapi_create_t)();    //定义一个类型, 用于存放插件中的create_plugin
    boost::function<pluginapi_create_t> creator;

    creator = boost::dll::import_alias<pluginapi_create_t>(             // type of imported symbol must be explicitly specified
        shared_library_path,                                            // path to library
        "create_plugin",                                                // symbol to import
        dll::load_mode::append_decorations                              // do append extensions and prefixes
    );

    boost::shared_ptr<my_plugin_api> plugin = creator();
    std::cout << "plugin->calculate(1.5, 1.5) call:  " << plugin->calculate(1.5, 1.5) << std::endl;
    std::cout << "plugin->calculate(1.5, 1.5) second call:  " << plugin->calculate(1.5, 1.5) << std::endl;
    std::cout << "Plugin Name:  " << plugin->name() << std::endl;
}
```

输出为:
```
plugin->calculate(1.5, 1.5) call:  3
plugin->calculate(1.5, 1.5) second call:  6
Plugin Name:  aggregator
```