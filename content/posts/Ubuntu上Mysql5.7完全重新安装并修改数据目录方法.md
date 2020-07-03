+++
title= "Ubuntu上Mysql5.7完全重新安装并修改数据目录方法"
draft = false
date= "2016-09-07 21:04:00"
+++

最近感觉vps上系统盘的剩余空间不多了，想要把一些站点数据迁移到数据盘上，而且原来编译安装的mysql占用的冗余空间太多，想要改成直接apt安装的，结果出现了一些问题，想来还是应该先做单机主从然后切换的。

### 一.操作前先备份（重要）

### 二.完全卸载之前的mysql安装
```
apt remove --purge mysql*
apt autoremove
apt autoclean
rm -rf /etc/mysql /var/lib/mysql
```
如果数据需要保留的话就不删数据目录，这一步很重要的就是需要确认做完后服务器上还有没有mysql相关的任何文件，最好直接
`find / -name ''`找一下所有的`my.cnf`、`mysql`，包含配置文件的需要全部删除才行。

### 三.重新安装mysql

```
apt install mysql-server
```

### 四.修改数据目录，步骤如下：

原先参考的国内的一些资料都失败了，原因就是最关键的修改 apparmor 配置没做。

1.停止mysql服务（如果没有新数据写入也可以不停机）

2.复制mysql数据目录，注意使用参数 `-arp` 保留目录权限设置

3.修改mysql配置文件 `my.cnf`(ubuntu16.04 的 5.7 版本的路径为`/etc/mysql/mysql.conf.d/mysqld.cnf`)中的datadir

4.修改 `/etc/apparmor.d/usr.sbin.mysqld` 中的数据路径

5.重启 apparmor 服务

6.重启 msyql 服务

参考链接：

[http://stackoverflow.com/questions/1795176/how-to-change-mysql-data-directory](http://stackoverflow.com/questions/1795176/how-to-change-mysql-data-directory)