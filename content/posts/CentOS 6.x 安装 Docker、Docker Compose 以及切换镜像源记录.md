+++
title= "CentOS 6.x 安装 Docker、Docker Compose 以及切换镜像源记录"
draft = false
date= "2018-02-28 18:56:00"
+++

**首先，这是个大坑，不到万不得已千万不要轻易尝试！！！**

由于工作需要，我不得不在 CentOS 6.x 上安装 Docker，而且由于需要一次性部署多个关联服务，不用 docker-compose 的话又会相当麻烦，于是便开始了这段折腾之路。

我这里总结一下主要步骤和注意事项，详细步骤包括具体命令请参见文末的参考链接。

- 首先 CentOS 6.x 用的报管理器是 yum，yum 只支持 python 2.6 及以下的版本，而 docker compose 只支持 python 2.7 及以上的版本，所以要编译安装 python 2.7，然后把 yum 的几个脚本里的 python 路径改成 2.6 版本的路径，默认的 python 改成 2.7 版本
- 然后根据参考链接里的步骤通过 epel 安装 1.7.1 版本的 docker，这个版本的 docker 是支持 CentOS 6.x 的最后一个版本了。貌似没有非常靠谱的方案在 CentOS 6.x 的机器上安装更高版本的 docker 了，因为新版本 docker 需要 3.x 的内核，以及其他很多高版本的依赖包，可能会出现问题，不过网上有成功升级内核至 3.10 并且升级 Docker 至 1.9.1 版本的记录，具体可查看文末参考链接
- 之后通过 pip 安装 docker-compose，需要注意支持 docker 1.7.1 的最后一个版本的 docker-compose 是 1.5.2 版本，所以安装的时候要指定安装这个版本
- 1.5.2 版本的 docker-compose 只能支持 version 1 的 docker-compose.yml 配置文件，使用新版本的配置文件时需要自己手工改成 v1 的格式
- daocloud 的镜像加速器亲测不支持 1.7 版本的 docker，中科大的镜像貌似也有点问题，阿里云的镜像可以完美支持，需要注意 1.7 版本的 docker 修改 registry 需要修改 `/etc/sysconfig/docker` 中的启动参数，详见参考链接

参考链接：

[CentOS6.x 安装 Docker 和 Docker Compose](http://blog.csdn.net/kinginblue/article/details/73527832)
[centos 6.5 & docker1.7.1 & docker的阿里云代理镜像设置](http://blog.csdn.net/MR_REN019235/article/details/78416802)
[CentOs 6.x升级内核到3.10, 安装并升级docker1.9.1](http://blog.csdn.net/renhanchi/article/details/76050421)