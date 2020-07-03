+++
title= "使用Navicat的SSH tunnel连接数据库时失败的可能原因"
draft = false
date= "2016-06-20 20:37:00"
+++

有可能ssh的配置文件 `\etc\ssh\sshd_config` 中禁用了tcp端口转发，

```shell
AllowTcpForwarding yes
```

如果上述参数为 no ，则修改为 yes 后重启 ssh 服务即可。

参考链接： [https://rzemieniecki.wordpress.com/2012/08/14/navicat-mysql-connection-error/](https://rzemieniecki.wordpress.com/2012/08/14/navicat-mysql-connection-error/)