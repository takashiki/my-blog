+++
title= "自动备份coding.net数据库至vps"
draft = false
date= "2015-08-10 20:24:19"
+++

coding.net上貌似本身没有自动备份数据库的功能，于是就想自己写一个来每天自动备份数据库到vps上。以下为具体代码：

```php
<?php
$url = 'xxx';
$referer = 'xxx';
$filename = 'xxx.sql';
$cookie = 'xxx';
$userAgent = 'xxx';

$fp = fopen($filename, 'w');
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_TIMEOUT, 50);
curl_setopt($ch, CURLOPT_REFERER, $referer);
curl_setopt($ch, CURLOPT_USERAGENT, $userAgent);
curl_setopt($ch, CURLOPT_COOKIE, $cookie);
curl_setopt($ch, CURLOPT_FILE, $fp);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_exec($ch);
curl_close($ch);
fclose($fp);

```

其中url为点击服务管理中的msyql控制台里的备份数据按钮跳转到的链接，referer为控制台链接，filename可自定义，cookie和ua使用chrome浏览器的调试窗口就能获取到，具体就不多说了。

在vps上设置一个crontab定时跑这个脚本就可以自动备份coding上的数据库了。