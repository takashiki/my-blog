+++
title= "Conoha VPS Ubuntu安装锐速"
draft = false
date= "2015-07-19 21:17:00"
+++

> **小尾巴** 通过[该链接](https://www.conoha.jp/referral/?token=mrBOqqw4yzeJSyoPloAjAim8mQQPBp6XY5E8lx4ir2hW.K81KX4-49S)注册conoha后充值500日元以上可获得1000日元优惠券。

对于一般站长来说还是习惯使用ubuntu系统，但是我在conoha vps ubuntu系统上安装锐速时，发现锐速暂不支持conoha自带的ubuntu14.04镜像的内核版本，于是查询了[锐速支持的列表](http://my.serverspeeder.com/ls.do?m=availables)后，决定安装受支持的版本内核。

```shell
apt-cache search linux-image (搜索可下载内核)
apt-get install linux-image-3.13.0-46-generic (安装指定内核)
apt-get remove linux-image-3.16.0-43-generic (卸载其他版本内核)
```

执行完成以上步骤之后就可以正常安装锐速了。