+++
title= "将cow的stat文件自动转为pac文件"
draft = false
date= "2015-10-09 22:01:16"
+++

[cow](https://github.com/cyfdecyf/cow)是一个简化穿墙的 HTTP 代理服务器。它能自动检测被墙网站，它的检测结果会保存在stat文件中。该文件为一个json文件，里面记录了特定的网址直接访问和被block的次数，通过分析该文件即可创建一个包含黑白名单的pac文件，使用黑白名单加cow的本地代理方案是比较省心省流量的。

以下代码可以自动将stat文件转为pac文件：

```php
<?php
$src = 'R:\stat.txt';
$dest = 'R:\my.pac';
$common = <<<EOF
var proxy = 'PROXY 127.0.0.1:7777; DIRECT';

var direct = 'DIRECT';

var IsMatch = function(host, domain) {
    return host.indexOf(domain, host.length - domain.length) !== -1 && 
    (domain.length === host.length || host.indexOf("." + domain, host.length - ("." + domain).length) !== -1);
}

function FindProxyForURL(url, host) {
    host = host.toLowerCase();

    for (i = 0; i < blackList.length; i++) {
        if (IsMatch(host, blackList[i])) {
            return proxy;
        }
    }

    for (i = 0; i < whiteList.length; i++) {
        if (IsMatch(host, whiteList[i])) {
            return direct;
        }
    }
    
    return proxy;
}
EOF;

$stat = file_get_contents($src);
$sites = json_decode($stat, true)['site_info'];
$black = [];
$white = [];
foreach ($sites as $url => $stat) {
    if (filter_var($url, FILTER_VALIDATE_IP)) continue;
    preg_match('/(?:.+\.)?(\w+\.\w+)/', $url, $matches);
    if (! isset($matches[1])) continue;
    if ($stat['block'] > 0) {
        $black[$matches[1]] = '"' . $matches[1] . '"';
    } else {
        $white[$matches[1]] = '"' . $matches[1] . '"';
    }
}
var_dump($black);
var_dump($white);
$blackList = 'var blackList = [' . PHP_EOL . '    ' . implode(',' . PHP_EOL . '    ', $black) . PHP_EOL . '];';
$whiteList = 'var whiteList = [' . PHP_EOL . '    ' . implode(',' . PHP_EOL . '    ', $white) . PHP_EOL . '];';
file_put_contents($dest, $blackList . PHP_EOL . PHP_EOL . $whiteList . PHP_EOL . PHP_EOL . $common);
```