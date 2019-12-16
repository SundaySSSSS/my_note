# QT 生成和解析Json
## 生成Json
### 生成键值结构
``` json
"time": 2345
```

``` C++
QJsonObject obj;
obj.insert("time", 2345);
```

### 生成多级结构
``` json
"studentInfo": {
        "name": "cxy",
        "age": 29,
        "number": "090010"
}
```

``` C++
QJsonObject obj;
obj.insert("name", "cxy");
obj.insert("age", 29);
obj.insert("number", "090010");

root.insert("studentInfo", obj);
```

### 生成数组
``` json
"studentList": [
        "cxy",
        "zlp",
        "zhf",
        "cmc"
    ],
```
``` C++
QJsonArray jsonArray;
jsonArray.push_back("cxy");
jsonArray.push_back("zlp");
jsonArray.push_back("zhf");
jsonArray.push_back("cmc");

```

### 生成最终Json
``` C++
QJsonDocument doc;
doc.setObject(obj);
baJson = doc.toJson();
```

## 解析Json
### 获取根节点
``` C++
QJsonObject rootObj;
if (!GetRootFromJson(rootObj, baJson))
{   //获取根节点失败
    return false;
}
```

``` C++
bool GetRootFromJson(QJsonObject &rootObj, const QByteArray &baJson)
{
    bool bRet = true;
    QJsonParseError jsonError;
    QJsonDocument parser = QJsonDocument::fromJson(baJson, &jsonError);
    if (!parser.isNull() && (jsonError.error == QJsonParseError::NoError))
    {
        if (parser.isObject())
        {
            rootObj = parser.object();
        }
        else
        {
            qDebug() << "json root not object";
            bRet = false;
        }
    }
    else
    {
        qDebug() << "create parser error";
        bRet = false;
    }

    if (rootObj.isEmpty())
    {
        qDebug() << "json parser root empty!";
        bRet = false;
    }
    return bRet;
}
```

### 解析键值结构
``` C++
if (rootObj.contains(JSON_SQL_TIME))
{
    QJsonValue tempNode = rootObj.value(JSON_SQL_TIME);
    long long i64Time = tempNode.toString().toLongLong();
}
```

### 解析多级结构
``` C++
if (rootObj.contains("studentInfo"))
{
    QJsonValue studentInfo = rootObj.value("studentInfo");
    if (studentInfo.isObject())
    {
        QJsonObject info = studentInfo.toObject();
        QStringList infoKeys = info.keys();
        foreach (QString key, infoKeys)
        {
            qDebug() << key << info[key].toVariant();
        }
    }
}

```

### 解析数组
``` C++
if (rootObj.contains("field"))
{
    QJsonValue fieldName = rootObj.value("field");
    if (fieldName.isArray())
    {
        QJsonArray arrFieldName = fieldName.toArray();
        for (int i = 0; i < arrFieldName.size(); ++i)
        {
            QJsonValue fieldNameValue = arrFieldName.at(i);
            qDebug() << fieldNameValue.toString();
        }
    }
}
```