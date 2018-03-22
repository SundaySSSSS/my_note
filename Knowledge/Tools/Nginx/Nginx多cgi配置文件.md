# Nginx多cgi配置文件
```
#user  nobody;
worker_processes  2;

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
	#access_log off;
	#error_log off;
	access_log off;
#	error_log /dev/null;
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

   fastcgi_cache_path /opt/nginx/fastcgi_cache levels=1:2  keys_zone=TEST:10m  inactive=5m;
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
            index  index.html index.htm;
        }
	#cgi处理

    location ~ /bh.cgi
    {
		fastcgi_pass 127.0.0.1:8083;
		fastcgi_index cgi-bin/bh.cgi;
		include fastcgi.conf;
		include fastcgi_params;
    }
    
    location ~ /set.cgi
    {
		fastcgi_pass 127.0.0.1:8082;
		fastcgi_index cgi-bin/set.cgi;
		include fastcgi.conf;
		include fastcgi_params;
    }
    }
}

```