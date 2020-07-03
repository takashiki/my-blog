+++
title= "jsonp接口xss防范"
draft = false
date= "2016-02-17 11:44:37"
+++

之前编写jsonp接口的时候并未注意xss的问题，最近经同事提醒才注意到这一点。

防范方式也很简单，只要在header里输出类型设置为javascript即可：

```php
header('Content-type: text/javascript;charset=utf-8');
```