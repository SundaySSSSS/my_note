# map用法整理
* 插入元素:

```
map<string, string> map_data;
map_data.insert(map<string, string>::value_type ("msg_type", "UPLOAD"));
map_data.insert(map<string, string>::value_type ("data", "1234"));
```

* 遍历:

```
map<string, string>::iterator iter;
for(iter = map_data.begin(); iter != map_data.end(); iter++)
	cout<<iter->first<<" "<<iter->second<<endl;
```

* 根据Key查找某Value

```
map<string, string>::iterator iter;
iter = map_data.find("msg_type");
if(iter != map_data.end())
	cout<<"Find, the value is "<<iter->second<<endl;
```

* map的基本操作函数:

```
     C++ maps是一种关联式容器，包含“关键字/值”对
     begin()         返回指向map头部的迭代器
     clear(）        删除所有元素
     count()         返回指定元素出现的次数
     empty()         如果map为空则返回true
     end()           返回指向map末尾的迭代器
     equal_range()   返回特殊条目的迭代器对
     erase()         删除一个元素
     find()          查找一个元素
     get_allocator() 返回map的配置器
     insert()        插入元素
     key_comp()      返回比较元素key的函数
     lower_bound()   返回键值>=给定元素的第一个位置
     max_size()      返回可以容纳的最大元素个数
     rbegin()        返回一个指向map尾部的逆向迭代器
     rend()          返回一个指向map头部的逆向迭代器
     size()          返回map中元素的个数
     swap()           交换两个map
     upper_bound()    返回键值>给定元素的第一个位置

     value_comp()     返回比较元素value的函数
```
