+++
title= "nginx日志分片及使用goaccess进行日志分析"
draft = false
date= "2016-05-13 11:14:15"
+++

## nginx日志分片

日志分片脚本详见：[https://github.com/takashiki/tool-scripts/blob/master/nginx_log_slice.sh](https://github.com/takashiki/tool-scripts/blob/master/nginx_log_slice.sh)

配置好其中的日志路径、nginx pid路径、备份目录即可，可以设置crontab每天凌晨跑一次。

## goaccess

这是goaccess的[官网链接](https://www.goaccess.io/)。

### 安装

官网给出了具体的安装方法，包括编译安装和包管理器安装，[https://goaccess.io/download](https://goaccess.io/download)。

### 使用

直接打开：

```shell
goaccess -f access.log
```

空格选择日志格式，一般为`NCSA Combined Log Format`，回车开始分析。

导出HTML或其他格式的报告能够获得更加详细的分析数据，在导出之前需要先添加配置文件`~/.goaccessrc`，内容如下：

```shell
time-format %T
date-format %d/%b/%Y
log-format %h %^[%d:%t %^] "%r" %s %b "%R" "%u"
```

执行以下命令开始导出：

```shell
goaccess -f access.log -p ~/.goaccessrc -a > report.html

```