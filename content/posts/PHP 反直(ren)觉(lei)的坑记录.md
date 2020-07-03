+++
title= "PHP 反直(ren)觉(lei)的坑记录"
draft = false
date= "2017-08-03 10:33:00"
+++

```php
$map = [
    '360' => '360',
    'baidu' => 'baidu',
    'google' => 'google',
];

$url = 'https://www.google.com';
foreach ($map as $key => $value) {
    if (strpos($url, $key) !== false) {
        echo $value;
        break;
    }
}
```

期望输出: google
实际输出: 360

参见：[http://php.net/manual/en/function.strpos.php](http://php.net/manual/en/function.strpos.php) 中 needle 参数的解释，'360' 在数组中被转换成了整型的 key，在 strpos 中使用到时整型的 360 就被当作了 ascii 序数值，而 `chr(360)` 结果为 `h`（chr 函数入参不在 0~255 范围内时会进行取模运算处理）。
------

```php
echo date('Y-m-d', strtotime('-1 month', strtotime('2017-07-31')));
```

期望输出: 2017-06-01
实际输出: 2017-07-01

参见：[https://bugs.php.net/bug.php?id=27793](https://bugs.php.net/bug.php?id=27793)。

PHP 的时间处理有很多类似的坑，主要是有点反直觉，`-1 month` 是减 30 天，即使使用 Datetime 类也会有类似的问题出现。

```php
<?php

$date1 = DateTime::createFromFormat('Y-m-d H:i:s', '2017-07-31 00:00:00');
$date2 = clone $date1;

$date1->modify('-1 month');
$date2->sub(new DateInterval("P1M"));

var_dump($date1->format('Y-m-d')); // 2017-07-01
var_dump($date2->format('Y-m-d')); // 2017-07-01
```

参见：[http://php.net/manual/en/class.datetime.php](http://php.net/manual/en/class.datetime.php)

------

```php
$arr = [1, 2, 3]; 

foreach ($arr as &$a) {}
foreach ($arr as $a) {}

var_dump($arr); 
```

这是 php 引用的一个坑，必须引用在循环结束之后必须 unset 一下，否则输出的结果与预期会不一致。

参考资料：[http://php.net/manual/en/control-structures.foreach.php](http://php.net/manual/en/control-structures.foreach.php)

具体案例可见 [https://laravel-china.org/articles/7001/php-ray-foreach-and-references-thunder](https://laravel-china.org/articles/7001/php-ray-foreach-and-references-thunder)

------

```php
$x = array('a');
$test = in_array(0, $x);
var_dump($test); // true

$x = array(0);
$test = in_array('a', $x);
var_dump($test); // true

$x = array('b' => 0);
$test = in_array('a', $x);
var_dump($test); // true

$x = array('0');
$test= in_array('a', $x);
var_dump($test); // false
```

可能很多人都不知道，`in_array` 函数有第三个参数 `strict`，这个参数默认为 false，不把这个参数设置成 true 就会出现上面的匪夷所思的情况。
但是 `strict` 为 true 的情况下会对值的类型进行判断，在实际应用场景中如果数据类型没有进行恰当的处理也可能有坑。

之所以前面三个 in_array 的结果都为 true，是因为在 php 中 `'a' == 0`，除了 in_array，switch case 等也会出现类似情况。

参考链接：[http://php.net/in_array](http://php.net/in_array)