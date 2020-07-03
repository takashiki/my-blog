+++
title= "Yii2 使用jsonp格式response时遇到的一个坑"
draft = false
date= "2017-02-20 09:18:00"
+++

最近的一个项目在实现前后端分离时，由于调用域名与接口域名可能不相同，所以使用了`jsonp`格式进行返回，但是在开发环境上开了`debug`的情况下遇到500错误时竟然没有任何错误显示，也即`response body`是空的，这让我很困扰。

通过查看 `Yii` 写的文件日志发现，这是 `Yii` 在默认的 `ErrorHandler` 中没有对 `jsonp` 格式返回进行特殊处理造成的，于是便在 `github` 上提了一个 [issue](https://github.com/yiisoft/yii2/issues/13563)。从回复来看，一年前就有人修改了`jsonp`的`formatter`的实现，不过由于会破坏兼容性，所以一直没正式接收。话说原本的`jsonp`实现方式实在是太坑了，和其他几种`Formatter`的实现不一致，使用起来很不方便，希望`Yii`官方早点改掉吧。