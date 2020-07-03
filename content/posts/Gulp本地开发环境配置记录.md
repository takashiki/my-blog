+++
title= "Gulp本地开发环境配置记录"
draft = false
date= "2016-09-27 17:16:02"
+++

首先安装 node 和 npm，这个之前写文章记录过：[https://blog.skyx.in/archives/206/](https://blog.skyx.in/archives/206/)。

然后在项目下编写 package.js ，执行 `npm install` 安装依赖包。

安装 `browser-sync` :

```shell
npm install browser-sync --save-dev
```

本地 `gulp` 命令行版本最好是 `4.0` 的，否则有些项目会报错。

如果是在没有图形界面的机器上，有可能会报 

```shell
gulp-notify: [Error in notifier] Error in plugin 'gulp-notify'
not found: notify-send
```

此时安装 `libnotify-bin` 即可：

```shell
apt-get install libnotify-bin
```

