+++
title= "ubuntu防火墙iptables操作学习"
draft = false
date= "2016-03-15 20:50:02"
+++

官方文档地址[https://help.ubuntu.com/community/IptablesHowTo](https://help.ubuntu.com/community/IptablesHowTo)

ubuntu 15.10 修改配置文件后使之生效：

```shell
iptables-apply /etc/iptables.up.rules
```