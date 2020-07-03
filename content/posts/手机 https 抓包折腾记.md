+++
title= "手机 https 抓包折腾记"
draft = false
date= "2018-08-02 17:27:31"
+++

目前常用的抓包软件一般是 Fiddler 和 Charles，个人感觉 Charles 的用户体验比 Fiddler 好不少，不过 Charles 是收费的。

这两个软件抓 https 的教程网上有很多，可以参考如下几篇：
- [fiddler抓包HTTPS请求](https://www.jianshu.com/p/0244146090c7)
- [Charles 4.2.1 HTTPS抓包](https://juejin.im/post/5a30a52a6fb9a0451d4175ed)
- [Mac下用Charles實現Android http和https抓包](https://com-it.tech/archives/6960)

简而言之，一般这个过程主要就是两步：

- 开启 https 抓包配置，fiddler 是一个勾选框，charles 则是自己配需要抓的域名，可以通配
- 在需要抓包的客户端安装证书并添加信任

其中不同客户端的操作又分别如下：

- PC 上需要把证书安装到 “受信任的根证书颁发机构”，默认一般是安装在个人或者其他几个选项卡里的，需要自己手工导出然后导入
- iOS 上安装完证书后要在设置里添加信任，可以参考上面的教程
- Android 低版本只要安装好证书就行

一般来说是这样的，但是安卓就特别坑，坑就坑在安卓太碎片化了，每家对于安装证书的处理都不太一样，据我所知 oppo 安装证书就比较麻烦，具体的可以自己搜索教程。
另外 Android N 开始用户安装的证书是没犯法被应用信任的，除非应用自身配置了安全策略，详见 charles 官网文档：[https://www.charlesproxy.com/documentation/using-charles/ssl-certificates/](https://www.charlesproxy.com/documentation/using-charles/ssl-certificates/) 中 Android 部分。