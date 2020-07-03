+++
title= "ssl站点启用Certificate Transparency功能记录"
draft = false
date= "2016-01-24 18:03:14"
+++

主要流程参考[http://blog.eqoe.cn/posts/enable-certificate-transparency-for-nginx.html](http://blog.eqoe.cn/posts/enable-certificate-transparency-for-nginx.html)。

需要注意的是如果之前安装了nginx但没有添加nginx-ct模块的需要重新编译安装nginx，另外配置项中`ssl ct on`应为`ssl_ct on`。