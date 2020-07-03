+++
title= "配置ssh免密码登录linux机器"
draft = false
date= "2015-07-12 20:23:00"
+++

首先本地机器如果是window的话，需要安装git或者其他工具以获取ssh工具。然后使用以下命令生成密钥对：

```shell
ssh-keygen -t rsa -C comment
```

然后进入密钥存放目录使用如下命令上传公钥置服务器端：

```shell
scp id_rsa.pub root@hostname:~/id_rsa.pub
```

公钥上传成功后进入服务器使用命令追加授权key：

```shell
cat ~/id_rsa.pub >> ~/.ssh/authorized_keys
```

修改授权文件权限：

```shell
chmod 600 ~/.ssh/authorized_keys
```

此时就可以免密码登录服务器了。