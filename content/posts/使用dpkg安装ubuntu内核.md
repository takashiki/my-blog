+++
title= "使用dpkg安装ubuntu内核"
draft = false
date= "2016-03-02 10:08:43"
+++

以64位ubuntu15.10、4.4版本内核为例，ubuntu官方构建的内核安装包地址为[http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.4-wily/](http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.4-wily/)。

需下载的文件有三个，分别为对应的headers、image和headers-all。

然后执行以下命令进行安装：

```shell
dpkg -i \
linux-headers-4.4.3-040403_4.4.3-040403.201602251634_all.deb \
linux-headers-4.4.3-040403-generic_4.4.3-040403.201602251634_amd64.deb \
linux-image-4.4.3-040403-generic_4.4.3-040403.201602251634_amd64.deb
```
