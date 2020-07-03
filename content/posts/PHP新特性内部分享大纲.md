+++
title= "PHP新特性内部分享大纲"
draft = false
date= "2016-06-28 22:06:40"
+++

### [PHP 5.4](http://php.net/manual/en/migration54.new-features.php)  

#### 数组短标签

```php
$arr = array(1, 2, 3);

$arr = [1, 2, 3];
```

#### 函数返回值数组访问解析

```php
function get_arr() {
    return [
        'a' => 1,
        'b' => 2,
    ];
}

echo get_arr()['a'];
```

#### 在实例化时访问类成员

```php
$query = new Query();
$news = $query->from('news')->all();

$news = (new Query())->from('news')->all();
```

#### traits

场景：soft delete等

```php
trait SoftDeleteTrait
{
    public function delete()
    {
        $this->status = Status::DELETED;

        return $this->save();
    }
}

class News extends \yii\db\ActiveRecord
{
    use SoftDeleteTrait;
}

$news = News::findOne($condition);
$news->delete();
```

#### 内置的http服务器

```shell
php -S localhost:8000
```

实例：[https://github.com/laravel/valet](https://github.com/laravel/valet)

#### 默认字符集改为 `UTF-8`

[http://php.net/manual/en/function.htmlspecialchars.php](http://php.net/manual/en/function.htmlspecialchars.php)

### [PHP 5.5](http://php.net/manual/en/migration55.new-features.php)

[http://php.net/manual/en/migration55.new-features.php](http://php.net/manual/en/migration55.new-features.php)

#### `foreach`支持`list`

在元素顺序固定时使用比较方便。

```php
$news = [
    [
        'title' => 'title1',
        'content' => 'content1',
        'url' => 'url1',
    ],
    [
        'title' => 'title2',
        'content' => 'content2',
        'url' => 'url2',
    ],
];

foreach ($news as $r) {
    echo $r['title'].$r['content'].$r['url'];
}

foreach ($news as list($title, $content, $url)) {
    echo $title.$content.$url;
}
```

#### `empty`支持任意表达式

```php
function get_result() {
    return false;
}

$var = get_result();
var_dump(empty($var));

var_dump(empty(get_result()));
```

#### 数组和字符串直接取值

```php
echo [1, 2, 3][0];
echo 'string'[0];
```

#### 通过 `::class` 获取类名

```php
echo News::class;

//yii2中的兼容5.4的实现
class Object implements Configurable
{
    public static function className()
    {
        return get_called_class();
    }
}

News::className();
```

#### 生成器

生成器和迭代器有点类似，但是与标准的PHP迭代器不同，PHP生成器不要求类实现`Iterator`接口，生成器会根据需求每次计算并产出需要迭代的值，从而减轻了类的开销和负担。这在处理较大的特殊文件、缓存数据等时会有比较明显的优势。

```php
function generatorRange($length) {
    for ($i=0; $i<$length; $i++) {
        yield $i;
    }
}

function iteratorRange($length) {
    $dataSet = [];
    for ($i=0; $i<$length; $i++) {
        $dataSet[] = $i;
    }
    return $dataSet;
}

foreach (generatorRange(10000000) as $i) {
    if ($i % 1000000 == 0) {
        echo $i.'<br>';
    }
}
```

#### 集成 `Zend Opcache`

### [PHP 5.6](http://php.net/manual/en/migration56.new-features.php)

#### 使用表达式定义常量

在之前的 PHP 版本中， 必须使用静态值来定义常量，声明属性以及指定函数参数默认值。 现在你可以使用包括数值、字符串字面量以及其他常量在内的数值表达式来 定义常量、声明属性以及设置函数参数默认值。

```php
const ONE = 1;
const TWO = ONE * 2;

class C {
    const THREE = TWO + 1;
    const ONE_THIRD = ONE / self::THREE;
    const SENTENCE = 'The value of THREE is '.self::THREE;

    public function f($a = ONE + self::THREE) {
        return $a;
    }
}

echo (new C)->f().'<br>';
echo C::SENTENCE;
```

#### 常量支持数组

可以通过 `const` 关键字来定义类型为 `array` 的常量。

```php
const ABC = ['a', 'b', 'c'];
```

#### `...` 运算符

参数合并

```php
function f($req, $opt = null, ...$params) {
    // $params 是一个包含了剩余参数的数组
    printf('$req: %d; $opt: %d; number of params: %d'."<br>",
           $req, $opt, count($params));
}

f(1);
f(1, 2);
f(1, 2, 3);
f(1, 2, 3, 4);
f(1, 2, 3, 4, 5);
```

参数展开

```php
function add($a, $b, $c) {
    return $a + $b + $c;
}

$operators = [2, 3];
echo add(1, ...$operators);
```

#### `**` 运算符

用于幂运算

```php
$a = 2;
$a **= 3;
printf("a = %d", $a);
```

#### `use` 可用于函数和常量

函数和常量可以不必封装在类中就可以支持命名空间。

```php
namespace Name\Space {
    const SORT_ASC = 1;
    const SORT_DESC = -1;
    function phpversion() { return 'custom'; }
}

namespace {
    echo SORT_ASC.' '.SORT_DESC.'<br>';
    echo phpversion().'<br>';

    use const Name\Space\SORT_ASC;
    use const Name\Space\SORT_DESC;
    use function Name\Space\phpversion;

    echo SORT_ASC.' '.SORT_DESC.'<br>';
    echo phpversion().'<br>';
}
```

#### 大文件上传

现在可以支持大于 2GB 的文件上传。

#### `php://input` 是可重用的了

可以多次打开并读取`php://input`， 数据流支持`seek` 操作，同时，这个特性使得在处理 POST 的数据的时候， 可以明显降低对于内存的需求量。

### [PHP 7](http://php.net/manual/en/migration70.new-features.php)

`PHP 7` 最令人激动的就是性能上的提升了，下面是来自鸟哥惠新宸的一些测试图片：

![5.6 vs 7.0](http://laruence-wordpress.stor.sinaapp.com/uploads/MYVQSTIBYX6KHZQ9XH72U-1024x573.jpg)

![benchmark](http://img.ptcms.csdn.net/article/201509/16/55f972f220584_middle.jpg)

![wordpress qps](http://img.ptcms.csdn.net/article/201509/16/55f9735ed3e69_middle.jpg)

#### `??` 运算符

日常使用中存在大量同时使用三元表达式和 isset()的情况而新增的语法糖。

```php
$result = isset($var) ? $var : 'none';

$result = $var ?? 'none';
```

#### `<=>` 比较操作符

组合比较符用于比较两个表达式。当$a小于、等于或大于$b时它分别返回-1、0或1。比较的原则是沿用 PHP 的[常规比较规则](http://php.net/manual/en/types.comparisons.php)进行的

```php
$arr = [
    ['name' => 'one', 'age' => 23],
    ['name' => 'two', 'age' => 12],
    ['name' => 'three', 'age' => 55],
];

usort($arr, function($a, $b) {
    return $a['age'] <=> $b['age'];
});

var_dump($arr);
```

#### `Unicode codepoint` 转译语法

这接受一个以16进制形式的 `Unicode codepoint`，并打印出一个双引号或 `heredoc` 包围的 UTF-8 编码格式的字符串。 可以接受任何有效的 `codepoint`，并且开头的 0 是可以省略的。

```php
//emoji微笑
echo "\u{1F603}";
```

#### 标量类型声明

标量类型声明有两种模式: 强制 (默认) 和 严格模式。 现在可以使用下列类型参数（无论用强制模式还是严格模式）： 字符串(string), 整数 (int), 浮点数 (float), 以及布尔值 (bool)。它们扩充了PHP5中引入的其他类型：类名，接口，数组和 回调类型。

```php
declare(strict_types=0);

function sumOfInts(int ...$ints)
{
    return array_sum($ints);
}

var_dump(sumOfInts(2, '3', 4.1));
```

标量类型声明在目前的阶段对性能是有负面的影响的，但类型提示会对类型推断起到帮助作用, `PHP 7.1` 中已经加入了"类似"JIT的技术(type specifical opcode handler), 到时候类型声明则可以间接地提高性能。

#### 返回值类型声明

支持函数`function`、方法`method`或者匿名函数`closure`的返回值类型声明。返回值支持的类型有：string、int、float、bool、array、[callable](http://php.net/manual/en/language.types.callable.php)、self（仅成员方法）、parent（仅成员方法）、Closure、类名、接口名。

```php
function sum5($a, $b) {
    return $a + $b;
}

function sum7($a, $b): float {
    return $a + $b;
}

var_dump(sum5(1, 2), sum7(1, 2), sum5(1.0, 2));
```

```php
class News
{
    public static function findNewsYouNeed()
    {
        return null;
    }
}

function getNews(): array {
    $news = News::findNewsYouNeed();
    return $news;
}

foreach ($news as $r) {}
```

#### `unserialize()` 过滤

这个特性旨在提供更安全的方式解包不可靠的数据。它通过白名单的方式来防止潜在的代码注入。

```php
// converts all objects into __PHP_Incomplete_Class object
$data = unserialize($foo, ["allowed_classes" => false]);

// converts all objects into __PHP_Incomplete_Class object except those of MyClass and MyClass2
$data = unserialize($foo, ["allowed_classes" => ["MyClass", "MyClass2"]);

// default behaviour (same as omitting the second argument) that accepts all classes
$data = unserialize($foo, ["allowed_classes" => true]);
```

#### 常量数组支持 `define()` 定义

`PHP5.6`开始支持`const`定义数组常量，`PHP7`开始支持`define()`。

```php
<?php
define('ANIMALS', [
    'dog',
    'cat',
    'bird'
]);

echo ANIMALS[1];
```

#### 匿名类

现在支持通过 `new class` 来实例化一个匿名类，这可以用来替代一些“用后即焚”的完整类定义。

```php
<?php
interface Logger {
    public function log(string $msg);
}

class Application {
    private $logger;

    public function getLogger(): Logger {
         return $this->logger;
    }

    public function setLogger(Logger $logger) {
         $this->logger = $logger;
    }
}

$app = new Application;
$app->setLogger(new class implements Logger {
    public function log(string $msg) {
        echo $msg;
    }
});

var_dump($app->getLogger());
```

#### Closure::call()

Closure::call() 可以方便地即时绑定一个闭包到对象上并调用它，而且它的性能更好。

```php
class A {private $x = 1;}

// Pre PHP 7 code
$getXCB = function() {return $this->x;};
$getX = $getXCB->bindTo(new A, A::class); // intermediate closure
echo $getX();

// PHP 7+ code
$getX = function() {return $this->x;};
echo $getX->call(new A);
```

#### `IntlChar`

新增加的 IntlChar 类旨在暴露出更多的 ICU 功能。这个类自身定义了许多静态方法用于操作多字符集的 `unicode` 字符。

```php
printf('%x', IntlChar::CODEPOINT_MAX);
echo '<br>'.IntlChar::charName('@').'<br>';
var_dump(IntlChar::ispunct('!'));
```

若要使用此类，需先安装 `Intl` 扩展。

#### 预期

预期是向后兼用并增强之前的 `assert()` 的方法。 它使得在生产环境中启用断言为零成本，并且提供当断言失败时抛出特定异常的能力。

老版本的API出于兼容目的将继续被维护，`assert()` 现在是一个语言结构，它允许第一个参数是一个表达式，而不仅仅是一个待计算的 `string` 或一个待测试的 `boolean`。

```php
ini_set('assert.exception', 1);

class CustomError extends AssertionError {}

assert(false, new CustomError('Some error message'));
```

#### `Group use declarations`

从同一 `namespace` 导入的类、函数和常量现在可以通过单个 use 语句 一次性导入了。

```php
// Pre PHP 7 code
use some\namespace\ClassA;
use some\namespace\ClassB;
use some\namespace\ClassC as C;

use function some\namespace\fn_a;
use function some\namespace\fn_b;
use function some\namespace\fn_c;

use const some\namespace\ConstA;
use const some\namespace\ConstB;
use const some\namespace\ConstC;

// PHP 7+ code
use some\namespace\{ClassA, ClassB, ClassC as C};
use function some\namespace\{fn_a, fn_b, fn_c};
use const some\namespace\{ConstA, ConstB, ConstC};
```

#### 生成器支持 `return`

这个特性是基于 `PHP 5.5` 版本中引入的生成器的，它使得生成器内部可以使用`return`语句返回一个最终的表达式（不允许返回引用）。该返回值在生成器产生完所有的值之后可以通过  `getReturn()` 方法获取到。

```php
$gen = (function() {
    yield 1;
    yield 2;

    return 3;
})();

foreach ($gen as $val) {
    echo $val, PHP_EOL;
}

echo $gen->getReturn(), PHP_EOL;
```

#### 生成器委托 `Generator delegation`

现在我们可以直接在构造生成器时通过 `yield from` 自动将另一个生成器、对象或数组作为自己的成员，而不需要在生成器外部去写冗余代码。

```php
function gen()
{
    yield 1;
    yield 2;

    yield from gen2();
}

function gen2()
{
    yield 3;
    yield 4;
}

foreach (gen() as $val)
{
    echo $val, PHP_EOL;
}
```

#### 使用 `intdiv()` 计算整数除法

用于计算整数除法。

```php
function div($a, $b) {
    var_dump(intval($a / $b), intdiv($a, $b));
    echo '<br>';
}

div(3, 2);
div(-3, 2);
div(3, -2);
div(-3, -2);
div(PHP_INT_MAX, PHP_INT_MAX);
div(PHP_INT_MIN, PHP_INT_MIN);
div(PHP_INT_MIN, -1);
div(1, 0);
```

#### `Session`配置项

`session_start()`
现在可以接收一个包含配置的数组以覆盖写在 `php.ini` 中的 `session` 配置项。

```php
session_start([
    'cache_limiter' => 'private',
    'read_and_close' => true,
]);
```

#### `preg_replace_callback_array()`

> mixed preg_replace_callback ( mixed $pattern , callable $callback , mixed $subject [, int $limit = -1 [, int &$count ]] )

> mixed preg_replace_callback_array ( array $patterns_and_callbacks , mixed $subject [, int $limit = -1 [, int &$count ]] )

在`PHP7`之前使用`preg_replace_callback`时只能使用一个特定的回调函数来替换匹配到的表达式，这使得有可能需要在回调函数里写分支来实现特定的替换逻辑，现在有了`preg_replace_callback_array`就可以让每个不同的表达式对应不同的回调函数。

```php
$subject = 'Aaaaaa Bbb';

echo preg_replace_callback_array(
    [
        '~[a]+~i' => function ($match) {
            return str_repeat('1', strlen($match[0]));
        },
        '~[b]+~i' => function ($match) {
            return str_repeat('2', strlen($match[0]));
        }
    ],
    $subject
);
```

#### 更可靠的随机函数

新增两个`CSPRNG`函数：`random_int`和`random_bytes`。

[https://github.com/paragonie/random_compat](https://github.com/paragonie/random_compat) 让`PHP 5.x`也可以使用`random_int`和`random_bytes`。

以上函数的随机性不同的取决于环境：

- 在window上，`CryptGenRandom()`总是被使用。
- 在其他平台，`arc4random_buf()`如果可用会被使用（在BSD系列或者具有libbsd的系统上成立）
- 以上都不成立的话，一个linux系统调`用getrandom(2)`会被使用
- 如果还不行，`/dev/urandom` 会被作为最后一个可使用的工具
- 如果以上都不行，系统会抛出错误

```php
$times = 600000; 
$csprng = 0; 
$rand = 0;

for ($i = 0; $i < $times; $i++){ 
    $csprng += roll() === 6 ? 1 : 0;
    $rand += roll(false) === 6 ? 1 : 0;
} 

function roll($csprng = true){ 
    return $csprng ? random_int(1, 6) : rand(1, 6); 
}

var_dump($csprng, $rand); 
```

#### 关键词在特定的场景中也可以使用

```php
class Test 
{
    public static function forEach($param) 
    {
        var_dump($param);
    }
    
    public static function function($param) 
    {
        static::forEach($param);
    }
}

Test::function([1,2,3]);
```

### 附录

#### [PHP7 一些不向后兼容的变更](http://php.net/manual/zh/migration70.incompatible.php)

`PHP 5.x`在版本更新中不向后兼容的变更大多数都是历史比较久远的特性了，现在的代码里尤其是在使用框架的情况下基本见不到，`PHP 7`的改动比较大，但影响到的部分一般也并不常用，很多优先级的改动其实只要实际编码中注意多使用 `()` 和 `{}`，原本的代码基本就可以无痛迁移至 `PHP 7`。

#### [PHP7 Compatibility Checker](https://github.com/sstalle/php7cc)

```shell
composer global require sstalle/php7cc

php7cc --help

php7cc /path/to/my/directory/
```

#### 参考资料

[风雪之隅](http://www.laruence.com/)

[http://www.php7.site/](http://www.php7.site/book/php7/about-30.html)

[现代 PHP 新特性系列文章](http://laravelacademy.org/modern-php/feature-modern-php)

