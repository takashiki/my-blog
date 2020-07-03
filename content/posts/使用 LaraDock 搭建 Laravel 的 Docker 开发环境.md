+++
title= "使用 LaraDock 搭建 Laravel 的 Docker 开发环境"
draft = false
date= "2018-02-03 16:24:00"
+++

参考链接：[基于 LaraDock 在 Docker 中快速构建 Laravel 应用系列教程 —— 搭建开发环境](http://laravelacademy.org/post/6569.html)

基本参考上文的步骤即可，不过有如下注意点：

- LaraDock 现在只支持原生 Docker， Docker Toolbox 这种基于虚拟机的方案需要使用比较老的版本
- 如果是在 Windows 上使用的话，LaraDock 的 .env 文件 中需要配置 `COMPOSE_PATH_SEPARATOR=;` 和`COMPOSE_FILE=docker-compose.yml;docker-compose.dev.yml`，因为这个分隔符在 Windows 中不支持使用 `:`
- 千万不要用 DaoCloud 的加速器，其他加速器貌似也不行，用了这个之后 `docker pull laradock/workspace` 一直失败，这个包会循环下载直到提示 `no space left on device`，一开始我以为是 Windows Docker 或者配置的问题，顺着这个方向去查解决方案，查了好久都没头绪，后来把加速器去掉果然好了
- 设置 proxy 时，格式为 `http://host:port`，如果 host 是在本机上的的话，需要写成 DockerNAT 那个网卡的 IP 地址，比如 `10.0.75.1`，另外这个 proxy 的配置也会被 docker 写入到容器中，具体见官网文档