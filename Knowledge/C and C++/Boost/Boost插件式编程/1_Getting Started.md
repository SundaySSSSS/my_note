# boost插件式编程 - Getting Started
boost文档Chapter13笔记

## 基础
### 添加基础内容
```C++
using namespace boost;

// `extern "C"` - specifies C linkage: forces the compiler to export function/variable by a pretty (unmangled) C name.
#define API extern "C" BOOST_SYMBOL_EXPORT
```

`BOOST_SYMBOL_EXPORT`宏本质就是`__declspec(dllexport)`(或其他形式)

### 导入库中内容的基本方法
#### 导入函数
动态库中:
```C++
namespace some_namespace {
    API int i_am_a_cpp11_function(std::string&& param) noexcept;
//          ^--------------------  function name to use in dll::import<>
}
```
外部导入时:
```C++
// Importing function.
auto cpp11_func = dll::import<int(std::string&&)>(
        path_to_shared_library, "i_am_a_cpp11_function"
    );
```
#### 导入变量
动态库中
``` C++
namespace your_project_namespace {
    API std::string cpp_variable_name;
}
```
外部导入时:
``` C++
// Importing  variable.
shared_ptr<std::string> cpp_var = dll::import<std::string>(
        path_to_shared_library, "cpp_variable_name"
    );
```
#### 通过关联名称导入函数
动态库中:
``` C++
namespace some_namespace {
    std::string i_am_function_with_ugly_name(const std::string& param) noexcept;
}

// When you have no control over function sources or wish to specify another name.
//将i_am_function_with_ugly_name关联到pretty_name上, 外部导入pretty_name即可
BOOST_DLL_ALIAS(some_namespace::i_am_function_with_ugly_name, pretty_name)

```
导入时:
``` C++
// Importing function by alias name
auto cpp_func = dll::import_alias<std::string(const std::string&)>(
        path_to_shared_library, "pretty_name"
    );
```
#### 导入整个库的方法

``` C++
//将整个库导入称为lib对象
boost::dll::shared_library lib("/test/boost/application/libtest_library.so");
//取用里面的元素
int plugin_constant = lib.get<const int>("integer_variable");
boost::function<int()> f = lib.get<int()>("function_returning_int");
int& i = lib.get_alias<int>("alias_to_int_variable");
```