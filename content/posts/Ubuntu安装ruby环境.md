+++
title= "Ubuntu安装ruby环境"
draft = false
date= "2015-08-05 18:39:57"
+++

首先安装gpg2，否则可能会报错：

```shell
apt-get install gnupg2

gpg2 --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3
```

安装rvm，科学上网会比较快，或者换淘宝源：

```shell
curl -L https://get.rvm.io | bash -s stable
```

exit后重新登录rvm会生效。

用rvm安装ruby并设置版本：

```shell
rvm install 2.0.0

rvm 2.0.0 --default
```