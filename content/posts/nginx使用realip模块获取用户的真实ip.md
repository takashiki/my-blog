+++
title= "nginx使用realip模块获取用户的真实ip"
draft = false
date= "2016-06-11 20:13:56"
+++

我们经常会使用cdn来达到加快网站访问速度和隐藏服务器真实ip的目的，但是站点使用了cdn后程序获取到的用户ip以及nginx日志中记录的ip均会变成cdn的中转ip。不过cdn一般会实用自定义ip头来保存用户的真实ip，或者是将其放在X_FORWARDED_FOR头里，通过nginx的realip模块和这些ip头里的信息就可以获取到用户的真实ip了。

首先需要确认安装nginx的时候加上了realip模块：

```
    ./configure --with-http_realip_module
```

nginx配置示例：

```
    server {
    listen       80;
    server_name  www.test.com;
    index index.php index.html index.html;
    root /data/site/www.test.com;
    access_log  /data/wwwlogs/test.access.log  main;

    set_real_ip_from  192.168.50.0/24;
    set_real_ip_from  61.22.22.22;
    set_real_ip_from  121.207.33.33;
    set_real_ip_from  127.0.0.1;
    real_ip_header    X-Forwarded-For;
    real_ip_recursive on;
    fastcgi_pass  unix:/var/run/phpfpm.sock;
    fastcgi_index index.php;
    include fastcgi.conf;
}
```

我的一个小站使用了百度云加速，于是开了一个项目用来保存这种cdn的realip配置，参见：[https://github.com/takashiki/cdn-real-ip-list](https://github.com/takashiki/cdn-real-ip-list)。