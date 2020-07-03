+++
title= "使用GoodSync实现文件双向实时同步"
draft = false
date= "2016-03-16 09:16:00"
+++

前情：[http://blog.skyx.in/archives/233/](http://blog.skyx.in/archives/233/)。

本来在windows上进行开发使用vagrant会是一种比较好的解决方案，但是vagrant只能在一台客户端机器上，如果有多台开发机并且经常切换，还是使用[Cloud9](https://c9.io/)这样的WebIDE或者vps比较方便。不过毕竟WebIDE没有phpStorm这样的IDE强大，所以我最后还是选择了使用vps。虽然phpStorm能自动将本地代码同步到服务器，但却不能将服务器上的文件变化同步回来，这就得借用第三方工具了。

上篇文章中我是使用rsync来实现这个需求的，不过后来发现了更加方便使用的[GoodSync](http://www.goodsync.com/)。Window上的安装就不说了，Linux上只需下载可执行文件即可使用，下载地址：[http://www.goodsync.com/for-linux](http://www.goodsync.com/for-linux)。

下载并解压后，我们将goodsync的几个可执行文件复制到`/usr/bin`中方便使用：

```shell
cp gs-server /usr/bin/gs-server
cp gscp /usr/bin/gscp
cp gsync /usr/bin/gsync
```

然后我们执行增加用户的命令，注意替换其中的用户名密码，之后直接执行gs-server就可以启动了：

```shell
gs-server /set-admin="gs-userid:gs-password:system-userid"
gs-server
```

然后使用 supervisor 设置开机启动，编辑`/etc/supervisor/conf.d/goodsync.conf`内容如下：

```shell
[program:gs-server]
command=/usr/bin/gs-server
autostart=true
autorestart=true
user=root
environment=HOME='/root'
```

重启supervisor并查看任务运行状态：

```shell
service supervisor restart
supervisorctl status
```

之后Windows客户端上的设置参考这篇教程即可，[http://jingyan.baidu.com/article/a3761b2bbbef2f1577f9aa43.html](http://jingyan.baidu.com/article/a3761b2bbbef2f1577f9aa43.html)。




