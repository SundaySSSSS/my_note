# for的新语法糖
``` C++
void testNewFor()
{
    std::vector<int> vec;
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(3);
    vec.push_back(4);
    vec.push_back(5);
    for (auto i : vec) //不能修改vector中的值
    {
        std::cout << i << std::endl;
    }

    for (auto& i : vec) //使用引用访问, 可以修改vector中的值
    {
        i = 6;
    }
    for (auto i : vec)
    {
        std::cout << i << std::endl;
    }
}
```
