# [C]全排列打印

## 思路
使用递归的方法
abcd的全排列可以分为:
a开头+bcd的全排列
b开头+acd的全排列
...

## 代码

```

#include <iostream>

using namespace std;

//从第k个元素到第m个元素进行排列
void permutation(char* a, int k , int m)
{
    int i, j;
    if (k == m)
    {
        for (i = 0; i <= m; i++)
        {
            cout<<a[i];
        }
        cout<<endl;
    }
    else
    {
        for (j = k; j <= m; j++)
        {
            swap(a[j], a[k]);
            permutation(a, k+1, m);
            swap(a[j], a[k]);
        }
    }
}

int main(void)
{
    char a[] = "abcdef";
    cout<<a<<" all the permutation:"<<endl;
    permutation(a, 0, 5);
    return 0;
}


```



