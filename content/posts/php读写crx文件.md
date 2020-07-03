+++
title= "php读写crx文件"
draft = false
date= "2016-05-04 11:55:01"
+++

chrome浏览器的扩展文件crx文件是一种包含特殊文件头的zip文件，详细格式见[官方说明](https://developer.chrome.com/extensions/crx)。

用php打包crx文件在github上已经有一些轮子实现了，比如[https://github.com/vegat/PHPCrxGenerator](https://github.com/vegat/PHPCrxGenerator)和[https://github.com/andyps/crxbuild](https://github.com/andyps/crxbuild)。

用php读取crx的轮子在github上没找到，虽然也可以按照原理自己写一个，不过也搜出来一个国人的实现，详见[PHP 用zip函数操作crx文件和如何获取crx文件的唯一标识crx_id](http://blog.j135.com/?p=441)。