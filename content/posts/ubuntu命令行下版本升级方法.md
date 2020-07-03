+++
title= "ubuntu命令行下版本升级方法"
draft = false
date= "2016-02-28 19:39:03"
+++

ubuntu在命令行下的版本升级，官方比较推荐的方式是使用`do-release-upgrade`，也即按顺序执行以下命令即可：

```shell
apt-get update
apt-get upgrade
apt-get install update-manager-core
do-release-upgrade
```

如果这种方式遇到如下报错：

```shell
Error authenticating some packages

It was not possible to authenticate some packages. This may be a transient network problem. You may want to try again later. See below for a list of unauthenticated packages
```

网上有一种解决办法是创建`/etc/update-manager/release-upgrades.d/unauth.cfg`文件，内容如下：

```shell
[Distro]
AllowUnauthenticated=yes
```

然后再执行`do-release-upgrade`。

不过我使用该方法后仍然失败，最后只好采用debian的升级方法来进行升级，步骤如下：

修改`/etc/apt/source.list`文件，修改其中的版本号，比如`14.04`修改到`15.10`即将`trusty`替换为`wily`，若使用vim可以批量替换`:%s/trusty/wily/g`。

然后依次执行以下命令即可：

```shell
apt-get update
apt-get upgrade
apt-get dist-upgrade
```

查看ubuntu版本命令如下:`lsb_release -a`。