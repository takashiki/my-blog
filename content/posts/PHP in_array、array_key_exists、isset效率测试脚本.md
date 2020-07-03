+++
title= "PHP in_array、array_key_exists、isset效率测试脚本"
draft = false
date= "2016-08-15 16:59:00"
+++

```php
<?php
$elemCount = 1000;
$repeatCount = 1000000;

$vArr = range(1, $elemCount);
$kArr = array_flip($vArr);

$start = microtime(true);
for ($i = 0; $i < $repeatCount; $i++) {
    in_array($i, $vArr);
}
$inArrTime = microtime(true) - $start;
echo "in_array:{$inArrTime}<br>";

$start = microtime(true);
for ($i = 0; $i < $repeatCount; $i++) {
    array_key_exists($i, $kArr);
}
$keyTime = microtime(true) - $start;
echo "array_key_exists:{$keyTime}<br>";

$start = microtime(true);
for ($i = 0; $i < $repeatCount; $i++) {
    isset($kArr[$i]);
}
$issetTime = microtime(true) - $start;
echo "isset:{$issetTime}<br>";
```

测试结果：

```
in_array:1.6679329872131
array_key_exists:0.23828101158142
isset:0.022069931030273
```