+++
title= "通过docker安装gitlab"
draft = false
date= "2017-03-01 17:20:05"
+++

### 安装 docker engine

参见 [官方文档](https://docs.docker.com/engine/installation)

### 安装 docker compose

参见 [官方文档](https://docs.docker.com/compose/install/)

### 设置 docker 镜像

这里用的是 daocloud 提供的加速器：

```
curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://b62e767d.m.daocloud.io
```

### 使用 compose 启动 gitlab 容器

```
wget https://raw.githubusercontent.com/sameersbn/docker-gitlab/master/docker-compose.yml
docker-compose up
```

注意修改 docker-compose.yml 中的配置项。