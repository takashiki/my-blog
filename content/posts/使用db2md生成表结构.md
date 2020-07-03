+++
title= "使用db2md生成表结构"
draft = false
date= "2016-05-19 17:40:19"
+++

[https://github.com/index0h/node-db2md](https://github.com/index0h/node-db2md)

这个简直是神器，写数据库文档再也不用头疼了。

首先要安装`node`和`npm`，这就不多说了。然后使用`npm`安装`db2md`：

```shell
npm install db2md -g
```

安装完成后创建配置文件[db2md.json](https://github.com/index0h/node-db2md/blob/master/examples/minimalConfiguration.json)，示例如下：

```json
{
    "user": "root",
    "pass": "123456",
    "database": "test",
    "tables": ".*"
}
```

配置完成后即可以开始导出：

```shell
db2md -o tables.md
```
