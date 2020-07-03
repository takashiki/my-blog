+++
title= "极简图床、sm.ms图床curl上传图片"
draft = false
date= "2015-08-18 21:23:00"
+++

[极简图床](http://yotuku.cn/)是一个基于七牛的图床程序，使用方便、界面简洁美观，美中不足就是没有开放api，目前代码也没有开源。为了方便的在程序中上传图片至极简图床，我写了一段代码用curl来模拟上传图片，供大家参考：

```php
<?php
$data = base64_encode(file_get_contents('test.jpg'));

$ch = curl_init('http://yotuku.cn/upload?name=');                                                                      
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");                                                                     
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);                                                                  
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);                                                                      
curl_setopt($ch, CURLOPT_HTTPHEADER, array(                                                                          
    'Content-Type: text/plain',                                                                                
    'Content-Length: ' . strlen($data))                                                                       
);                                                                                                                   

$result = curl_exec($ch);
echo $result;
```

[sm.ms](https://sm.ms/)是vps.to、shadowsocks.com等站的站长，拥有t.tt、s.how等神域名的人建的一个图床，支持全站https，下面是curl上传图片至该站的代码：

```php
<?php
$url = 'https://sm.ms/index.php?act=upload';
$image = curl_file_create(realpath('test.jpg'), 'image/jpg', 'test.jpg');

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, ['smfile' => $image]);
$data = curl_exec($ch);
curl_close($ch);
echo $data;
```