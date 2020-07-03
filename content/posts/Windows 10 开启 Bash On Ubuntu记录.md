+++
title= "Windows 10 开启 Bash On Ubuntu记录"
draft = false
date= "2018-02-04 21:19:00"
+++

**2018.02.04 更新**：

这周折腾了半天准备用 WSL (Windows Subsystem for Linux) 搭个开发环境，结果发现这个玩意儿虽然出来一段时间了，但是坑还是真的多。

首先是没有支持 `TCP_INFO socket option`，参考 [php-fpm启动提示Protocol not available (92)该怎么解决呢？](https://www.zhihu.com/question/62495462)，这导致了 php-fpm 监听端口时，日志里会一直打印错误，但是能用，很神奇，而如果 listen 的是 socket 的话，则功能不正常，一直超时。

我发现的还有，如果 mysql 的 data 目录不是放在 WSL 自身硬盘路径内，而是放到 D 盘或者其他外部目录的话，虽然能新建数据库，但是建表有问题。

其他比如不支持升级发行版之类的必然的问题就不多说了，还有就是新版的 Win10 WSL 的安装路径是 `C:\Users\<username>\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState`。

所以从亲身的惨痛经历来看，建议还是不要妄想在 Windows 上用虚拟化以外的方案搭建开发环境。

===

步骤记录如下：

1.设置 -> 更新和安全 -> 针对开发人员，选择开启开发人员模式，这一步可能需要重启。

2.控制面板 -> 程序 -> 启用或关闭windows功能，选中 “适用于 Linux 的 Windows 子系统（Beta）”，然后重启。

3.打开 cmd 或者 PowerShell，点击左上角进入设置，在 ‘选项’ 面板中将 “使用旧版控制台” 取消选中，然后重启命令行。

4.在命令行中键入 ‘bash’，然后系统就会让你下载系统文件，选择 ‘y’ 之后就等待下载安装完成吧。

几个注意点：

1.不翻墙的话下载速度很慢，反正电信不翻墙是几乎下载不了的。
2.这个子系统的根目录默认在 `%userprofile%\AppData\Local\Lxss\rootfs`，这个略坑。

使用`xshell`或`putty`等ssh终端连接本地`bash`方式：

1.卸载并重新安装 openssh-server:

```shell
sudo apt-get remove --purge openssh-server
sudo apt-get install openssh-server
```

2.在`/etc/ssh/sshd_config`中添加或将原有的配置项的值修改为如下：

```
ListenAddress 0.0.0.0
UsePrivilegeSeparation no
PasswordAuthentication yes
```

3.运行`service ssh --full-restart`即可