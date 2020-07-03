+++
title= "部署系统 Walle 在使用中遇到的一些问题吐槽"
draft = false
date= "2016-07-27 09:06:00"
+++

最近公司在用 walle ，感觉很不理解为什么一个用 yii2 开发的部署系统对 yii2 这么不友好，每次新项目上线都得配好久，新手得两天左右，总结下来坑如下：

1.各种文件需要新版发布时保持原样，就得 cp 来 cp 去，尤其使用 yii2-advanced 的人应该深有体会

2.由于使用了软链，所以开了 opcache 的话新版上线需要 reload php-fpm ，或者其他方式重置 opcache ，原因是 opcache 解析的文件路径是 realpath

3.如果使用了 git subtree 之类的需要自己在 composer 里添加 autoload 规则的东西，每次新版上线必须 composer dump-autoload ，具体原理不明

……好像还有其他的来着

关于PHP代码发布有一篇不错的文章： [http://huoding.com/2016/05/27/515](http://huoding.com/2016/05/27/515)，十分推荐。