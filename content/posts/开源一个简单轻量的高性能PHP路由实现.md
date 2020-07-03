+++
title= "开源一个简单轻量的高性能PHP路由实现"
draft = false
date= "2016-07-02 19:57:00"
+++

Github:[https://github.com/takashiki/cdo](https://github.com/takashiki/cdo)

Git@OSC:[http://git.oschina.net/takashiki/cdo](http://git.oschina.net/takashiki/cdo)

使用很简单，不过只支持 pathinfo 模式，贴一段示例代码：

```php
$do = new \Mis\Cdo();

$do->get('/', function () {
    echo 'hello world';
});

$do->post('/', function () {
    $name = isset($_POST['name']) ? $_POST['name'] : 'world';
    echo "hello {$name}";
});

$do->any('/(\d+)', function ($id) {
    echo $id;
});

/**
 * When using named subpattern, order of parameters is not matter.
 * eg. /book/2
 */
$do->any('/(?P<type>\w+)/(?P<page>\d+)', function ($page, $type) {
    echo $type.'<br>'.$page;
});

$do->run();
```

或者：

```php
use Mis\Cdo;

Cdo::get('/', function () {
    echo 'hello world';
});

Cdo::run();
```

写这个项目的初衷是前断时间在写一个小项目时发现现在绝大多数 PHP 的路由都不足够轻量，在只有各位数的路由时 QPS 也只能达到不使用路由时的一半左右，于是便自己写了一个。

这是在 index 文件里直接打印 `hello world` 的 qps：

![QQ截图20160702204339.jpg](https://ooo.0o0.ooo/2016/07/02/5777b8ef78859.jpg)

这是使用了路由后的qps：

![QQ截图20160702204316.jpg](https://ooo.0o0.ooo/2016/07/02/5777b8ecb250f.jpg)
