+++
title= "使用fiddler抓包安卓模拟器网络请求"
draft = false
date= "2017-05-21 17:07:36"
+++

我用的是夜神模拟器，其他常见模拟器的抓包方式应该相同。

首先打开 fiddler，在 tools > fiddler options > connentions 选项卡中查看代理端口号（默认是 8888）以及是否勾选 Allow remote computers to connect （需勾选才行）。

然后回到模拟器，在模拟器的设置中选择 wlan，选择修改网络，将代理改为手动，ip 填写电脑的本地网络 ip，可以通过 ipconfig 命令查看，有可能会有几个内网 ip 地址，可以都试一下，端口为 fiddler 配置的端口号。

配置完成后安卓模拟器内访问网络应该就能看到请求了