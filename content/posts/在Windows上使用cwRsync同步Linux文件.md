+++
title= "在Windows上使用cwRsync同步Linux文件"
draft = false
date= "2016-03-15 16:12:43"
+++

现在我平时日常使用的电脑操作系统为Windows，但Windows用于开发会有很多的坑，于是便搞了一个vps在上面进行开发，然而phpStorm的Deployment只能支持自动同步本地文件至远程服务器，而服务器上文件有改动时却无法自动同步至本地，这在经常需要在服务器上进行composer和npm操作的情况下十分不便。

我最初想要解决这个问题的方法是找phpStorm有没有这方面的插件，然而并没有找到。后来又想将vps上的目录通过Samba或者类似NetDrive这种软件挂载成一个驱动器，这样就能直接用phpStorm打开远程的项目了，然而卡到飞起，已然不是能够使用的状态了，遂打消了这方面的念头，决定使用rsync来实现。

cwRsync免费版下载地址：[https://www.itefix.net/content/cwrsync-free-edition](https://www.itefix.net/content/cwrsync-free-edition)，免费版的cwRsync已经能满足需求，下载下来的是压缩包，直接解压就可以使用了。

服务器端安装可以直接使用包管理器安装，就不多说了。安装好后编辑`/etc/rsyncd.conf`，内容如下：

```shell
#全局配置
uid = root #用户名，也即为执行rsync操作的用户，若该用户没有足够的权限操作需备份的文件夹则备份时会报错
gid = root #用户组名
use chroot = no
read only = yes

#访问权限控制
#hosts allow=172.16.0.0/255.255.0.0 192.168.1.0/255.255.255.0 10.0.1.0/255.255.255.0
#hosts deny=*                                

max connections = 5
pid file = /var/run/rsyncd.pid
secrets file = /etc/rsyncd/rsyncd.secrets
#lock file = /var/run/rsync.lock           
#motd file = /etc/rsyncd/rsyncd.motd        

#log file = /var/log/rsync.log               
#This will log every file transferred - up to 85,000+ per user, per sync
transfer logging = yes
log format = %t %a %m %f %b
syslog facility = local3

timeout = 300

#模块配置
[webapp]
path = /data/wwwroot/ #服务器上需要同步的路径，如不存在的话同步时会报错
list=yes
ignore errors
auth users = rsync #配置在rsyncd.secrets中的用户名
```

然后新建`/etc/rsyncd/rsyncd.secrets`文件，内容即为`用户名：密码`对，一行一个：

```shell
rsync:rsync
```

文件都配置好后使用如下命令启动rsync服务端：

```shell
rsync --daemon --config /etc/rsyncd.conf
```

rsync默认使用端口为873，需要在防火墙里开放873端口的tcp链接。

这样服务器端就配置好了，在Windows客户端中进入cwRsync的bin目录，创建`rsyncd.secrets`文件，内容即为刚才服务端`/etc/rsyncd/rsyncd.secrets`文件中的密码部分（不需要用户名），然后执行以下命令即可开始同步：

```shell
rsync -vzrtopg --progress --delete -
-password-file=rsyncd.secrets rsync@118.193.255.211::webapp local_sync_dir
```