# 2_9_Tutorial_在WIndows DLL中引入C函数

当通过名称引用C函数时, 必须使用`boost::dll::import`, 不能使用`boost::dll::import_alias`

一个平凡的例子
```C++
#include <boost/dll/import.hpp>         // for dll::import
#include <boost/dll/shared_library.hpp> // for dll::shared_library
#include <boost/function.hpp>
#include <iostream>
#include <windows.h>

namespace dll = boost::dll;

int main() {
    typedef HANDLE(__stdcall GetStdHandle_t)(DWORD );       // function signature with calling convention

    // OPTION #0, requires C++11 compatible compiler that understands GetStdHandle_t signature.

    auto get_std_handle = dll::import<GetStdHandle_t>(
        "Kernel32.dll",
        "GetStdHandle",
        boost::dll::load_mode::search_system_folders
    );
    std::cout << "0.0 GetStdHandle() returned " << get_std_handle(STD_OUTPUT_HANDLE) << std::endl;

    // You may put the `get_std_handle` into boost::function<>. But boost::function<Signature> can not compile with
    // Signature template parameter that contains calling conventions, so you'll have to remove the calling convention.
    boost::function<HANDLE(DWORD)> get_std_handle2 = get_std_handle;
    std::cout << "0.1 GetStdHandle() returned " << get_std_handle2(STD_OUTPUT_HANDLE) << std::endl;


    // OPTION #1, does not require C++11. But without C++11 dll::import<> can not handle calling conventions,
    // so you'll need to hand write the import.
    dll::shared_library lib("Kernel32.dll", dll::load_mode::search_system_folders);
    GetStdHandle_t& func = lib.get<GetStdHandle_t>("GetStdHandle");

    // Here `func` does not keep a reference to `lib`, you'll have to deal with that on your own.
    std::cout << "1.0 GetStdHandle() returned " << func(STD_OUTPUT_HANDLE) << std::endl;

    return 0;
}
```