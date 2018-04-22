# 2_7_Tutorial_在库中查找某类型的符号
当在使用库的时候, 有时会不知道要使用的具体函数名, 这种情况, 可以用如下方法解决

情形: 有个项目名为Anna, 它使用的库中有一个函数特征为: void(const std::string &) 但不知道具体的函数名

解决方案: 
和库的开发者沟通, 他们可以把这些函数任意命名, 但必须都放在一个名为Anna的域中
(规定此域中的函数都是void(const std::string &)形式)
库的开发者可以使用`BOOST_DLL_ALIAS_SECTIONED`来将函数放到Anna域中
```C++
#include <boost/dll/alias.hpp> // for BOOST_DLL_ALIAS_SECTIONED
#include <iostream>
#include <string>

void print(const std::string& s) {
    std::cout << "Hello, " << s << '!' << std::endl;
}

BOOST_DLL_ALIAS_SECTIONED(print, print_hello, Anna)
```

``` C++
#include <boost/dll/alias.hpp> // for BOOST_DLL_ALIAS_SECTIONED
#include <string>
#include <iostream>

void print_howdy(const std::string& s) {
    std::cout << "How're you doing, " << s << '?' << std::endl;
}

void print_bored(const std::string& s) {
    std::cout << "Are you bored, " << s << '?' << std::endl;
}

BOOST_DLL_ALIAS_SECTIONED(print_howdy, howdy, Anna)
BOOST_DLL_ALIAS_SECTIONED(print_bored, are_you_bored, Anna)
```

使用`boost::dll::library_info`来加载这些函数
```C++
#include <boost/dll/shared_library.hpp>
#include <boost/dll/library_info.hpp>
#include <iostream>

void load_and_execute(const boost::filesystem::path libraries[], std::size_t libs_count)
{
    const std::string username = "User";

    for (std::size_t i = 0; i < libs_count; ++i) {
        // Class `library_info` can extract information from a library
        boost::dll::library_info inf(libraries[i]);

        // Getting symbols exported from 'Anna' section
        std::vector<std::string> exports = inf.symbols("Anna");

        // Loading library and importing symbols from it
        boost::dll::shared_library lib(libraries[i]);
        for (std::size_t j = 0; j < exports.size(); ++j) {
            std::cout << "\nFunction '" << exports[j] << "' prints:\n\t";
            lib.get_alias<void(const std::string&)>(exports[j]) // importing function
                (username);                                     // calling function
        }
    }
}
```

输出结果为:
```
Function 'print_hello' prints:
	Hello, User!

Function 'are_you_bored' prints:
	Are you bored, User?

Function 'howdy' prints:
	How're you doing, User?
```