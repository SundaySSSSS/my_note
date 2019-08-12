# python爬虫
## 获取网络信息
### 基本理念
The Website is the API
## Requests库
### 安装
```
pip insstall requesets
```
### Requests库的基本方法
| 方法       | 说明                                       |
|------------+--------------------------------------------|
| requests() | 构造请求, 是以下方法的基础方法             |
| get()      | 获取HTML的主要方法, 对应于HTTP的GET        |
| head()     | 获取HTML网页头信息的方法, 对应于HTML的HEAD |
| post()     | 向网页提交POST请求                         |
| put()      | 向网页提交PUT请求                          |
| patch()    | 向HTML网页提交局部修改请求                 |
| delete()   | 向网页提交删除请求                         |

#### get方法
##### 基本形式:
``` python
r = requests.get(url) #返回的r是一个包含服务器资源的Response对象
```
##### 完整形式:
``` python
requests.get(url, params = None, **kwargs)
# url: 待获取网页的url
# params: url中的额外参数, 字典或字节流格式, 可选
# ## kwargs: 12个控制访问的参数
```

### Response对象
包含服务器资源的对象, 是requests相关方法的返回值
#### Response对象属性
| 属性                | 说明                                           |
|---------------------+------------------------------------------------|
| r.status_code       | http请求的返回状态, 200表示成功, 其他表示失败  |
| r.text              | http响应内容的字符串形式, 即url对应的页面内容  |
| r.encoding          | 从http header中猜测出的响应内容编码方式        |
| r.apparent_encoding | 从内容中分析出的响应内容编码方式(备选编码方式) |
| r.content           | http响应内容的二进制形式                       | 
备注: r.encoding中如果header中不存在charset, 则默认认为是ISO-8859-1  
而apparent_encoding是根据网页内容分析编码方式, 通常此字段更准确

### Request的异常
| 异常                     | 说明                                        |
|--------------------------+---------------------------------------------|
| request.ConnectionError  | 网络链接错误异常, 如DNS查询失败, 拒绝链接等 |
| request.HTTPError        | HTTP错误异常                                |
| request.URLRequired      | URL缺失异常                                 |
| request.TooManyRedirects | 超过最大重定向次数, 产生重定向异常          |
| request.ConnectTimeout   | 连接远程服务器超时异常                      |
| request.Timeout          | 请求URL超时, 产生超时异常                   |

可以使用r.raise_for_status()方法, 如果状态码不是200, 则抛出HTTPError

### 爬取网页的通用代码框架
``` python
import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status() # 如果状态码不是200, 则抛出HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))

```

## 网络爬虫盗亦有道
### 限制爬虫的手段:
#### 来源审查, 判断User-Agent进行限制
检查来访HTTP协议头的User-Agent域, 只响应浏览器或友好爬虫的访问

#### 发布公告, Robots协议
告知所有爬虫网站的爬取策略, 要求爬虫遵守
Robots协议全称为Robots Exclusion Standard网络爬虫排除标准
作用: 告知网络爬虫哪些页面可以爬取, 哪些不能. 如果不提供robots协议, 则默认说明任何爬虫可以爬取任何信息
形式: 在网站根目录下的robots.txt文件
##### 基本语法
# * 代表所有, /代表根目录
User-agent: *
Disallow: /
##### 案例: 京东的Robots协议
``` 
User-agent: *   # 任何网络爬虫都要遵守如下协议 
Disallow: /?*   # 任何爬虫都不能访问/?*
Disallow: /pop/*.html 	# 任何爬虫都不能访问/pop/*.html
Disallow: /pinpai/*.html?* # 基本同上
User-agent: EtaoSpider 
Disallow: / # EtaoSpider这个爬虫不允许爬取任何资源
User-agent: HuihuiSpider 
Disallow: / 
User-agent: GwdangSpider 
Disallow: / 
User-agent: WochachaSpider 
Disallow: /
```

##### Robots协议的遵守
网络爬虫要能够自动或人工识别robots.txt, 再进行内容爬取
网络爬虫如果不遵守Robots协议, 将面临法律风险

## 实例
### 京东商品页面的爬取
``` python
import requests

def getHTMLText(url):
    try:
        kv = {'usr-agent': 'Mozilla/5.0'}
        r = requests.get(url, timeout = 30, headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "https://item.jd.com/3707076.html"
    print(getHTMLText(url))

```

### 百度关键字提交
``` python
import requests

# 百度搜索引擎的关键词提交接口
# http://www.baidu.com/s?wd=keyword
# 其中keyword就是关键字

def getHTMLText(url, keyword):
    try:
        hd = {'usr-agent': 'Mozilla/5.0'}
        kw = { 'wd':keyword }
        r = requests.get(url, timeout = 30, headers = hd, params = kw)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print("The requests url = " + r.request.url)
        return r.text[:1000]
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://www.baidu.com/s"
    print(getHTMLText(url, 'Python'))

```

### 网络图片的爬取
``` python
import requests

# 网络图片链接的格式
# http://www.example.com/picture.jpg
# http://img1.gamersky.com/image2018/03/20180303_ll_136_10/gamersky_03small_06_201833173390C.jpg

path = "./abc.jpg"

url = "http://img1.gamersky.com/image2018/03/20180303_ll_136_10/gamersky_03small_06_201833173390C.jpg"
r = requests.get(url)
r.status_code
with open(path, 'wb') as f:
    f.write(r.content)
    f.close()
    
```

### 查询ip归属地
``` python
import requests

# 使用IP138的一个网站来查询ip地址归属地
# 此网站接口形式: http://m.ip138.com/ip.asp?ip=ipaddress

url = "http://m.ip138.com/ip.asp?ip="
try:
    r = requests.get(url + '202.204.80.112')
    print(r.requests.url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500: ])
except:
    print("爬取失败")
    print(r.status_code)

```

* 解析网络信息
## Beautiful Soup基本使用
### 概述
BeautifulSoup库是解析, 遍历, 维护html"标签树"的功能库

### 安装
``` 
pip3 install beautifulsoup4
```

### 基本使用
``` python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
```

### BeautifulSoup的基本元素
| 基本元素        | 说明                                                       |
|-----------------+------------------------------------------------------------|
| Tag             | 标签, 最基本的信息组织单元, 用<>和</>表明开头和结尾        |
| Name            | 标签的名字, <p>..</p>的名字是p, 格式: <tag>.name           |
| Attributes      | 标签的属性, 字典形式组织, 格式: <tag>.attrs                |
| NavigableString | 标签内非属性字符串, <>...</>中的字符串, 格式: <tag>.string |
| Comment         | 标签内的注释部分                                           |

例如:
一个简单的html
``` html
<html>
<head>
<title>This is a python demo page</title>
</head>
<body>
<p class="title">
	<b>The demo python introduces several python courses.</b>
</p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>
</body>
</html>
```

想要提取第一个<p>中的<b>的内容The demo...
方法如下:
``` python
import requests
r = requests.get("http://python123.io/ws/demo.html") # 上面demo的url
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo, "html.parser")
soup.p.b.string
```

### 基于BeautifulSoup的HTML遍历
#### 遍历相关的方法:
| 属性               | 说明                                                  |
|--------------------+-------------------------------------------------------|
| .contents          | 子节点的列表, 将<tag>的所有子节点存入列表             |
| .children          | 子节点的迭代类型, 与.contents相似, 用于循环遍历子节点 |
| .descendants       | 孙子节点的遍历类型, 包含所有子孙节点, 用于循环遍历    |
| .parent            | 节点的父亲标签                                        |
| .parents           | 节点先辈标签的迭代类型, 用于循环遍历先辈节点          |
| .next_sibling      | 返回HTML文本顺序的下一个平行节点标签                  |
| .previous_sibling  | 返回HTML文本顺序的上一个平行节点标签                  |
| .next_siblings     | .next_sibling的迭代类型                               |
| .previous_siblings | .previous_sibling的迭代类型                           |

#### 基本使用Demo
##### 下行遍历
``` python
for child in soup.body.children:
	print(child)
```

##### 上行遍历
``` python
#对a标签所有先辈标签
soup = BeautifulSoup(demo, "html.parser")
for parent in soup.a.parents:
	if parent is None:
		print(parent)
	else:
		print(parent.name)
```

##### 平行遍历
平行遍历必须在同一个父节点之下
``` python
soup = BeautifulSoup(demo, "html.parser")
for sibling in soup.a.next_siblings:
	print(sibling)
```

### 基于BeautifulSoup的输出
关键问题: 如何让Html内容更加友好的显示
``` python
soup.prettify()
soup.a.prettify() # 对某个标签友好显示
```
## 信息组织和提取
### 信息组织的三种形式
XML
JSON
YAML

### 信息提取的一般方法
#### 完整解析信息的标记形式, 再提取关键信息
如bs4库的标签树遍历
优点: 信息解析准确
缺点: 提取过程繁琐, 速度慢

#### 无视标记形式, 直接搜索关键字
优点: 提取过程简洁, 速度快
缺点: 提取结果准确性和信息内容相关

#### 两者结合的方法
例如: 提取HTML中的所有url链接
思路:
1, 搜索所有<a>标签
2, 解析<a>标签格式, 提取href后的链接内容
实例:
``` python
soup = BeautifulSoup(demo, "html.parser")
for link in soup.find_all('a'):
	print(link.get('href'))
```

### 查找HTML
#### find_all方法的基本形式
<>.find_all(name, attrs, recursive, string, **kwargs)
返回一个列表类型, 存储查找的结果
name: 对标签名称的检索字符串
attrs: 对标签属性值的检索字符串, 可标注属性检索
recursive: 是否对子孙全部检索, 默认为True
string: <>...</>中字符串区域的检索字符串

#### 具体例子:
``` python
soup.find_all('a') # 查找a标签
soup.find_all(['a','b']) # 查找a标签和b标签
soup.find_all(True) # 返回所有标签
# 打印所有标签
for tag in soup.find_all(True):
	print(tag.name)

# 搜索所有b开头的标签
for tag in soup.find_all(re.compile('b')):
	print(tag.name)

# 搜索名称为p, 属性中含有course的标签
soup.find_all('p', 'course');
# 搜索id属性为link1的标签
soup.find_all(id='link1')
# 搜索以id属性为link开头的标签
soup.find_all(id=re.compile('link'))

# 搜索字符串为Basic Python的标签
soup.find_all(string = "Basic Python")
# 搜索字符串中包含Python的标签
soup.find_all(stirng = re.compile("python"))

```

#### find_all的扩展方法
``` python
<>.find() # 搜索且只返回一个结果, 字符串类型, 同.find_all()参数
<>.find_parents() # 在先辈节点中搜索, 返回列表
<>.find_parent() # 在先辈节点中搜索, 返回字符串
<>.find_next_siblings() # 在后续平行节点中搜索, 返回列表
<>.find_next_sibling() # 在后续平行节点中搜索一个结果, 返回字符串
<>.find_previous_siblings()
<>.find_previous_sibling()
```

# 完整实例
## 爬取中国大学排名
功能描述:
输入: 大学排名url
输出: 大学排名信息屏幕输出

可行性判定:
取出html, 看看是否包含信息, 如果不在html中, 则需要其他技术支持
这个例子是可行的
url链接: http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html

``` python
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    # 经观察, 网页中信息均在tbody标签中的td标签内
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag): # 过滤掉不是Tag的内容
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])

def printUnivList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))

def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)

main()

```

## 淘宝商品信息定向爬虫
目标: 索取淘宝搜索页面的信息, 提取其中的商品名称和价格
需要做到:
1, 淘宝的搜索接口
2, 翻页的处理

``` python
import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt, html):
    try:
        priceList = re.findall(r'\"price\"\:\"[\d\.]*\"', html)
        titleList = re.findall(r'\"title\"\:\".*?\"', html)
        # print(priceList)
        for i in range(len(priceList)):
            price = eval(priceList[i].split(':')[1])
            title = eval(titleList[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("Error in parsePage")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = "键盘"
    depth = 2 # 爬取深度, 爬取几个页面
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(48*i)
            html = getHTMLText(url)
            # print(html[0:1500])
            parsePage(infoList, html)
        except:
            print("Error at page: " + str(i))
            continue
    printGoodsList(infoList)

main()

```
## 股票数据定向爬虫
### 功能描述
目标: 获取上交所和深交所的所有股票的名称和交易信息
输出: 保存到文件中
技术路线: request -> bs4 -> re

### 程序设计
1, 从东方财富网获取股票列表
2, 根据股票列表逐个到百度股票获取个股信息
3, 将结果存储到文件

### 具体代码
``` python
import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url, code = 'utf-8'):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""

def getStockList(lst, stockURL):
    html = getHTMLText(stockURL, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a') # 查找所有a标签
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0]) # sh或sz开头, 后面跟着6个数字
        except:
            continue

def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        # 制造合适的url
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs = {'class':'stock-bets'})
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            # print(name)
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding = 'utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
        except:
            # traceback.print_exc()
            count = count + 1
            print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
            continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'http://gupiao.baidu.com/stock/'
    output_file = 'BaiduStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    # print(slist)
    getStockInfo(slist, stock_info_url, output_file)

main()

```
```
