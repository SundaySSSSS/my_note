# C++读写文件

``` C++
#include "stdafx.h"  
#include <vector>  
#include <string>  
#include <fstream>  
#include <iostream>  
using namespace std;  
int _tmain(int argc, _TCHAR* argv[])  
{  
    ifstream myfile("E:\\hello.txt");  
    ofstream outfile("E:\\out.txt", ofstream::app);  
    string temp;  
    if (!myfile.is_open())  
    {  
        cout << "未成功打开文件" << endl;  
    }  
    while(getline(myfile,temp))  
    {  
        outfile<<temp;  
    }  
    myfile.close();  
    return 0;  
}
```