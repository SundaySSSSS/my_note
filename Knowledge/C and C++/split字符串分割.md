# split字符串分割
C++标准库里面没有字符分割函数split ，这可太不方便了，我已经遇到>3次如何对字符串快速分割这个问题了。列几个常用方法以备不时之需。
 
* 方法一: 利用STL自己实现split 函数(常用，简单，直观)
原型: vector<string> split(const string &s, const string &seperator);
输入一个字符串，一个分隔符字符串(可包含多个分隔符)，返回一个字符串向量。这是我最喜欢的方法，因为它最直观，在平常也最常用。实现及测试代码如下

```
 #include <vector>
#include <string>
#include <iostream>
using namespace std;
 
vector<string> split(const string &s, const string &seperator){
  vector<string> result;
  typedef string::size_type string_size;
  string_size i = 0;
  
  while(i != s.size()){
    //找到字符串中首个不等于分隔符的字母；
    int flag = 0;
    while(i != s.size() && flag == 0){
      flag = 1;
      for(string_size x = 0; x < seperator.size(); ++x)
    if(s[i] == seperator[x]){
      ++i;
      flag = 0;
      break;
    }
    }
    
    //找到又一个分隔符，将两个分隔符之间的字符串取出；
    flag = 0;
    string_size j = i;
    while(j != s.size() && flag == 0){
      for(string_size x = 0; x < seperator.size(); ++x)
    if(s[j] == seperator[x]){
      flag = 1;
      break;
    }
      if(flag == 0) 
    ++j;
    }
    if(i != j){
      result.push_back(s.substr(i, j-i));
      i = j;
    }
  }
  return result;
}
 
int main(){
  string s = "a,b*c*d,e";
  vector<string> v = split(s, ",*"); //可按多个字符来分隔;
  for(vector<string>::size_type i = 0; i != v.size(); ++i)
    cout << v[i] << " ";
  cout << endl;
  //输出: a b c d
}
```

@egmkang 提供了一段更简洁高效的代码，实现如下:

```
void SplitString(const std::string& s, std::vector<std::string>& v, const std::string& c)
{
  std::string::size_type pos1, pos2;
  pos2 = s.find(c);
  pos1 = 0;
  while(std::string::npos != pos2)
  {
    v.push_back(s.substr(pos1, pos2-pos1));
 
    pos1 = pos2 + c.size();
    pos2 = s.find(c, pos1);
  }
  if(pos1 != s.length())
    v.push_back(s.substr(pos1));
}

```

* 方法二: 用C语言中的strtok 函数来进行分割
原型:  char *strtok(char *str, const char *delim);
strtok函数包含在头文件<string.h>中，对于字符数组可以采用这种方法处理。当然也可以将字符数组转换成字符串之后再使用法一。测试代码如下

```
#include <string.h>
#include <stdio.h>
 
int main(){
  char s[] = "a,b*c,d";
  const char *sep = ",*"; //可按多个字符来分割
  char *p;
  p = strtok(s, sep);
  while(p){
    printf("%s ", p);
    p = strtok(NULL, sep);
  }
  printf("\n");
  return 0;
}
//输出: a b c d
```
 
* 方法三: boost库中包含了split 函数
boost库有很多方法来实现split，也包含了一个split函数，可以直接使用，非常实用而且强大，但是得自己下载boost库。使用代码如下

```
#include <boost/algorithm/string.hpp>
#include <iostream>
#include <string>
#include <vector>
 
using namespace std;
using namespace boost;
 
void print( vector <string> & v )
{
  for (size_t n = 0; n < v.size(); n++)
    cout << "\"" << v[ n ] << "\"\n";
  cout << endl;
}
 
int main()
{
  string s = "a,b, c ,,e,f,";
  vector <string> fields;
 
  cout << "Original = \"" << s << "\"\n\n";
 
  cout << "Split on \',\' only\n";
  split( fields, s, is_any_of( "," ) );
  print( fields );
 
  cout << "Split on \" ,\"\n";
  split( fields, s, is_any_of( " ," ) );
  print( fields );
 
  cout << "Split on \" ,\" and elide delimiters\n"; 
  split( fields, s, is_any_of( " ," ), token_compress_on );
  print( fields );
 
  return 0;
}

输出结果如下：

Original = "a,b, c ,,e,f,"
 
Split on ',' only
"a"
"b"
" c "
""
"e"
"f"
""
 
Split on " ,"
"a"
"b"
""
"c"
""
""
"e"
"f"
""
 
Split on " ," and elide delimiters
"a"
"b"
"c"
"e"
"f"
""
```

