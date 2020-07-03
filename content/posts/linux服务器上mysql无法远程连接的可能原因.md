+++
title= "linux服务器上mysql无法远程连接的可能原因"
draft = false
date= "2015-07-03 14:51:00"
+++

如果telnet远程linux服务器的3306端口是通的话，那说明没有授予用户远程登录权限，那么就在远程服务器上登入mysql后使用如下语句授权：

```sql
grant all privileges on *.* to root@"%" identified by "password" with grant option;

flush privileges;
```

第一行命令解释如下，*.*：第一个*代表数据库名；第二个*代表表名。root：授予用户账号。“%”：表示授权的用户IP，%代表任意的IP地址都能访问。“password”：分配账号对应的密码。第二行命令是刷新权限信息，也即是让我们所作的设置马上生效。

如果telnet不通，我们先用netstat查看3306端口是否已监听所有ip地址的请求：

    netstat -an | grep 3306

如果输出为

    tcp        0      0 127.0.0.1:3306            0.0.0.0:*               LISTEN
    
则说明只监听了本地连接。解决方法：修改/etc/mysql/my.cnf文件。打开文件，找到下面内容：

```
# Instead of skip-networking the default is now to listen only on
# localhost which is more compatible and is not less secure.
bind-address  = 127.0.0.1
```

把上面`bind-address = 127.0.0.1`这一行注释掉或者把127.0.0.1换成合适的IP。
重新启动mysql再用netstat检测是否为：

    tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN

如果这样之后还是telnet不通，那基本就是防火墙的问题了，查看iptables的rules文件里是否包含

    -A INPUT -p tcp -m tcp --dport 3306 -j ACCEPT
    
如果没有该规则的话加入该规则后重启iptables就可以了。