+++
title= "每天自动push代码到coding.net赚码币"
draft = false
date= "2015-07-27 20:56:47"
+++

[coding.net](https://coding.net/register?key=b00cbbdb-b891-4727-b93a-edf112c136e9)可以用作代码托管和演示，也即相当于一个paas平台。它提供的项目演示服务分为免费版、开发版和高级版，其中开发版每月49元，而每天push代码到coding.net即可获得0.03个码币，一个码币相当于50元，每天push代码的话，开发就只要花几块钱就能买一个月了。

首先我们在[coding.net](https://coding.net/register?key=b00cbbdb-b891-4727-b93a-edf112c136e9)上创建一个专门用于自动push代码的项目，用readme.md初始化，其他随意。然后我们到自己的服务器或者vps上clone这个项目，注意一定要用SSH方式。

然后我们在项目根目录新增一个auto.sh文件，内容如下：

```shell
cd /home/wwwroot/default/log
echo -e "\n" >> README.md
date >> README.md
git add README.md
git commit -m "log datetime"
git push 
```

注意把文件中的项目路径改为自己的项目存放路径。

最后我们编辑crontab：

```shell
crontab -e
```

增加如下内容，即每天8点push代码，注意修改路径：
```shell
0 8 * * * /home/wwwroot/default/log/auto.sh
```

重启crontab
```shell
service cron restart
```

大功告成