+++
title= "免费SSL证书Let’s Encrypt安装使用记录"
draft = false
date= "2016-01-23 20:19:00"
+++

目前我包括博客在内的几个小站都在sae上，由于sae上的限制还是比较多的，所以有迁移到vps上的计划。

今天在vps上折腾了一下配置ssl证书，发现这方面很多前人已经提供了不少经验和工具，可以很方便地给自己的站点用上https。

首先申请Let’s Encrypt的证书我是用了[https://www.v2ex.com/t/241819](https://www.v2ex.com/t/241819)这个帖子里给出的一个shell脚本，全程只要修改下配置文件，就会全自动获取证书，也可以自动给证书续期，十分方便。

下载脚本：

```shell
wget https://raw.githubusercontent.com/xdtianyu/scripts/master/lets-encrypt/letsencrypt.conf
wget https://raw.githubusercontent.com/xdtianyu/scripts/master/lets-encrypt/letsencrypt.sh
chmod +x letsencrypt.sh
```

修改配置文件：
```shell
ACCOUNT_KEY="letsencrypt-account.key"
DOMAIN_KEY="example.com.key"
DOMAIN_DIR="/var/www/example.com"
DOMAINS="DNS:example.com,DNS:whatever.example.com"
```

里面的key脚本都会自动帮我们生成，只要配置正确即可。

```shell
./letsencrypt.sh letsencrypt.conf
```

执行上述命令即可完成整个证书签发过程，需要注意的有：

* 签发的域名必须已经解析，并且项目路径要填写对，在证书签发过程中，脚本会在项目根目录写一个文件，然后通过http方式来访问该文件，必须保证该文件能被正常下载才能通过验证。

* 服务器python版本必须大于等于2.7，2.6及以下会出现各种问题，不确定3.x是否可以。

获得证书后，如果是使用nginx作为服务器的话，只要在配置文件里加上类似如下的配置：
```
server {
    listen 443;
    ssl on;
    ssl_certificate  /usr/local/nginx/conf/server.crt;
    ssl_certificate_key  /usr/local/nginx/conf/server_nopwd.key;
}
```
然后重启nginx服务即可。
