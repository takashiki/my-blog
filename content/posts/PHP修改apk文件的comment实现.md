+++
title= "PHP修改apk文件的comment实现"
draft = false
date= "2016-09-20 21:24:00"
+++

参考链接：
[一种动态为apk写入信息的方案](http://pingguohe.net/2016/03/21/Dynimac-write-infomation-into-apk.html?utm_source=tuicool&utm_medium=referral)

apk文件本身即为zip文件，在PHP中可以使用 `ZipArchive` 类中的 `setArchiveComment` 方法方便地设置 apk 的 comment 内容。

也可以使用 `fseek` 和 `fwrite` 来参照上述文章原理实现：

```php
$comment = '123测试';

$file = fopen('R:\1.apk', 'r+');
fseek($file, -2, SEEK_END);
fwrite($file, pack('s', mb_strlen($comment, '8bit')));
fwrite($file, $comment);
fclose($file);

$zip = new ZipArchive();

$zip->open('R:\1.apk');
var_dump($zip->getArchiveComment());
//$zip->setArchiveComment($comment);
//var_dump($zip->getArchiveComment());
$zip->close();
```