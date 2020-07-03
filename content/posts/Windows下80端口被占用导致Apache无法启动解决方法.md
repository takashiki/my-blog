+++
title= "Windows下80端口被占用导致Apache无法启动解决方法"
draft = false
date= "2015-08-26 15:13:00"
+++

本来公司开发机用的是Win7，自家用的机器升级Win10一段时间了，感觉还不错，就把公司开发机也升级到了Win10，后来用到本地的Apache服务时发现启动不了了，`netstat -ano | grep 80`之后发现80端口被pid为4的系统进程占用了，就查了一下解决方法。

使用管理员身份运行cmd执行以下命令即可：

```shell
net stop http

sc config http start=disabled
```