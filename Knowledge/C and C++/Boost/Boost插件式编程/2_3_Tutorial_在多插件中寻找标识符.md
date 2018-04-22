# 2_3_Tutorial_在多插件中寻找标识符
当我们有多个插件时(多个动态库), 不知道某个符号(例如: create_plugin)在哪个动态库中时, 
可以按照如下方法构造一个搜索标识符的函数
``` C++
#include <boost/dll/import.hpp> // for import_alias
#include <boost/make_shared.hpp>
#include <boost/function.hpp>
#include <iostream>
#include "../tutorial_common/my_plugin_api.hpp"

namespace dll = boost::dll;

//输入的plugins是所有插件名称的数组
std::size_t search_for_symbols(const std::vector<boost::filesystem::path>& plugins) {
    std::size_t plugins_found = 0;

    for (std::size_t i = 0; i < plugins.size(); ++i) {
        std::cout << "Loading plugin: " << plugins[i] << '\n';
        dll::shared_library lib(plugins[i], dll::load_mode::append_decorations);
        if (!lib.has("create_plugin")) {
            // no such symbol
            continue;
        }

        // library has symbol, importing...
        typedef boost::shared_ptr<my_plugin_api> (pluginapi_create_t)();
        boost::function<pluginapi_create_t> creator
            = dll::import_alias<pluginapi_create_t>(boost::move(lib), "create_plugin");

        std::cout << "Matching plugin name: " << creator()->name() << std::endl;
        ++ plugins_found;
    }

    return plugins_found;
}

```

输出为:
```
Loading plugin: "/test/libmy_plugin_aggregator.so"
Matching plugin name: aggregator
Loading plugin: "/test/libmy_plugin_sum.so"
Constructing my_plugin_sum
Destructing my_plugin_sum ;o)
```


