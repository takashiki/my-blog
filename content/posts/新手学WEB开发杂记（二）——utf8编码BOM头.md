+++
title= "新手学WEB开发杂记（二）——utf8编码BOM头"
draft = false
date= "2013-04-09 22:28:32"
+++

在刚刚开始学PHP时，遇到过这样一个问题，在本地运行得好好的一段代码在SAE上则获取cookie失败，这让我百思不得其解。搞了很长时间之后也找不到到底是哪出了问题，于是我将cookie换成了session试了一下，结果本地运行也出了问题，报了这个错误：

Cannot modify header information - headers already sent by......

这是十分常见的错误，原因是session_start（）前已经有了输出，但我仔细检查代码后也没发现有什么输出。在网上查了一些资料后，终于发现一个可能的原因，那就是BOM头的问题。

BOM头是在utf-8编码文件中BOM在文件头部，占用三个字节，用来标示该文件属于utf-8编码。这三个字节便是session_start()前的输出。将文件格式改成无BOM头的utf-8后，问题果然解决了，SAE上也运行成功。

至于为什么在本地环境setcookie可以成功我则一直想不通，略奇怪啊。

 