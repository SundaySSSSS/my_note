# C++中的STL中map用法详解

Map是STL的一个关联容器，它提供一对一（其中第一个可以称为关键字，每个关键字只能在map中出现一次，第二个可能称为该关键字的值）的数据 处理能力，由于这个特性，它完成有可能在我们处理一对一数据的时候，在编程上提供快速通道。这里说下map内部数据的组织，map内部自建一颗红黑树(一 种非严格意义上的平衡二叉树)，这颗树具有对数据自动排序的功能，所以在map内部所有的数据都是有序的，后边我们会见识到有序的好处。  

## 1、map简介
map是一类关联式容器。它的特点是增加和删除节点对迭代器的影响很小，除了那个操作节点，对其他的节点都没有什么影响。  
对于迭代器来说，可以修改实值，而不能修改key。  

## 2、map的功能
自动建立Key － value的对应。key 和 value可以是任意你需要的类型。
根据key值快速查找记录，查找的复杂度基本是Log(N)，如果有1000个记录，最多查找10次，1,000,000个记录，最多查找20次。
快速插入Key -Value 记录。
快速删除记录
根据Key 修改value记录。
遍历所有记录。
 
## 3、使用map
使用map得包含map类所在的头文件  
`#include <map>  //注意，STL头文件没有扩展名.h`
map对象是模板类，需要关键字和存储对象两个模板参数：  
`std:map<int,string> personnel;`
这样就定义了一个用int作为索引,并拥有相关联的指向string的指针.  

## 4、map的构造函数
 
map共提供了6个构造函数，这块涉及到内存分配器这些东西，略过不表，在下面我们将接触到一些map的构造方法，这里要说下的就是，我们通常用如下方法构造一个map：  
`map<int, string> mapStudent;`

## 5、数据的插入
 
在构造map容器后，我们就可以往里面插入数据了。这里讲三种插入数据的方法：  

* 第一种：用insert函数插入pair数据  

```
//数据的插入--第一种：用insert函数插入pair数据  
#include <map>
#include <string>
#include <iostream>
using namespace std;

int main()
{
    map<int, string> mapStudent;
    mapStudent.insert(pair<int, string>(1, "student_one"));
    mapStudent.insert(pair<int, string>(2, "student_two"));
    mapStudent.insert(pair<int, string>(3, "student_three"));
    map<int, string>::iterator iter;
    for(iter = mapStudent.begin(); iter != mapStudent.end(); iter++)
       cout<<iter->first<<" "<<iter->second<<endl;
}

```

* 第二种：用insert函数插入value_type数据，下面举例说明

```
//第二种：用insert函数插入value_type数据，下面举例说明  
#include <map>
#include <string>
#include <iostream>
using namespace std;
int main()
{
    map<int, string> mapStudent;
    mapStudent.insert(map<int, string>::value_type (1, "student_one"));
    mapStudent.insert(map<int, string>::value_type (2, "student_two"));
    mapStudent.insert(map<int, string>::value_type (3, "student_three"));
    map<int, string>::iterator iter;
    for(iter = mapStudent.begin(); iter != mapStudent.end(); iter++)
       cout<<iter->first<<" "<<iter->second<<endl;
}

```

* 第三种：用数组方式插入数据，下面举例说明

```
//第三种：用数组方式插入数据，下面举例说明
#include <map>
#include <string>
#include <iostream>
using namespace std;
int main()
{
    map<int, string> mapStudent;
    mapStudent[1] = "student_one";
    mapStudent[2] = "student_two";
    mapStudent[3] = "student_three";
    map<int, string>::iterator iter;
    for(iter = mapStudent.begin(); iter != mapStudent.end(); iter++)
        cout<<iter->first<<' '<<iter->second<<endl;
}

```

以上三种用法，虽然都可以实现数据的插入，但是它们是有区别的，当然了第一种和第二种在效果上是完成一样的，用insert函数插入数据，在数据的 插入上涉及到集合的唯一性这个概念，即当map中有这个关键字时，insert操作是插入数据不了的，但是用数组方式就不同了，它可以覆盖以前该关键字对 应的值，用程序说明

```
mapStudent.insert(map<int, string>::value_type (1, "student_one"));
mapStudent.insert(map<int, string>::value_type (1, "student_two"));
```

上面这两条语句执行后，map中1这个关键字对应的值是“student_one”，第二条语句并没有生效，那么这就涉及到我们怎么知道insert语句是否插入成功的问题了，可以用pair来获得是否插入成功，程序如下

```
pair<map<int, string>::iterator, bool> Insert_Pair;
Insert_Pair = mapStudent.insert(map<int, string>::value_type (1, "student_one"));
```

我们通过pair的第二个变量来知道是否插入成功，它的第一个变量返回的是一个map的迭代器，如果插入成功的话Insert_Pair.second应该是true的，否则为false。
  
下面给出完成代码，演示插入成功与否问题
 
```
[cpp] view plain copy
 
//验证插入函数的作用效果
#include <map>
#include <string>
#include <iostream>
using namespace std;

int main()
{
    map<int, string> mapStudent;
    pair<map<int, string>::iterator, bool> Insert_Pair;

    Insert_Pair = mapStudent.insert(pair<int, string>(1, "student_one"));

    if(Insert_Pair.second == true)
        cout<<"Insert Successfully"<<endl;
    else
        cout<<"Insert Failure"<<endl;

    Insert_Pair = mapStudent.insert(pair<int, string>(1, "student_two"));

    if(Insert_Pair.second == true)
        cout<<"Insert Successfully"<<endl;
    else
        cout<<"Insert Failure"<<endl;
    map<int, string>::iterator iter;
    for(iter = mapStudent.begin(); iter != mapStudent.end(); iter++)
        cout<<iter->first<<' '<<iter->second<<endl;
}

```

大家可以用如下程序，看下用数组插入在数据覆盖上的效果

```
//验证数组形式插入数据的效果
#include <map>
#include <string>
#include <iostream>
using namespace std;

int main()
{
    map<int, string> mapStudent;
    mapStudent[1] = "student_one";
    mapStudent[1] = "student_two";
    mapStudent[2] = "student_three";
    map<int, string>::iterator iter;
    for(iter = mapStudent.begin(); iter != mapStudent.end(); iter++)
        cout<<iter->first<<' '<<iter->second<<endl;
}

```

## 6、map的大小

在往map里面插入了数据，我们怎么知道当前已经插入了多少数据呢，可以用size函数，用法如下：  

```
Int nSize = mapStudent.size();
```

## 7、数据的遍历
这里也提供三种方法，对map进行遍历

* 第一种：应用前向迭代器，上面举例程序中到处都是了，略过不表
* 第二种：应用反相迭代器，下面举例说明

```
//第二种，利用反向迭代器
#include <map>
#include <string>
#include <iostream>

using namespace std;

int main()
{
map<int, string> mapStudent;
mapStudent.insert(pair<int, string>(1, "student_one"));
mapStudent.insert(pair<int, string>(2, "student_two"));
mapStudent.insert(pair<int, string>(3, "student_three"));
map<int, string>::reverse_iterator iter;
for(iter = mapStudent.rbegin(); iter != mapStudent.rend(); iter++)
    cout<<iter->first<<"  "<<iter->second<<endl;
}

```

* 第三种，用数组的形式，程序说明如下：

```
//第三种：用数组方式，程序说明如下
#include <map>
#include <string>
#include <iostream>
using namespace std;

int main()
{
    map<int, string> mapStudent;
    mapStudent.insert(pair<int, string>(1, "student_one"));
    mapStudent.insert(pair<int, string>(2, "student_two"));
    mapStudent.insert(pair<int, string>(3, "student_three"));
    int nSize = mapStudent.size();
    //此处应注意，应该是 for(int nindex = 1; nindex <= nSize; nindex++)  
    //而不是 for(int nindex = 0; nindex < nSize; nindex++)  
    for(int nindex = 1; nindex <= nSize; nindex++)  
        cout<<mapStudent[nindex]<<endl;
}

```
 
## 8、查找并获取map中的元素（包括判定这个关键字是否在map中出现）
 
在这里我们将体会，map在数据插入时保证有序的好处。  
要判定一个数据（关键字）是否在map中出现的方法比较多，这里标题虽然是数据的查找，在这里将穿插着大量的map基本用法。  
这里给出三种数据查找方法  

* 第一种：用count函数来判定关键字是否出现，其缺点是无法定位数据出现位置,由于map的特性，一对一的映射关系，就决定了count函数的返回值只有两个，要么是0，要么是1，出现的情况，当然是返回1了  

* 第二种：用find函数来定位数据出现位置，它返回的一个迭代器，当数据出现时，它返回数据所在位置的迭代器，如果map中没有要查找的数据，它返回的迭代器等于end函数返回的迭代器。  
查找map中是否包含某个关键字条目用find()方法，传入的参数是要查找的key，在这里需要提到的是begin()和end()两个成员，  
分别代表map对象中第一个条目和最后一个条目，这两个数据的类型是iterator.  
程序说明  


```
#include <map>
#include <string>
#include <iostream>

using namespace std;

int main()
{
    map<int, string> mapStudent;
    mapStudent.insert(pair<int, string>(1, "student_one"));
    mapStudent.insert(pair<int, string>(2, "student_two"));
    mapStudent.insert(pair<int, string>(3, "student_three"));
    map<int, string>::iterator iter;
    iter = mapStudent.find(1);
    if(iter != mapStudent.end())
       cout<<"Find, the value is "<<iter->second<<endl;
    else
       cout<<"Do not Find"<<endl;
    return 0;
}
```

通过map对象的方法获取的iterator数据类型是一个std::pair对象，包括两个数据 iterator->first和 iterator->second分别代表关键字和存储的数据。  

* 第三种：这个方法用来判定数据是否出现，是显得笨了点，但是，我打算在这里讲解

lower_bound函数用法，这个函数用来返回要查找关键字的下界(是一个迭代器)  
upper_bound函数用法，这个函数用来返回要查找关键字的上界(是一个迭代器)  
例如：map中已经插入了1，2，3，4的话，如果lower_bound(2)的话，返回的2，而upper-bound（2）的话，返回的就是3  
Equal_range函数返回一个pair，pair里面第一个变量是Lower_bound返回的迭代器，pair里面第二个迭代器是Upper_bound返回的迭代器，如果这两个迭代器相等的话，则说明map中不出现这个关键字，  
程序说明  
 
```
#include <map>
#include <string>
#include <iostream>
using namespace std;

int main()
{
    map<int, string> mapStudent;
    mapStudent[1] = "student_one";
    mapStudent[3] = "student_three";
    mapStudent[5] = "student_five";
    map<int, string>::iterator iter;
    iter = mapStudent.lower_bound(1);
    //返回的是下界1的迭代器
        cout<<iter->second<<endl;
    iter = mapStudent.lower_bound(2);
    //返回的是下界3的迭代器
        cout<<iter->second<<endl;
    iter = mapStudent.lower_bound(3);
    //返回的是下界3的迭代器
        cout<<iter->second<<endl;
    iter = mapStudent.upper_bound(2);
    //返回的是上界3的迭代器
        cout<<iter->second<<endl;
    iter = mapStudent.upper_bound(3);
    //返回的是上界5的迭代器
        cout<<iter->second<<endl;
    pair<map<int, string>::iterator, map<int, string>::iterator> mappair;
    mappair = mapStudent.equal_range(2);
    if(mappair.first == mappair.second)
        cout<<"Do not Find"<<endl;
    else
        cout<<"Find"<<endl;
    mappair = mapStudent.equal_range(3);
    if(mappair.first == mappair.second)
        cout<<"Do not Find"<<endl;
    else
        cout<<"Find"<<endl;
    return 0;
}

```

## 9、从map中删除元素

移除某个map中某个条目用erase（）  
该成员方法的定义如下：  
iterator erase（iterator it);//通过一个条目对象删除  
iterator erase（iterator first，iterator last）//删除一个范围  
size_type erase(const Key&key);//通过关键字删除  
clear()就相当于enumMap.erase(enumMap.begin(),enumMap.end());  
   
这里要用到erase函数，它有三个重载了的函数，下面在例子中详细说明它们的用法  

```
#include <map>  
  
#include <string>  
  
#include <iostream>  
  
using namespace std;  
  
int main()
{
    map<int, string> mapStudent;
    mapStudent.insert(pair<int, string>(1, "student_one"));
    mapStudent.insert(pair<int, string>(2, "student_two"));
    mapStudent.insert(pair<int, string>(3, "student_three"));
    //如果你要演示输出效果，请选择以下的一种，你看到的效果会比较好
    //如果要删除1,用迭代器删除
    map<int, string>::iterator iter;
    iter = mapStudent.find(1);
    mapStudent.erase(iter);
    //如果要删除1，用关键字删除
    int n = mapStudent.erase(1);//如果删除了会返回1，否则返回0
    //用迭代器，成片的删除
    //一下代码把整个map清空
    mapStudent.erase( mapStudent.begin(), mapStudent.end() );
    //成片删除要注意的是，也是STL的特性，删除区间是一个前闭后开的集合
    //自个加上遍历代码，打印输出吧
}
```


## 10、map中的swap用法
 
map中的swap不是一个容器中的元素交换，而是两个容器所有元素的交换。

## 11、map的基本操作函数：
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
