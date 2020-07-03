+++
title= "常见PHP框架简单性能测试"
draft = false
date= "2016-05-26 21:19:00"
+++

本测试使用 `apache bench`，参数均为 `-c 100 -n 2000`。

测试环境：

- 单核 i7-4700MQ
- 2G 内存
- 7200 转机械硬盘

软件版本：

- nginx 1.9
- PHP 7

### 纯PHP文件

这是一个只包含 `echo 'hello world'` 的纯PHP文件的测试结果：

![php](https://ooo.0o0.ooo/2016/05/26/5746fe473d7d1.jpg)

### Yii2

![Yii2](https://ooo.0o0.ooo/2016/05/26/5746fe596ebae.jpg)

### Laravel

![Laravel](https://ooo.0o0.ooo/2016/05/26/5746fe49d74d6.jpg)

### Slim3

![Slim3](https://ooo.0o0.ooo/2016/05/26/5746fe5439fb6.jpg)

### Flight

![Flight](https://ooo.0o0.ooo/2016/05/26/5746fe7a22930.jpg)

### Lumen

![Lumen](https://ooo.0o0.ooo/2016/05/28/57498fa4c8f58.jpg)
