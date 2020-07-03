+++
title= "git submodule 使用初试"
draft = false
date= "2016-04-22 10:39:08"
+++

在团队项目开发中，经常会把一些公用的模块抽取出来作为单独的项目。对于php来说，引用这些项目的方式除了手动复制之外主要有两种，一种是composer，一种是git submodule，这两种方式在自己使用下来的话，我觉得个人项目更推荐于使用composer，但是对于公司项目，在一些场景下使用submodule则可能更方便一些。

不过git submodule在使用中遇到了一些坑，详见这篇文章：[http://mobile.51cto.com/aprogram-393324.htm](http://mobile.51cto.com/aprogram-393324.htm)。