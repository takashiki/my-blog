+++
title= "通过curl每天自动在coding上创建task和push代码"
draft = false
date= "2015-10-03 21:10:00"
+++

Coding.net每天可以通过push代码和创建task赚取码币，码币可以用来换实物或coding的开发版服务。码币现在虽然汇率一直没有变过，但是获取码币是越来越难了，趁着还能每天获取保底0.03码币可多屯一点。

首先是创建task：

```php
<?php
$url = 'xxx';
$referer = 'xxx';
$cookie = 'xxx';
$userAgent = 'xxx';
$data = [
    'priority' => 1,
    'content' => 'xxx',
    'owner_id' => xxx,
    'deadline' => '',
    'description' => '',
]; 

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_TIMEOUT, 50);
curl_setopt($ch, CURLOPT_REFERER, $referer);
curl_setopt($ch, CURLOPT_USERAGENT, $userAgent);
curl_setopt($ch, CURLOPT_COOKIE, $cookie);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
var_dump(curl_exec($ch));
var_dump(curl_error($ch));
curl_close($ch);
```

，代码内的xxx都换为各自的数据就行了，在手动创建task时在chrome的开发者工具的network下可以看到，或者用其他抓包工具也可获取。

然后是自动push代码的：

```php
<?php
require 'Curl.php';

use Curl\Curl;

$url = [
    'create' => 'https://ide.coding.net/backend/ws/create',
    'write' => 'https://ide.coding.net/backend/ws/xxx/write',
    'status' => 'https://ide.coding.net/backend/git/xxx/status?__t=',
    'commit' => 'https://ide.coding.net/backend/git/xxx/commit',
    'push' => 'https://ide.coding.net/backend/git/xxx/push',
];
$referrer = 'https://ide.coding.net/ws/xxx';
$cookie = 'xxx';
$userAgent = 'xxx';
$data = [
    'create' => [
        'ownerName' => '',
        'projectName' => '',
        'host' => '',
        'spaceKey' => 'xxx',
    ],
    'write' => [
        'path' => '/README.md',
        'content' => 'xxx',
    ],
    'commit' => [
        'files[]' => 'README.md',
        'message' => 'xxx',
    ],
    'push' => [],
]; 

$get = getCurl($userAgent, $referrer);
$post = getCurl($userAgent, $referrer);
$put = getCurl($userAgent, $referrer);

var_dump($post->post($url['create'], $data['create']));
var_dump($put->put($url['write'], $data['write']));
var_dump($get->get($url['status'] . substr(str_replace('.', '', microtime(true)), 0, 13)));
var_dump($post->post($url['commit'], $data['commit']));
var_dump($post->post($url['push'], $data['push']));

function getCurl($userAgent, $referrer)
{
    $curl = new Curl();
    $curl->setUserAgent($userAgent);
    $curl->setReferrer($referrer);
    $curl->setCookie('sid', 'xxx');
    $curl->setCookie('_gat', 1);
    $curl->setCookie('_ga', 'xxx');
    $curl->setCookie('JSESSIONID', 'xxx');
    $curl->setHeader('X-Requested-With', 'XMLHttpRequest');
    $curl->setOpt(CURLOPT_SSL_VERIFYPEER, false);
    return $curl;
}
```

这段代码中用到了一个开源项目：[php-curl-class](https://github.com/php-curl-class/php-curl-class/blob/master/src/Curl/Curl.php)，原因是我自己构造的curl请求不知道为什么会获得401的返回。同样的代码内的所有xxx都要替换为各自对应的数据，其中create、write、commit、push四个步骤是必须的，status是为了观察执行情况。

至于如何实现定时执行计划任务，有条件的自然是在服务器上使用crontab，如果没有自己的服务器的，我比较推荐使用第三方的cron服务，比如sae和ace就有提供cron服务，sae目前有一定免费配额，虽然很少，不过用作执行计划任务绰绰有余，个人十分推荐。