# Nginx移植说明

```


1. 版本说明
虚拟机系统：Linux Ubuntu 10.04
交叉编译环境：dm8168 (DVRRDK_02.00.00.23)
Nginx 版本：1.6.0
Zlib   版本：1.2.3
Pcre  版本：8.32
2. 准备工作
Ø 在Linux系统目录建立一个文件夹nginx，此处建立到/dm81689_work/目录下
Ø 将nginx-1.6.0.tar.gz、pcre-8.32.tar.gz、zlib.tar.bz2解压到nginx文件夹下
3. 修改nginx源码
	1. 修改auto/cc/name
	 
		if [ "$NGX_PLATFORM" != win32 ]; then
		
		    ngx_feature="C compiler"
		    ngx_feature_name=
		    #ngx_feature_run=yes
		    ngx_feature_run=no   ==>set to no to skip check
		    ngx_feature_incs=
		    ngx_feature_path=
	2. 修改auto/types/sizeof
	ngx_test="$CC $CC_TEST_FLAGS $CC_AUX_FLAGS
	    ==> ngx_test="gcc $CC_TEST_FLAGS $CC_AUX_FLAGS
	3. 修改src/os/unix/ngx_errno.h
	at line 15 add #define NGX_SYS_NERR 333
	4. 修改auto/lib/pcre/make
	 ./configure --disable-shared $PCRE_CONF_OPT 
	    ==>./configure --disable-shared $PCRE_CONF_OPT --host=arm
	5. 修改src/os/unix/ngx_shm.c
	打开NGX_HAVE_MAP_ANON编译条件。
	6. 在nginx-1.6.0目录下建立my_configure.sh脚本
	#!/bin/sh
	BUILD_PATH=/usr/local/nginx
	CC_PATH=/opt/DVRRDK_02.00.00.23/ti_tools/cgt_a8/arm-2009q1/bin/arm-none-linux-gnueabi-gcc
	CPP_PATH=/opt/DVRRDK_02.00.00.23/ti_tools/cgt_a8/arm-2009q1/bin/arm-none-linux-gnueabi-g++
		./configure \
		  --prefix=$BUILD_PATH \
		  --user=root \
		  --group=root \
		  --builddir=$BUILD_PATH\build \
		  --with-zlib=/dm8168_work/Nginx/zlib-1.2.3 \
		  --with-pcre \
		  --with-pcre=/dm8168_work/Nginx/pcre-8.32 \
		  --with-pcre-jit \
		  --with-cc=$CC_PATH  \
	        --with-cpp=$CPP_PATH
	备注：/usr/local/目录若不存在，需要手动建立。
 
4. 完成移植 
 
第一步：进入编译目录
	#cd /dm8168_work/nginx
第二步：执行配置脚本
	#./ my_configure.sh
第三步：编译
		#make
		#make install
第四步：编译完成
5. 运行nginx服务器
Ø 将生成的/usr/local/nginx目录拷贝到dm8168平台相对应的目录
Ø 测试：# /usr/local/nginx/sbin/nginx –t,成功提示如下：
	2008/12/16 09:08:35 [info] 28412#0: the configuration file /usr/local/nginx/conf/nginx.conf
	syntax is ok
	2008/12/16 09:08:35 [info] 28412#0: the configuration file /usr/local/nginx/conf/nginx.conf was
	tested successfully 
Ø Nginx 启动：
	# /usr/local/nginx/sbin/nginx
6. nginx添加fastcgi接口
	1. 本次使用模块版本
	spawn-fcgi-1.6.3.tar.gz:fastcgi 管理器。
	fcgi-2.4.0.tar.gz：fastcgi 库。
 
	2. 生成spawn-fcgi
Ø 解压spawn-fcgi-1.6.3.tar：#tar –zxvf spawn-fcgi-1.6.3.tar.gz
Ø 进入spawn-fcgi-1.6.3目录：#cd spawn-fcgi-1.6.3
Ø 配置交叉编译：# ./configure CC=/opt/DVRRDK_02.00.00.23/ti_tools/cgt_a8/arm-2009q1/bin/arm-none-linux-gnueabi-gcc --host=arm-linux
Ø 生成spawn-fcgi：#make -- #make install
Ø 将生成在src目录下的spawn-fcgi 拷贝到/usr/local/nginx/sbin/ 目录
	3. 生成fcgi库
Ø 解压fcgi-2.4.0.tar.gz：#tar –zxvf fcgi-2.4.0.tar.gz
Ø 进入fcgi-2.4.0目录：#cd fcgi-2.4.0
Ø 配置交叉编译：/configure CC=/opt/DVRRDK_02.00.00.23/ti_tools/cgt_a8/arm-2009q1/bin/arm-none-linux-gnueabi-gcc CXX=/opt/DVRRDK_02.00.00.23/ti_tools/cgt_a8/arm-2009q1/bin/arm-none-linux-gnueabi-g++ --host=arm-linux
Ø 生成fcgi库：#make -- #make install
Ø 根据需要将 libcgi/.libs/libfcgi.a libfcgi++.a 拷贝到指定目录，用于编写fastcgi程序。
	4. 编写fastcgi测试程序
Ø 建立cgidemo文件夹
Ø 将fcgi-2.4.0目录下的include文件夹拷贝到cgidemo目录
Ø 在cgidemo目录建立lib文件夹
Ø 将libfcgi.a libfcgi++.a文件拷贝到lib目录中
Ø cgidemo目录下编写demo.c文件：
			#include "fcgi_stdio.h"
			#include <stdlib.h>
			 
			int main() 
			{
			    int count = 0;
			    while (FCGI_Accept() >= 0) {
			        printf("Content-type: text/html\r\n"
			                "\r\n"
			                ""
			                "FastCGI Hello!"
			                "Request number %d running on host%s "
			                "Process ID: %d\n", ++count, getenv("SERVER_NAME"), getpid());
			    }
			    return 0;
		}
Ø cgidemo目录下编写Makefile文件：
			# Makefile
			 
			#定义目标文件(最终生成文件)
			TARGET = demo
			 
			#指定引用目录, -I 指定编译的引用目录
			INCLUDES += -I./include
			 
			#g++编译选项，可编译 .c和.cpp的文件
			COMPILE.c = /opt/DVRRDK_02.00.00.23/ti_tools/cgt_a8/arm-2009q1/bin/arm-none-linux-gnueabi-g++ $(INCLUDES)
			#gcc编译选项，只可编译 .c的文件
			LINK.c = /opt/DVRRDK_02.00.00.23/ti_tools/cgt_a8/arm-2009q1/bin/arm-none-linux-gnueabi-gcc $(INCLUDES)
			 
			#源文件
			SOURCES = $(wildcard *.c)
			#头文件
			HEADERS = /dm8168_work/Nginx/cgidemo/include/*.h
			 
			RELOBJFILES = $(SOURCES:%.c=%.o)
			 
			LIBS = /dm8168_work/Nginx/cgidemo/lib/libfcgi.a /dm8168_work/Nginx/cgidemo/lib/libfcgi++.a
			 
			 
			all: $(RELOBJFILES)
				$(COMPILE.c) -o $(TARGET) $(RELOBJFILES) $(LIBS)
			 
			$(RELTARGET): 
			#.cpp文件编译规则
			%.o: %.cpp
				$(COMPILE.c) -c $< -o $@
			#.c文件编译规则
			%.o: %.c
				$(LINK.c) -c $< -o $@
			 
			#清除命令，在此处要删除编译过程中生成的中间.o .a 文件和目标文件
			clean:    
			-$(RM) -rf *.o
Ø 生成测试fastcgi程序
		在cgidemo目录下执行编译：#make
Ø 将生成的demo可执行程序拷贝到/usr/local/nginx/cgi-bin/目录，如果目录不存在则自己建立一个
	5. 测试fastcgi
Ø 启动fastcgi进程：
		/usr/local/nginx/sbin/spawn-fcgi -a 127.0.0.1 -p 8081 -f /usr/local/nginx/cgi-bin/demo -F 1
		备注：此处为fastcgi程序 监听本地8081端口，-F 后为ginx收到cgi请求后，会看有多少个该cgi程序的进程（spawn-fcgi -F指定的参数），然后根据并发量来调用(调度)cgi程序。
Ø 配置nginx
		进入/usr/local/nginx/conf目录。
		打开nginx.conf配置文件。
		配置fastcgi，nginx.conf文件如下，红色部分为配置fastcgi
			#user  nobody;
			worker_processes  1;
			 
			#error_log  logs/error.log;
			#error_log  logs/error.log  notice;
			#error_log  logs/error.log  info;
			 
			#pid        logs/nginx.pid;
			 
			 
			events {
			    #use epoll;
			    worker_connections  50;
			}
			 
			 
			http {
			    include       mime.types;
			    default_type  application/octet-stream;
			 
			    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
			    #                  '$status $body_bytes_sent "$http_referer" '
			    #                  '"$http_user_agent" "$http_x_forwarded_for"';
			 
			    #access_log  logs/access.log  main;
			 
			    sendfile        on;
			    #tcp_nopush     on;
			 
			    #keepalive_timeout  0;
			    keepalive_timeout  65;
			 
			    server_names_hash_bucket_size 128;
			    client_header_buffer_size 2k;
			    large_client_header_buffers 4 4k;
			    client_max_body_size 8m;
			    #sendfile on;
			    tcp_nopush     on;
			 
			   fastcgi_cache_path /usr/local/nginx/fastcgi_cache levels=1:2  keys_zone=TEST:10m  inactive=5m;
			   fastcgi_connect_timeout 300;
			   fastcgi_send_timeout 300;
			   fastcgi_read_timeout 300;
			   fastcgi_buffer_size 64k;
			   fastcgi_buffers 8 64k;
			   fastcgi_busy_buffers_size 128k;
			   fastcgi_temp_file_write_size 128k;
			   fastcgi_cache TEST;
			   fastcgi_cache_valid 200 302 1h;
			   fastcgi_cache_valid 301 1d;
			   fastcgi_cache_valid any 1m;
			   fastcgi_cache_min_uses 1;
			   fastcgi_cache_use_stale error timeout invalid_header http_500;
			   open_file_cache max=204800 inactive=20s;
			   open_file_cache_min_uses 1;
			   open_file_cache_valid 30s;
			   tcp_nodelay on;
			 
			 
			 
			    server {
			        listen       80;
			        server_name  localhost;
			 
			        #charset koi8-r;
			 
			        #access_log  logs/host.access.log  main;
			 
				#默认打开主页
			        location / {
			            root   html;
			            index  MainIndex.html MainIndex.htm;
			        }
				#cgi处理
			     location ~ \.cgi$ {
					fastcgi_pass 127.0.0.1:8081;
					fastcgi_index cgi-bin/demo;
					include fastcgi.conf;
					include fastcgi_params;
			        }
			 
			        #error_page  404              /404.html;
			 
			        # redirect server error pages to the static page /50x.html
			        #
			        error_page   500 502 503 504  /50x.html;
			        location = /50x.html {
			            root   html;
			        }
			    }
		}
Ø 启动nginx服务器：
		/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf
Ø 在网页上测试
		在地址栏输入：http://serverip:server port(80端口可以不写)/*.cgi
Ø 测试完成。


```

