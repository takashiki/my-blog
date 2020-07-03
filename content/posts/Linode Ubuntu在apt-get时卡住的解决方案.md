+++
title= "Linode Ubuntu在apt-get时卡住的解决方案"
draft = false
date= "2016-03-18 16:00:00"
+++

在使用linode时用apt-get经常会出现卡住的问题，看起来像是因为linode默认使用了ipv6的问题，于是使用以下命令试了一下ipv4会不会卡住：

```shell
apt-get -o Acquire::ForceIPv4=true update
```

试过后发现果然不会出现卡住的问题了，于是编辑`/etc/apt/apt.conf.d/99force-ipv4`文件，内容如下：

```shell
Acquire::ForceIPv4 "true";
```

这样apt-get就会强制使用ipv4了。

参考链接： [https://www.vultr.com/docs/force-apt-get-to-ipv4-or-ipv6-on-ubuntu-or-debian](https://www.vultr.com/docs/force-apt-get-to-ipv4-or-ipv6-on-ubuntu-or-debian)