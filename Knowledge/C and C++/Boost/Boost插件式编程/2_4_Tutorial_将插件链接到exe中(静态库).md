# 2_4_Tutorial_将插件链接到exe中(静态库)
将插件链接到可执行程序中有如下好处
1, 降低发布包的大小
2, 简化发布包的安装
3, 更快的加载插件

创建一个可链接的插件
```C++
//文件example/tutorial4/static_plugin.hpp
#include <boost/dll/alias.hpp>                          // for BOOST_DLL_ALIAS
#include <boost/shared_ptr.hpp>
#include "../tutorial_common/my_plugin_api.hpp"

namespace my_namespace {
    boost::shared_ptr<my_plugin_api> create_plugin();   // Forward declaration
} // namespace my_namespace

BOOST_DLL_ALIAS(
    my_namespace::create_plugin,                        // <-- this function is exported with...
    create_plugin                                       // <-- ...this alias name
)
```

主要技巧是关联定义BOOST_DLL_ALIAS中的内容, 当让插件进行静态链接时, 关联必须是exe源文件中的实例, 否则插件会被链接器优化掉
如下代码和普通工厂方法比较, 创建方法不再是类的静态成员函数, 而是改为一个单独的函数
```C++
//文件example/tutorial4/static_plugin.cpp
#include "static_plugin.hpp" // this is essential, BOOST_SYMBOL_ALIAS must be seen in this file

#include <boost/make_shared.hpp>
#include <iostream>

namespace my_namespace {

class my_plugin_static : public my_plugin_api {
public:
    my_plugin_static() {
        std::cout << "Constructing my_plugin_static" << std::endl;
    }

    std::string name() const {
        return "static";
    }

    float calculate(float x, float y) {
        return x - y;
    }

    ~my_plugin_static() {
        std::cout << "Destructing my_plugin_static" << std::endl;
    }
};

boost::shared_ptr<my_plugin_api> create_plugin() {
    //boost::make_shared和new类似, 具体差别官方解释为:"它可以只用内存分配完成对象分配和相关控制块分配，消除相当一部分创建shared_ptr的开销"
    return boost::make_shared<my_plugin_static>();
}

} // namespace my_namespace
```

将上面的代码编译成静态库, 再和如下代码链接在一起
``` C++
#include <boost/dll/shared_library.hpp>         // for shared_library
#include <boost/dll/runtime_symbol_info.hpp>    // for program_location()
#include "static_plugin.hpp"                    // without this headers some compilers may optimize out the `create_plugin` symbol
#include <boost/function.hpp>
#include <iostream>

namespace dll = boost::dll;

int main() 
{
    dll::shared_library self(dll::program_location());

    std::cout << "Call function" << std::endl;
    boost::function<boost::shared_ptr<my_plugin_api>()> creator
        = self.get_alias<boost::shared_ptr<my_plugin_api>()>("create_plugin");

    std::cout << "Computed Value: " << creator()->calculate(2, 2) << std::endl;
}
```

程序输出如下:
```
Call function
Constructing my_plugin_static
Computed Value: 0
Destructing my_plugin_static
```

备注:
在linux下链接时, 需要加`-rdynamic`选项

备注:
如果要想将上面的插件变为一个单独的动态库, 需要做的有:
去掉`#include "static_plugin.hpp"`, 
将`dll::program_location()`改为动态库的地址



