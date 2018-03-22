# [转]Nginx多FastCGI配置

```
前言
Nginx自身不支持独立的外部程序调用，但是我们可以通过一些设置和处理来达到调用fcgi程序的目的。
本文解决两个问题：1、如何在一个Nginx的网页上面遇到.cgi请求的时候，启用外部的fcgi程序
                                 2、如何让Nginx服务器支持调用多个fcgi程序。
 
 1、原理性概述
          Fastcgi程序可以使用很多语言来编写，PHP，Python，C/C++等等，本文采用C语言来编写。Nginx不支持对外部程序的直接调用或者解析，所有的外部程序（包括php）都是需要通过FastCGI接口来调用的。而为了调用CGI程序，还需要一个叫做spawn-fcgi的程序，可以简单地理解为，要想通过Nginx启动FCGI程序，必须得先通过启动spawn-fast，由spawn-fast去传递Nginx启动的请求，可以把spawn-cgi理解为一个中间搭桥的。
 
2、获取fcgi和spawn-fcgi的源码库（配置编译都是在Linux环境下）
      源码下载云盘 http://pan.baidu.com/s/1bo2FpN5
    fcgi
     （1）要编写fastcgi程序，需要使用到fastcgi的头文件。要运行fastcgi程序需要依赖库文件。通过fastcgi源码去         得到头文件和库
      将下载好的fastcgi压缩文件解压，
     
    （2）进入解压后的源码目录， 在解压后的目录中创建文件夹 _install  因为我的习惯是把配置编译生成出来的东西都放到指定文件夹下面，这样要查找东西很方便，特别是在解压配置编译一个比较大的源码的时候
     
    （3）然后进入include目录，找到fcgio.h文件
   
   打开该文件，加入一行代码 #include <cstdio> ，
#include <iostream>
#include "fcgiapp.h"
#include <cstdio>  //添加这一行
#ifndef DLLAPI
#ifdef _WIN32
#define DLLAPI __declspec(dllimport)
这是因为gcc编译器更新的比较快，比较新，而fastcgi版本比较旧，可能存在一些不兼容的问题，在make的时候会报错。
    （4）然后配置，通过参数--prefix来指定一会make install的文件都放到指定目录，prefix后面跟的是绝对路径，大家根据自己的实际情况来填写路径，只要最后指到新建的_install目录就正确。配置命令如下：
     ./configure  --prefix=/home/fastcgi/fcgi/fcgi-2.4.0/_install
    配置完成以后就编译
    依次输入命令：
    make
    make  install
    然后就可以在_install目录中看到生成的文件了。
 
把_install/lib下面的libfcgi.so.0库拷贝到/usr/lib/目录下面,就算大功告成了。
 
   spawn-fcgi
（1）
 解压，进入源码目录，方法同上，新建_install目录。
在配置之前先运行./autogen.sh
 
（2）配置
./configure  --prefix=/home/fastcgi/fcgi/spawn-fcgi-1.6.3/_install
 
（3）然后依次输入
make
make install
（4）进入到_install目录
 
把bin目录下生成的程序拷贝到nginx服务器的安装目录下的sbin目录里面去，例如我的安装目录是
/server/nginx/sbin,如果nginx是默认安装，一般会是/usr/local/nginx/sbin/这个目录。
 
至此，fastcgi和spawn-fcgi就算准备好了。
 
3、编写fcgi程序
   

这个程序最好放到刚刚解压fastcgi源码的那个目录下面去，就是放到这里：

 
fcgi.c就是编写的C程序。
有两点稍微说明一下：
（1）、在while(FCGI_Accept() >= 0)循环的外面可以放一些变量定义等等，实际的操作语句放到while循环里面，fcgi的工作方式是，网页一旦请求，那么就触发fcgi程序，每请求一次，while就循环一次。
（2）、"Conten-type:text/html\r\n"这个代码一定要加上。
 
接下来编译：
gcc -lfcgi fcgi.c -o hellofcgi
生成fcgi程序。
将该程序拷贝到nginx的安装目录下的某个文件夹，可以自己新建一个cgibin，完整目录是/server/nginx/cgibin，把程序移到这个文件夹中。记得检查一下hellofcgi程序权限。
 
4、配置相关文件
打开nginx的配置文件，目录位置是/server/nginx/conf/   有一个名为nginx.conf的文件，打开它，在server节点下面添加如下代码：（#注释的部分不用添加），这种配置称为A，下面还有一种对比的配置。

 
把配置文件中的其他部分也贴出来，方便大家查找，就把上面的代码加到下面代码后面就行了
 

有些小伙伴可能发现自己打开了nginx.conf配置文件，但是却找不到server节点，这有可能是nginx把配置文件拆成几个部分了，检查一下nginx配置文件最下面有没有如下代码，

 
意思是说，还有vhosts目录下的conf文件也被包含进来，那么这时候就进到所示目录下，打开conf文件，就能找到server节点了。
 
另外一种配置方式，添加下面代码： 称为配置方式B
 location ~ \.cgi$ {
        fastcgi_pass 127.0.0.1:8088;
        fastcgi_index index.cgi;
        fastcgi_param SCRIPT_FILENAME fcgi$fastcgi_script_name;
        include fastcgi_params;
    }
 
方式A和方式B的对比:
在A中，网页上来的请求，必须是hellofcgi.cgi，Nginx有这个请求，那么spawn就会查找与hellofcgi配对的模块，那么一查找就能找到nginx/cgibin/目录下的hellofcgi程序。这就为多条fcgi程序奠定下了基础，网页上可以来的也可以是hifcgi.cgi请求，那么就在配置文件当中再去添加一项，换一个端口就行了，比如8089端口，然后location后面的名字就是/hifcgi.cgi，那么网页上来的是hifcgi.cgi请求的时候，就会去配对到hifcgi模块。
配置方式B，意思为无论网页上来的是什么cgi请求，我都传到8088这个端口绑定的cgi模块上面去，比如我们8088端口绑定的hellofcgi（下面会讲如何使用spawn-fcgi做绑定），那么不论网页上是什么cgi请求，不论是hellofcgi.cgi、1.cgi、2.cgi等等，都统统交给hellofcgi模块来处理，这样的话就相当于Nginx只能绑定一个外部的fcgi程序。
所以综上，想要Nginx支持多个fcgi程序，就使用配置方式A。当然，有几个程序就要添加几个端口。
 
5、使用spawn-fcgi绑定端口
进入到/nginx/sbin/目录下面，启用spawn-fcgi，代码如下：（根据自己的实际情况填写路径）
   ./spawn-fcgi -a 127.0.0.1 -p 8088 -f /server/nginx/cgibin/hellofcgi
其中，127.0.0.1是本地主机地址（这里的端口和IP地址要和Nginx的配置文件里的一样），如果你是有公网IP的，就绑定公网IP，端口8088，绑定之前使用netstat -tunlp查看一下端口使用情况，不要占用其他程序的端口。
 
如果要使用多个fcgi程序，那么就要绑定不同的端口，绑定之前确定在nginx的配置文件当中添加了相关的代码（就只有端口和location后面的名字不一样）。多个程序的时候每个程序的名字很重要，比如说有hellofcgi1程序和hellofcgi2程序，那么在nginx配置文件当中添加上相应代码。并把这两个程序放到/nginx/cgibin目录下，绑定上相应的端口，网页的请求如果是http://localhost/hellofcgi1.cgi（如果绑定的是本地ip地址，浏览器里面输入localhost就相当于127.0.0.1的地址），那么就会去调用hellofcgi1程序，如果网页请求是http://localhost/hellofcgi2.cgi，那么就会调用hellofcgi2程序。
 
6、重启Nginx
上面的步骤做好以后，就需要重启Nginx服务器了，然后在浏览器当中去输入http://localhost/hellofcgi.cgi就能看到有所显示了~
 

 
7、结语
到这里就全部介绍完了，当然只是稍微领进门，后面如何深入diy还需要各位小伙伴自己发挥。另外有一点提醒一下，在编写fcgi程序的时候，所有对于c语言本身的操作，路径都是相对于根目录而言的；所有对于网页的操作，路径都是对于网页站点的目录而言的。我当时因为忽略了这一点费了不少事。
比如说：
A： readdir(dir)
B :   printf( "<img src=\"/sd/%s\" width=\"240\" height=\"200\" />",“hello.jpg”);  //在网页上显示一幅图片
 
A和B的路径如果说一样的话，那么A中dir的路径应该是/server/contents/sd
而B中直接就是/sd，AB最终指向的都是同一个目录，但是由于A是C语言代码，无视web服务器（这样说好像也不太准确，但就是那个意思），所以说对它而言的路径就是根目录，而B当中，是对网页进行操作，实际上是HTML语言，这里的printf实际上做了另外的宏定义了（在fastcgi的源码头文件里面，感兴趣的可以自己找找）。而我的Nginx站点目录是/server/contents，所以对于B而言/server/contents就成了根目录。


```
