# CJson使用方法
代码见附件, 于2018/02/14下载
# 1 解析Json数据
如果要解析以下的Json数据：  
```
{
    "programmers": [{
        "firstName": "Brett",
        "lastName": "McLaughlin",
        "id": 1
    }, {
        "firstName": "Jason",
        "lastName": "Hunter",
        "id": 2
    }, {
        "firstName": "Elliotte",
        "lastName": "Harold",
        "id": 3
    }]
}
```

首先把上述Json数据写入char* jsonStr中，之后，调用
`cJSON* root = cJSON_Parse(jsonStr);`

得到Json数据指针root  
root中存在一个节点，名称为programmers，内容为一个数组，  
调用：  
`cJSON* programmersNode = cJSON_GetObjectItem(root, "programmers");`

得到该节点。由于此节点内容为一个数组，可以使用：  
`int iSize = cJSON_GetArraySize(programmersNode);`

取得此数组的元素个数  
如果要取出某一个元素，可以使用：  
`cJSON* firstMan = cJSON_GetArrayItem(programmersNode, 0);`


上述代码取得了第一个人的数据，即
```
{
        "firstName": "Brett",
        "lastName": "McLaughlin",
        "id": 1
}
```

要取出每一个元素，可以使用：  
```
cJSON* firstName = cJSON_GetObjectItem(programmers[i], "firstName");
cJSON* lastName = cJSON_GetObjectItem(programmers[i], "lastName");
cJSON* id = cJSON_GetObjectItem(programmers[i], "id");
```

如果要输出每一个元素的值：
```
cout << "id: " << id->valueint << endl;
cout << "FirstName: " << firstName->valuestring << endl;
cout << "lastName: " << lastName->valuestring << endl;
```

解析完毕后，要对空间进行释放：（只需要删除根节点即可）
`cJSON_Delete(root);`

至此，已经将Json数据基本解析完毕，其余部分类似。解析部分代码如下：  
```
/* 解析Json函数 */
BOOL ParseJson(const char* jsonStr)
{
    cJSON* root = cJSON_Parse(jsonStr);
    BOOL ret = FALSE;
    if (root != NULL)
    {
        cJSON* programmersNode = cJSON_GetObjectItem(root, "programmers");
        if (programmersNode != NULL)
        {
            int iSize = cJSON_GetArraySize(programmersNode);
            if (iSize == 3)
            {
                cJSON* programmers[3] = {0};
                for (int i = 0; i < 3; ++i)
                {
                    programmers[i] = cJSON_GetArrayItem(programmersNode, i);
                    if (programmers[i] != NULL)
                    {
                        cJSON* firstName = cJSON_GetObjectItem(programmers[i], "firstName");
                        cJSON* lastName = cJSON_GetObjectItem(programmers[i], "lastName");
                        cJSON* id = cJSON_GetObjectItem(programmers[i], "id");
                        if (firstName != NULL && lastName != NULL && id != NULL)
                        {
                            cout << "id: " << id->valueint << endl;
                            cout << "FirstName: " << firstName->valuestring << endl;
                            cout << "lastName: " << lastName->valuestring << endl;
                        }
                        else
                        {
                            cJSON_Delete(root);
                            return FALSE;
                        }
                    }
                }
                ret = TRUE;
            }
        }
    }
    cJSON_Delete(root);
    return ret;
}
```
# 2 生成Json数据
生成Json数据主要用到如下函数
```
cJSON_CreateObject  //创建一个节点
cJSON_CreateArray   //创建一个数组
cJSON_AddStringToObject //将一个字符串加入一个节点
cJSON_AddNumberToObject //将一个整数加入一个节点
cJSON_AddItemToArray    //将另一个节点加入数组
```
如果要生成如下的Json串：  
```
{
        "programmers":  [{
                        "firstname":    "Brett",
                        "lastName":     "McLaughlin",
                        "id":   1
                }]
}
```
使用的代码如下：  

```
BOOL MakeJson()
{
    cJSON *temp = cJSON_CreateObject();
    if (temp == NULL)
    {   //创建失败
        return FALSE;
    }
    //加入节点(键值对)
    cJSON_AddStringToObject(temp, "firstname", "Brett");
    cJSON_AddStringToObject(temp, "lastName", "McLaughlin");
    cJSON_AddNumberToObject(temp, "id", 1);
    cJSON * array = cJSON_CreateArray();
    if (array == NULL)
    {   //创建失败
        cJSON_Delete(temp);
        return FALSE;
    }
    cJSON_AddItemToArray(array, temp);
 
    cJSON *root = cJSON_CreateObject();
    if (root == NULL)
    {   //创建失败
        cJSON_Delete(temp);
        cJSON_Delete(array);
        return FALSE;
    }
    cJSON_AddItemToObject(root, "programmers", array);
 
    char* strJson = cJSON_Print(root);
    cout << strJson << endl;
    free(strJson);
    cJSON_Delete(root);
}
```
打印Json串的方法： 
root是一个cJSON的节点，打印此节点下的所有内容：
```
char* strJson = cJSON_Print(root);
cout << strJson << endl;
free(strJson);
```