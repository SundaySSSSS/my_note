# 2_5_Tutorial_linux系统中符号遮蔽问题
暂时用不到, 先贴上英文原文

Let's make an executable, link a plugin into it and attempt to load all the existing plugins:
```C++
namespace dll = boost::dll;

class plugins_collector {
    // Name => plugin
    typedef boost::container::map<std::string, dll::shared_library> plugins_t;

    boost::filesystem::path         plugins_directory_;
    plugins_t                       plugins_;

    // loads all plugins in plugins_directory_
    void load_all();

    // Gets `my_plugin_api` instance using "create_plugin" or "plugin" imports,
    // stores plugin with its name in the `plugins_` map.
    void insert_plugin(BOOST_RV_REF(dll::shared_library) lib);

public:
    plugins_collector(const boost::filesystem::path& plugins_directory)
        : plugins_directory_(plugins_directory)
    {
        load_all();
    }

    void print_plugins() const;

    std::size_t count() const;
    // ...   
};
```

```C++
int main(int argc, char* argv[]) {

    plugins_collector plugins(argv[1]);

    std::cout << "\n\nUnique plugins " << plugins.count() << ":\n";
    plugins.print_plugins();
    // ...
```

With the default flags you'll get a very strange output:
```
Loaded (0x180db60):"/libs/dll/test/libmy_plugin_aggregator.so"
Constructing my_plugin_static
Destructing my_plugin_static
...

Unique plugins 2:
(0x180db60): static
(0x180e3b0): sum
Destructing my_plugin_sum ;o)
```

Why my_plugin_static was constructed while we were loading my_plugin_aggregator?

That's because function create_plugin from libmy_plugin_aggregator.so was shadowed by the create_plugin function from other plugin. Dynamic linker thought that create_plugin was already loaded and there is no need to load it again.

Warning
Use "-fvisibility=hidden" flag (at least for plugins) while compiling for POSIX platforms. This flag makes your code more portable ("-fvisibility=hidden" is the default behavior under Windows), reduces size of the binaries and improves binary load time.

Now if we recompile your example with "-fvisibility=hidden" we'll get the following output:
```
Loaded (0x2406b60):"/libs/dll/test/libmy_plugin_aggregator.so"
Loaded (0x2407410):"/libs/dll/test/libgetting_started_library.so"
Constructing my_plugin_sum
...

Unique plugins 3:
(0x2406b60): aggregator
(0x7fd1cadce2c8): static
(0x24073b0): sum
Destructing my_plugin_sum ;o)
```

Full sources:
example/tutorial5/load_all.cpp
example/tutorial4/static_plugin.cpp
example/tutorial2/my_plugin_aggregator.cpp
example/tutorial1/my_plugin_sum.cpp