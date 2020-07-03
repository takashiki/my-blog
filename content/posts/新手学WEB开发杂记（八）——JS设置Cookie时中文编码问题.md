+++
title= "新手学WEB开发杂记（八）——JS设置Cookie时中文编码问题"
draft = false
date= "2013-05-18 10:51:34"
+++

    最近写的一个页面中我使用了js来设置登录后的用户名cookie，但是PHP获取该cookie时，发现其值中的中文字符被编码成了\u开头的unicode编码，该编码在PHP中可以使用如下语句转换成utf8编码：
[js]preg_replace("#\\\u([0-9a-f]{4})#ie", "iconv('UCS-2BE', 'UTF-8', pack('H4', '\\1'))", $unicode_string)；[/js]
   
   我在同一个domain的另一个页面中登录时是采用php设置cookie的，php设置的cookie中的中文是utf8编码的。在PHP获取cookie时使用上面的语句处理一下就可以解决不同页面设置的cookie在另外的页面工作不正常的问题。
 
   还有另外一个办法可以解决该问题，也很简单，即JS端使用encodeURI() 函数可把字符串作为 URI 进行编码，PHP端使用urldecode函数进行解码。
 