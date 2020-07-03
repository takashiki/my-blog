+++
title= "lnmp 环境下 502 问题原因及解决方案整理"
draft = false
date= "2017-05-23 15:54:00"
+++

参考资料：

- [nginx+php-fpm出现502 bad gateway错误解决方法](http://www.nginx.cn/102.html)
- [NGINX 502 Bad Gateway: PHP-FPM](https://www.datadoghq.com/blog/nginx-502-bad-gateway-errors-php-fpm/)

一般来说 502 可能的原因及解决方案如下：

#### php-fpm 未启动或不在运行

首先如果服务器上有多个版本的 php 的话，首先需要确认自己使用的是哪个版本。一般来说通过查看 nginx 配置文件中 fastcgi_pass 可以查看到监听对应 socket 或 端口的 fpm 是那个版本的。

然后 service php-fpm status 查看运行状态，注意对应版本的 fpm 的 service 名是不是 php-fpm 。

#### nginx 无法与 php-fpm 交互

这个一般是由于 nginx 配置文件中 fastcgi_pass 配置有问题造成的，查看 php-fpm 配置中 listen 项具体的值是否与 nginx 配置文件中的 fastcgi_pass 对应。

#### nginx 超时

nginx 超时一般与下面三个配置项有关：

```
fastcgi_connect_timeout 300;
fastcgi_send_timeout 300;
fastcgi_read_timeout 300;
```

在对应配置文件中修改这几个值即可。

#### php-fpm 超时

这个可以修改 php.ini 中的最大执行时间 max_execution_time 参数，或者在代码中使用 set_time_limit() 函数来改变时间限制。

还有就是 php-fpm.conf 中的 request_terminate_timeout 参数如果配置了的话也需要修改。

#### php 部分扩展存在问题

比如在 ubuntu 服务器上，imagick 经常会因为一些软件的更新引发 core dump，重启服务器后才会恢复正常，此时如果 `phpinfo()` 都会抛出 502 的话，很可能就是该原因导致的。