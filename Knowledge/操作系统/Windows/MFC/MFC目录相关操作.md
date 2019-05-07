# MFC目录相关操作
## 判定目录是否存在
```C++
PathFileExists(path)
```

## 递归创建路径
```
#include <vector>

bool CreateMultipleDirectory(const CString& szPath)
{
	CString strDir(szPath);    //存放要创建的目录字符串

	if (strDir.GetAt(strDir.GetLength() - 1) != _T('\\'))  //确保以'\'结尾以创建最后一个目录
	{
		strDir.AppendChar(_T('\\'));
	}

	std::vector<CString> vPath;              //存放每一层目录字符串
	CString strTemp;                    //一个临时变量,存放目录字符串
	bool bSuccess = false;              //成功标志

	//遍历要创建的字符串
	for (int i = 0; i < strDir.GetLength(); ++i)
	{
		if (strDir.GetAt(i) != _T('\\'))
		{                               //如果当前字符不是'\\'
			strTemp.AppendChar(strDir.GetAt(i));
		}
		else
		{                                //如果当前字符是'\\'
			vPath.push_back(strTemp);    //将当前层的字符串添加到数组中
			strTemp.AppendChar(_T('\\'));
		}
	}
	//遍历存放目录的数组,创建每层目录
	std::vector<CString>::const_iterator vIter;
	for (vIter = vPath.begin(); vIter != vPath.end(); vIter++)
	{
		if (!PathIsDirectory(*vIter))    //判断当前目录时候存在，不存在就创建
		{
			//如果CreateDirectory执行成功,返回true,否则返回false
			bSuccess = CreateDirectory(*vIter, NULL) ? true : false;
		}
	}
	return bSuccess;
}
```

