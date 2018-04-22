# 2_6_Tutorial_在动态库卸载时调用回调
boost.dll本身不提供抓取动态库卸载时机的机制, 但这种机制是很容易实现的
需要做的就是:
写一个简单的类, 将需要在动态库卸载时需要调用的回调注册进去, 如下例
``` C++
#include <boost/dll/alias.hpp> // for BOOST_DLL_ALIAS
#include <boost/function.hpp>
#include <vector>

namespace my_namespace {

struct on_unload {
    typedef boost::function<void()> callback_t;
    typedef on_unload this_type;

    ~on_unload() {
        for (std::size_t i = 0; i < callbacks_.size(); ++i) {
            callback_t& function = callbacks_[i];
            function(); // calling the callback
        }
    }

    // not thread safe
    static void add(const callback_t& function) {
        static this_type instance;
        instance.callbacks_.push_back(function);
    }

private:
    std::vector<callback_t> callbacks_;
    on_unload() {} // prohibit construction outside of the `add` function
};

// Exporting the static "add" function with name "on_unload"
BOOST_DLL_ALIAS(my_namespace::on_unload::add, on_unload)

} // namespace my_namespace
```

在上面例子中, on_unload是一个单例类, 里面有一个存放回调的数组, 在析构时调用
下面加载动态库, 再提供一个回调

```C++
#include <boost/dll/import.hpp>
#include <boost/function.hpp>
#include <iostream>

typedef boost::function<void()> callback_t;

void print_unloaded() {
    std::cout << "unloaded" << std::endl;
}

int main(int argc, char* argv[]) {
    // argv[1] contains full path to our plugin library
    boost::filesystem::path shared_library_path =  argv[1];

    // loading library and getting a function from it
    boost::function<void(const callback_t&)> on_unload
        = boost::dll::import_alias<void(const callback_t&)>(
            shared_library_path, "on_unload"
        );

    on_unload(&print_unloaded); // adding a callback
    std::cout << "Before library unload." << std::endl;

    // Releasing last reference to the library, so that it gets unloaded
    on_unload.clear();
    std::cout << "After library unload." << std::endl;
}
```
