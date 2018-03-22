# Python网页解析

## 使用Python解析网页的步骤
1. 使用BeautifulSoup解析网页
`Soup = BeautifulSoup(html, 'lxml')`
2. 描述要爬取的东西在哪
`Soup.select(  ...  )`
3. 从标签中获取需要的信息

### 第一步: 使用BeautifulSoup解析网页
基础用法
`Soup = BeautifulSoup(html, 'lxml')`
可以理解为
`汤 = BeautifulSoup(汤料, 食谱)`
汤: 解析出来的东西
汤料: html
食谱: 解析html的工具, 常用的有
> html.parser
> lxml HTML
> lxml XML
> html5lib

### 第二步: 描述要爬取的东西在哪
通常使用chrome的方法为:
在想要的东西上点`右键->检查`
在弹出的网页代码中被标记的部分`右键->Copy->Copy Selector`
复制出来的东西类似于
`body > div:nth-child(6) > div > div.v1-bangumi-info-img > a > img`
然后在Soup的select中指明
注意, 通常复制出来的内容中有解析不了的内容, 
如上面的`nth-child`需要改为`nth-of-type`
`images = Soup.Select('body > div:nth-of-type(6) > div > div.v1-bangumi-info-img > a > img')`

### 第三步: 从标签中获取需要的信息
#### get_text
如果是获取文本信息, 可以通过get_text方法来获取
例如:
```
titles = Soup.select('body > div > div > div.v1-bangumi-info > div.v1-bangumi-info-body > div > div.v1-bangumi-list-part-wrapper.slider-part-wrapper > ul > div.complete-list > div > div.slider-list-content > div > ul > li > a')
for title in titles:
    print(title.get_text())
```
#### get
类似的, 图片通常是一个属性, 可以通过get方法来获得
`print(images.get('src'))`
#### stripped_strings
当需要获取多个内容时, 可以使用此方法, 通常将返回的结果转换成list
```
cate = Soup.select('Somthing...')
list(cate.stripped_strings)
```




