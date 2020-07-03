+++
title= "VMWare11安装Mac OS 10.10(Yosemite)过程记录"
draft = false
date= "2015-09-05 20:51:00"
+++

最近想玩玩苹果的系统，不过没有mac的机器，只能在我船上安虚拟机玩玩了，下面记录一下vmware11安装yosemite的过程。

vmware的安装就不多说了，要在vmware上装mac的操作系统，需要打一下vmware unblocker补丁。vmware11系列需要用vmware unblocker 2.x的版本，而vmware10及以下版本则要使用vmware unblocker 1.x的版本，这里分享一下我所使用的2.06版：[http://pan.baidu.com/s/1sj20CFF](http://pan.baidu.com/s/1sj20CFF) 密码: s6dh。

windows上使用管理员身份运行win-install.cmd即可，运行前最好在任务管理器里把所有vmware相关的服务和进程都关掉，否则有可能破解失败。如果运行后出现“unblocker.exe 已停止运行”的提示则是破解失败，这一般是因为有vmware的进程或服务没有停止，停止后手工运行unblocker.exe或unblocker.py则能完成破解。成功打完补丁后应该就能在新建虚拟机时选择客户机操作系统为 Apple Mac Os X 了。

接下来下载Yosemite的镜像，这个网上有很多，最好选择一个完整包，免得遇到些其他问题，或者找一些懒人版本也不错，需要注意的是dmg文件无法直接使用，得找个cdr版本的。这是我用的完整包：[http://pan.baidu.com/s/1sj4ri5R](http://pan.baidu.com/s/1sj4ri5R) 密码: y86w。

安装时如果遇到以下问题，只要找到并打开安装目录下的 XXXX.vmx 文件，使用文本编辑器打开后，在 smc.present = "TRUE" 后添加“smc.version = 0”后即可解决。

接下来就可以开启虚拟机安装了，安装时注意在选择安装位置时要进入磁盘工具，然后选择创建的硬盘，进行抹掉操作，这样该硬盘才能被系统识别。