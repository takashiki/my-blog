+++
title= "PHP通过fsock实现异步HTTP请求"
draft = false
date= "2016-06-29 11:18:00"
+++

参考文章：

[PHP实现异步调用方法研究](http://www.laruence.com/2008/04/14/318.html)
[使用fscok实现异步调用PHP](http://www.laruence.com/2008/04/16/98.html)
[how-to-make-async-requests-in-php](https://segment.com/blog/how-to-make-async-requests-in-php/)

```php
function asyncRequest($url, $params = array(), $type = 'GET')
{
    $query = http_build_query($params);

    $parts = parse_url($url);

    $fp = fsockopen(
        $parts['host'],
        isset($parts['port']) ? $parts['port'] : 80,
        $errno,
        $errstr,
        30
    );

    $location = $parts['path'] . (empty($parts['query']) ? '' : "?{$parts['query']}");
    $location .= ($type == 'GET' && !empty($query)) ? (empty($parts['query']) ? '?' : '&').$query : '';

    $out = "{$type} {$location} HTTP/1.1\r\n";
    $out .= "Host: {$parts['host']}\r\n";
    $out .= "Connection: Close\r\n\r\n";
    $out .= $type == 'POST' ? "Content-Type: application/x-www-form-urlencoded\r\n" : '';
    $out .= 'Content-Length: '.strlen($query)."\r\n";
    $out .= ($type == 'POST' && isset($query)) ? $query : '';

    fwrite($fp, $out);
    fclose($fp);
}
```

注意点：

服务端 PHP 要设置 `ignore_user_abort` 为 `ture`，Apache 需要在 `Apache.conf` 中设置对应的 `php_value ignore_user_abort`，nginx 需要设置 `fastcgi_ignore_client_abort` 为 `on`。