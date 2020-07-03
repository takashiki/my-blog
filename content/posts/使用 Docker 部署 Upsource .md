+++
title= "使用 Docker 部署 Upsource "
draft = false
date= "2017-12-28 16:03:00"
+++

Upsource 是 Jetbrains 推出的一款用于 Code Review 的基于 Web 的系统，功能十分强大，最重要的是和 IDE 全家桶无缝集成，可以直接在 IDE 里进行 Code Review。

在选择 Upsource 之前我也调研了 Gerrit 和 Phabricator，觉得不太适合当前的团队。这两个工具更适用于强制 Code Review 并且把其作为 CI 的一环的团队使用，这自然是有好处，不过稍微有些繁琐。这两者的具体区别可以参考 [https://stackoverflow.com/questions/10545480/gerrit-phabricator-review](https://stackoverflow.com/questions/10545480/gerrit-phabricator-review)。

### 使用 Docker 部署

使用 Docker 部署 Upsource 可以参考官方的文档 [https://www.jetbrains.com/upsource/download/#section=docker](https://www.jetbrains.com/upsource/download/#section=docker)。

有几个注意点：

- docker pull 的时候必须指定镜像版本号（也就是 <version>.<build>，见[https://hub.docker.com/r/jetbrains/upsource/tags/](https://hub.docker.com/r/jetbrains/upsource/tags/)），不然找不到
- 在跑容器之前，记得把映射的那几个目录按照教程上 chown 一下
- 配置 base url 时可以先按照能检测通过的配，后面可以通过修改 `conf/internal/bundle.properties` 来修改
- 如果提示某个目录不为空，无法下一步的话，可以进目录看看有没有隐藏文件，如果有就全删了

不出意外的话应该就能正常跑起来了。

### 使用 nginx 配置反代

由于 Upsource 使用了 websocket，所以常规的反代配置可能有问题，直接参考官方文档就 ok 了，见 [https://www.jetbrains.com/help/upsource/proxy-configuration.html#NginxConfiguration](https://www.jetbrains.com/help/upsource/proxy-configuration.html#NginxConfiguration)。

```nginx
server {
         listen  2222;
         server_name  localhost;
         location  / {
            proxy_set_header X-Forwarded-Host $http_host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_http_version 1.1;

            # to proxy WebSockets in nginx
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            
            proxy_pass http://upsourcemachine.domain.local:1111;
            proxy_pass_header Sec-Websocket-Extensions;
         }
      }
```

### 与 IDE 的整合

安装 Upsource Integration 插件即可，首先 Upsource 上先连接号该项目的 Git，然后本地打开的项目右下角点击 Upsource 图标就可以进行关联。

参考链接

[http://blog.csdn.net/nikobelic8/article/details/54897314](http://blog.csdn.net/nikobelic8/article/details/54897314)

