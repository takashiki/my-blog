+++
title= "Navicat通过http tunnel管理coding.net等paas平台数据库方法"
draft = false
date= "2015-08-12 10:43:00"
+++

像[coding](https://coding.net)和[好雨云](http://goodrain.com/)之类的paas平台，并没有像sae等平台一样原生提供phpmyadmin之类的数据库管理工具的支持，自己专门开一个应用来部署phpmyadmin一来比较麻烦，二来占用多余的资源，于是这两天研究了一下如何方便的管理这些平台上的数据库。

经过网友提示，我发现可以使用navicat通过http通道来进行管理，具体操作也很简单：

1.首先到navicat的安装目录下找到ntunnel_mysql.php文件

2.将上述文件传到需要管理数据库的项目里，并且进行部署

3.配置navicat链接，http通道填写你自己的项目内该文件的地址，该文件可以自己重命名，连接信息可以在平台的mysql服务连接信息里找到。

![http通道](https://ooo.0o0.ooo/2015/08/12/55cab1f4c5638.png "http通道")
![连接信息](https://ooo.0o0.ooo/2015/08/12/55cab1f4ee263.png "连接信息")

配置完成后点击连接测试，不出意外的话就成功了。