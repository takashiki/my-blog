+++
title= "开源一个简单的短网址程序Ourls"
draft = false
date= "2015-09-20 17:07:00"
+++

一直想要自己搭一个短网址服务，奈何github上找过几圈，都没有找到十分符合心意的，于是就趁周末自己写了一个。

Ourls的灵感来源于知乎上关于短址生成算法的一个问题下的讨论，[http://www.zhihu.com/question/29270034](http://www.zhihu.com/question/29270034)，详细的关于短址生成的各种设计原理的利弊可见该问题下的几个回答。综合考虑后，我决定采用如下方案：使用sha1来判断url在数据库中是否已存在，若不存在则给该url发一个号（即数据库中的自增id），然后使用hashids对该id进行hash，最终得出该连接的短址。

该项目需要PHP版本5.4以上，在5.5.24下测试通过。项目所使用后端框架为flight，前端使用了amazeui。

sae上的rewrite规则如下

```
- rewrite: if ( in_header["host"] == "yoursiteurl" && path ~ "^(?!public/)(.*)" ) goto "public/$1"
- rewrite: if ( ! is_dir() && ! is_file() ) goto "public/index.php?%{QUERY_STRING}"
```

在线演示地址：[http://skyx.in/](http://skyx.in/)。

github地址：[https://github.com/takashiki/Ourls](https://github.com/takashiki/Ourls)。

osc地址：[http://git.oschina.net/takashiki/Ourls](http://git.oschina.net/takashiki/Ourls)。