+++
title= "PHP编码规范内部分享大纲"
draft = false
date= "2016-06-28 22:10:00"
+++

## 序言

### 为什么要有规范

> 在谷歌，我可以查看任何的代码，进入所有谷歌的代码库，我有权查看它们。事实上，这种权限是很少人能拥有的。但是，让我感到惊讶的却是，如此多的编码规范—缩进，命名，文件结构，注释风格—这一切让我出乎意料的轻松的阅读任意一段代码，并轻易的看懂它们。这让我震惊—因为我以为这些规范是微不足道的东西。它们不可能有这么大的作用—但它们却起到了这么大的作用。当你发现只通过看程序的基本语法结构就能读懂一段代码，这种时间上的节省不能不让人震撼！ —— Mark CC.《Google为何要执行严格的代码编写规范》

现在项目规模和团队规模不断壮大，如果不执行规范，只会让整个项目的理解和沟通更加复杂。本指南的意图是为了减少不同开发者在浏览代码时减少认知的差异。为此列举一组如何格式化PHP代码的共用规则。 

### 现有的一些规范

[PSR规范](http://www.php-fig.org/psr/)

[PEAR 编码准则](http://pear.php.net/manual/en/standards.php)

[Symfony 编码准则](http://symfony.com/doc/current/contributing/code/standards.html)

## PHP-FIG

[FIG组织 (Framework Interop Group)](http://www.php-fig.org/) 在制定跟PHP相关规范 (PHP Standard Recommendation)，简称[PSR](https://github.com/php-fig/fig-standards)。按照其官网的说法，这个组织的目的并不是告诉你你应该怎么做，只是一些主流的框架之间相互协商和约定。但是目前PSR已经成了PHP社区主流的代码规范。

在PHP-FIG出现之前，PHP的社区可以说是一盘散沙，各种风格和标准同时存在，熟悉不同项目的代码需要额外的成本。PHP-FIG 的意义对普通开发者来说，好处很多，如果你熟悉一个遵守标准的框架，你学习另一个框架也会快很多，代码也容易读懂，你要开源一个遵守标准的库，别人也容易使用和掌握；对框架团队来说，竞争就更激烈了，因为编码风格上的优势现在大家都没了（以前这真算一个优势），现在只能拼框架的设计、效率、扩展性、可用的类库，等，但这对开发者来说还是个好处。

其实 PHP-FIG 的这些标准，和设计模式的性质是差不多的，都是些最佳实践，通过反复实践沉淀下来的东西会更加稳定一些，固化下来有利于大家的沟通和交流。

现有的PSR规范如下：

PSR-0 Autoloading Standard (Deprecated)

PSR-1 [Basic Coding Standard](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-1-basic-coding-standard.md)

PSR-2 [Coding Style Guide](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-2-coding-style-guide.md)

PSR-3 Logger Interface

PSR-4 [Autoloader](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-4-autoloader.md)

PSR-5 [PHPDoc](https://github.com/phpDocumentor/fig-standards/blob/master/proposed/phpdoc.md) (Draft)

PSR-6 Cache Interface

PSR-7 HTTP Message Interface

PSR-8 Hug (April Fool)

PSR-9 Security Reporting Process (Draft)

PSR-10 Security Disclosure Publication (Draft)

PSR-11 Container Interoperability (Draft)

PSR-12 [Extended Coding Style Guide](https://github.com/php-fig/fig-standards/blob/master/proposed/extended-coding-style-guide.md) (Draft)

### 1. 概览

----------

该文档基于PSR-12的结构，将PSR-1、PSR-2以及PSR-12进行了总结。

- 源文件`必须`只使用 `<?php` 和 `<?=` 这两种标签。

- 源文件中php代码的编码格式`必须`只使用不带`字节顺序标记(BOM)`的`UTF-8`。

- 一个源文件`建议`只用来做声明（`类(class)`，`函数(function)`，`常量(constant)`等）或者只用来做一些引起副作用的操作（例如：输出信息，修改`.ini`配置等）,但`不建议`同时做这两件事。

- `命名空间(namespace)`和`类(class)` `必须`遵守[PSR-0][]标准。

- `类名(class name)` `必须`使用`帕斯卡式(PascalCase)`写法 (后文将直接用`PascalCase`表示)。

- `类(class)`中的常量`必须`只由大写字母和`下划线(_)`组成。

- `方法名(method name)` `必须`使用`驼峰式(cameCase)`写法(后文将直接用`camelCase`表示)。

- 代码`必须`使用4个空格来进行缩进，而不是用制表符。

- 一行代码的长度`不建议`有硬限制；软限制`必须`为120个字符，`建议`每行代码80个字符或者更少。

- 在`命名空间(namespace)`的声明下面`必须`有一行空行，并且在`导入(use)`的声明下面也`必须`有一行空行。

- `类(class)`的左花括号`必须`放到其声明下面自成一行，右花括号则`必须`放到类主体下面自成一行。

- `方法(method)`的左花括号`必须`放到其声明下面自成一行，右花括号则`必须`放到方法主体的下一行。

- 所有的`属性(property)`和`方法(method)` `必须`有可见性声明；`抽象(abstract)`和`终结(final)`声明`必须`在可见性声明之前；而`静态(static)`声明`必须`在可见性声明之后。

- 在控制结构关键字的后面`必须`有一个空格；而`方法(method)`和`函数(function)`的关键字的后面`不可`有空格。

- 控制结构的左花括号`必须`跟其放在同一行，右花括号`必须`放在该控制结构代码主体的下一行。

- 控制结构的左括号之后`不可`有空格，右括号之前也`不可`有空格。

#### 实例

```php
<?php
declare(strict_types=1);

namespace Vendor\Package;

use Vendor\Package\{ClassA as A, ClassB, ClassC as C};
use Vendor\Package\Namespace\ClassD as D;

use function Vendor\Package\{functionA, functionB, functionC};
use const Vendor\Package\{ConstantA, ConstantB, ConstantC};

class Foo extends Bar implements FooInterface
{
    public function sampleFunction(int $a, int $b = null): array
    {
        if ($a === $b) {
            bar();
        } elseif ($a > $b) {
            $foo->bar($arg1);
        } else {
            BazClass::bar($arg2, $arg3);
        }
    }

    final public static function bar()
    {
        // method body
    }
}


```

### 2. 通则

----------

### 2.1 基础代码规范

代码`必须`遵守 [PSR-1][] 和 [PSR-2][] 中的所有规则。

#### 2.2 源文件

所有的PHP源文件`必须`使用Unix LF(换行)作为行结束符。

> File > Settings > Editor > Coding Style 设置换行符为LF。

所有PHP源文件`必须`以一个空行结束。

纯PHP代码源文件的关闭标签`?>` `必须`省略。

##### 2.2.1 PHP标签

PHP代码`必须`只使用`长标签(<?php ?>)`或者`短输出式标签(<?= ?>)`；而`不可`使用其他标签。

##### 2.2.2 字符编码

PHP代码的编码格式`必须`只使用不带`字节顺序标记(BOM)`的`UTF-8`。

> File > Settings > Editor > File Encodings 设置IDE Encoding为UTF-8。

##### 2.2.3 副作用

一个源文件`建议`只用来做声明（`类(class)`，`函数(function)`，`常量(constant)`等）或者只用来做一些引起副作用的操作（例如：输出信息，修改`.ini`配置等）,但`不建议`同时做这两件事。

短语`副作用(side effects)`的意思是 *在包含文件时* 所执行的逻辑与所声明的`类(class)`，`函数(function)`，`常量(constant)`等没有直接的关系。

`副作用(side effects)`包含但不局限于：产生输出，显式地使用`require`或`include`，连接外部服务，修改ini配置，触发错误或异常，修改全局或者静态变量，读取或修改文件等等

下面是一个既包含声明又有副作用的示例文件；即应避免的例子：

```php
<?php
// 副作用：修改了ini配置
ini_set('error_reporting', E_ALL);

// 副作用：载入了文件
include "file.php";

// 副作用：产生了输出
echo "<html>\n";

// 声明
function foo()
{
    // 函数体
}
```

下面是一个仅包含声明的示例文件；即应提倡的例子：

```php
<?php
// 声明
function foo()
{
    // 函数体
}

// 条件式声明不算做是副作用
if (! function_exists('bar')) {
    function bar()
    {
        // 函数体
    }
}
```

#### 2.3 行

行长度`不可`有硬限制。

行长度的软限制`必须`是120个字符；对于软限制，代码风格检查器`必须`警告但`不可`报错。

一行代码的长度`不建议`超过80个字符；较长的行`建议`拆分成多个不超过80个字符的子行。

在非空行后面`不可`有空格。

空行`可以`用来增强可读性和区分相关代码块。

一行`不可`多于一个语句。

#### 2.4 缩进

代码`必须`使用4个空格，且`不可`使用制表符来作为缩进。

> 注意：代码中只使用空格，且不和制表符混合使用，将会对避免代码差异，补丁，历史和注解中的一些问题有帮助。空格的使用还可以使通过调整细微的缩进来改进行间对齐变得更加的简单。


#### 2.5 关键字和 True/False/Null

PHP类型(`int`, `object`, `float`, `mixed`,
`bool`, `numeric`, `string` 和 `resource`)、常量(`true`, `false`和`null`)和关键字([keywords][])  `必须`使用小写字母。

### 3. `声明(Declare)`,`命名空间(Namespace)`和`导入(Use)`声明

如果存在`declare`语句，那么该语句后`必须`有一行空行，如`declare(ticks=);`。

declare语句`必须`紧跟在PHP开始标签的下一行，在declare语句前`不可`有空行。

一行`不可`有多个declare语句。

当开始标签`<?php`在文件的第一行时, 该行`不可`有其他语句。

`命名空间(namespace)`的声明后面`必须`有一行空行。

`命名空间(namespace)``必须`写在`declare`语句之后。

所有的`导入(use)`声明`必须`放在`命名空间(namespace)`声明的下面。

一句声明中，`必须`只有一个`导入(use)`关键字。

Use statements MUST be in blocks, grouped by varying entity (classes [inc. interfaces and traits],
functions or constants). To elaborate, this means that any and all classes are in a block
together; any and all functions are in a block together; and any and all constants must
be grouped together. Within each block there MUST be no blank lines. If a block has
multiple lines there MUST be a blank line before the first line and a blank line after
the last line.

Classes, functions or constants grouped together into a single line must be listed
alphabetically.

The groups MUST be ordered such that classes (together with interfaces and traits) are first,
followed by functions and then constants.

Example of the above notices about namespace, strict types and use declarations:

```php
<?php
declare(strict_types=1);

namespace Vendor\Package;

use Vendor\Package\{ClassA as A, ClassB, ClassC as C};
use Vendor\Package\Namespace\ClassD as D;
use Vendor\Package\AnotherNamespace\ClassE as E;

use function Vendor\Package\{functionA, functionB, functionC};
use const Vendor\Package\{ConstantA, ConstantB, ConstantC};

class FooBar
{
    // ... additional PHP code ...
}

```

Compound namespaces with a depth of two or more MUST not be used. Therefore the
following is the maximum compounding depth allowed:
```php
<?php

use Vendor\Package\Namespace\{
    SubnamespaceOne\ClassA,
    SubnamespaceOne\ClassB,
    SubnamespaceTwo\ClassY,
    ClassZ,
};
```

When wishing to declare strict types in files containing markup outside PHP
opening and closing tags MUST, on the first line, include an opening php tag,
the strict types declaration and closing tag.

For example:
```php
<?php declare(strict_types=1); ?>
<html>
<body>
    <?php
        // ... additional PHP code ...
    ?>
</body>
</html>
```

Declare statements MUST contain no spaces and MUST look like `declare(strict_types=1);`.

Block declare statements are allowed and MUST be formatted as below. Note position of
braces and spacing:
```php
declare(ticks=1) {
    //some code
}
```

### 4. `类(class)`，`属性(property)`和`方法(method)`

术语“类”指所有的`类(class)`，`接口(interface)`和`特性(trait)`。

类的右花括号后同一行内`不可`有任何注释或语句。

当实例化一个类时，即使没有任何初始化参数，也`必须`写上括号。

```php
new Foo();
```

#### 4.1 `扩展(extend)`和`实现(implement)`

一个类的`扩展(extend)`和`实现(implement)`关键词`必须`和`类名(class name)`在同一行。

`类(class)`的左花括号`必须`放在下面自成一行，且其之前或之后`不可`有空行；右花括号必须放在`类(class)`主体的后面自成一行，且其之前`不可`有空行。

```php
<?php
namespace Vendor\Package;

use FooClass;
use BarClass as Bar;
use OtherVendor\OtherPackage\BazClass;

class ClassName extends ParentClass implements \ArrayAccess, \Countable
{
    // constants, properties, methods
}
```


`实现(implement)`列表`可以`被拆分为多个缩进了一次的子行。如果要拆成多个子行，列表的第一项`必须`要放在下一行，并且每行`必须`只有一个`接口(interface)`。

```php
<?php
namespace Vendor\Package;

use FooClass;
use BarClass as Bar;
use OtherVendor\OtherPackage\BazClass;

class ClassName extends ParentClass implements
    \ArrayAccess,
    \Countable,
    \Serializable
{
    // constants, properties, methods
}
```

#### 4.2 Using traits

The `use` keyword used inside the classes to implement traits MUST be
declared on the next line after the opening brace.

```php
<?php
namespace Vendor\Package;

use Vendor\Package\FirstTrait;

class ClassName
{
    use FirstTrait;
}
```

Each individual Trait that is imported into a class MUST be included 
one-per-line, and each inclusion MUST have its own `use` statement.

```php
<?php
namespace Vendor\Package;

use Vendor\Package\FirstTrait;
use Vendor\Package\SecondTrait;
use Vendor\Package\ThirdTrait;

class ClassName
{
    use FirstTrait;
    use SecondTrait;
    use ThirdTrait;
}
```

When the class has nothing after the `use` declaration, the class
closing brace MUST be on the next line after the `use` declaration.

```php
<?php
namespace Vendor\Package;

use Vendor\Package\FirstTrait;

class ClassName
{
    use FirstTrait;
}
```

Otherwise it MUST have a blank line after the `use` declaration.

```php
<?php
namespace Vendor\Package;

use Vendor\Package\FirstTrait;

class ClassName
{
    use FirstTrait;

    private $property;
}
```

#### 4.3 `属性(property)`

所有的`属性(property)`都`必须`声明其可见性。

`变量(var)`关键字`不可`用来声明一个`属性(property)`。

一条语句`不可`声明多个`属性(property)`。

`属性名(property name)` `不推荐`用单个下划线作为前缀来表明其`保护(protected)`或`私有(private)`的可见性。

一个`属性(property)`声明看起来应该像下面这样。

```php
<?php
namespace Vendor\Package;

class ClassName
{
    public $foo = null;
}
```

#### 4.4 `方法(method)`和`函数(function)`

所有的`方法(method)`都`必须`声明其可见性。

`方法名(method name)` `不推荐`用单个下划线作为前缀来表明其`保护(protected)`或`私有(private)`的可见性。

`方法名(method name)`在其声明后面`不可`有空格跟随。其左花括号`必须`放在下面自成一行，且右花括号`必须`放在方法主体的下面自成一行。左括号后面`不可`有空格，且右括号前面也`不可`有空格。

一个`方法(method)`声明看来应该像下面这样。 注意括号，逗号，空格和花括号的位置：

```php
<?php
namespace Vendor\Package;

class ClassName
{
    public function fooBarBaz($arg1, &$arg2, $arg3 = [])
    {
        // method body
    }
}
```

一个`函数(function)`声明看来应该像下面这样。 注意括号，逗号，空格和花括号的位置：

```php
<?php

function fooBarBaz($arg1, &$arg2, $arg3 = [])
{
    // function body
}
```

#### 4.5 `方法(method)`和`函数(function)`的参数

在参数列表中，逗号之前`不可`有空格，而逗号之后则`必须`要有一个空格。

`方法(method)`中有默认值的参数必须放在参数列表的最后面。

`方法(method)`和`函数(function)`的参数的标量类型声明`必须`小写。

```php
<?php
namespace Vendor\Package;

class ClassName
{
    public function foo(int $arg1, &$arg2, $arg3 = [])
    {
        // method body
    }
}
```

参数列表`可以`被拆分为多个缩进了一次的子行。如果要拆分成多个子行，参数列表的第一项`必须`放在下一行，并且每行`必须`只有一个参数。A single argument being
split across multiple lines (As might be the case with an anonymous function or
array) does not constitute splitting the argument list itself.

当参数列表被拆分成多个子行，右括号和左花括号之间`必须`又一个空格并且自成一行。

```php
<?php
namespace Vendor\Package;

class ClassName
{
    public function aVeryLongMethodName(
        ClassTypeHint $arg1,
        &$arg2,
        array $arg3 = []
    ) {
        // method body
    }
}
```

```php
<?php

somefunction($foo, $bar, [
  // ...
], $baz);

$app->get('/hello/{name}', function ($name) use ($app) {
    return 'Hello '.$app->escape($name);
});
```

When you have a return type declaration present there MUST be one space after
the colon with followed by the type declaration. The colon and declaration MUST be
on the same line as the argument list closing parentheses with no spaces between
the two characters. The declaration keyword (e.g. string) MUST be lowercase.

```php
<?php
declare(strict_types=1);

namespace Vendor\Package;

class ReturnTypeVariations
{
    public function functionName($arg1, $arg2): string
    {
        return 'foo';
    }
}
```

#### 4.6 `抽象(abstract)`，`终结(final)`和 `静态(static)`

当用到`抽象(abstract)`和`终结(final)`来做类声明时，它们`必须`放在可见性声明的前面。

而当用到`静态(static)`来做类声明时，则`必须`放在可见性声明的后面。

```php
<?php
namespace Vendor\Package;

abstract class ClassName
{
    protected static $foo;

    abstract protected function zim();

    final public static function bar()
    {
        // method body
    }
}
```

#### 4.7 调用方法和函数

调用一个方法或函数时，在方法名或者函数名和左括号之间`不可`有空格，左括号之后`不可`有空格，右括号之前也`不可`有空格。参数列表中，逗号之前`不可`有空格，逗号之后则`必须`有一个空格。

```php
<?php

bar();
$foo->bar($arg1);
Foo::bar($arg2, $arg3);
```

参数列表`可以`被拆分成多个缩进了一次的子行。如果拆分成子行，列表中的第一项`必须`放在下一行，并且每一行`必须`只能有一个参数。

```php
<?php

$foo->bar(
    $longArgument,
    $longerArgument,
    $muchLongerArgument
);
```

### 5. 控制结构

下面是对于控制结构代码风格的概括：

- 控制结构的关键词之后`必须`有一个空格。
- 控制结构的左括号之后`不可`有空格。
- 控制结构的右括号之前`不可`有空格。
- 控制结构的右括号和左花括号之间`必须`有一个空格。
- 控制结构的代码主体`必须`进行一次缩进。
- 控制结构的右花括号`必须`主体的下一行。

每个控制结构的代码主体`必须`被括在花括号里。这样可是使代码看上去更加标准化，并且加入新代码的时候还可以因此而减少引入错误的可能性。


#### 5.1 `if`，`elseif`，`else`

下面是一个`if`条件控制结构的示例，注意其中括号，空格和花括号的位置。同时注意`else`和`elseif`要和前一个条件控制结构的右花括号在同一行。

```php
<?php

if ($expr1) {
    // if body
} elseif ($expr2) {
    // elseif body
} else {
    // else body;
}
```

`推荐`用`elseif`来替代`else if`，以保持所有的条件控制关键字看起来像是一个单词。

#### 5.2 `switch`, `case`

下面是一个`switch`条件控制结构的示例，注意其中括号，空格和花括号的位置。`case`语句`必须`要缩进一级，而`break`关键字（或其他中止关键字）`必须`和`case`结构的代码主体在同一个缩进层级。如果一个有主体代码的`case`结构故意的继续向下执行则`必须`要有一个类似于`// no break`的注释。

```php
<?php

switch ($expr) {
    case 0:
        echo 'First case, with a break';
        break;
    case 1:
        echo 'Second case, which falls through';
        // no break
    case 2:
    case 3:
    case 4:
        echo 'Third case, return instead of break';
        return;
    default:
        echo 'Default case';
        break;
}
```


#### 5.3 `while`, `do while`

下面是一个`while`循环控制结构的示例，注意其中括号，空格和花括号的位置。

```php
<?php

while ($expr) {
    // structure body
}
```

下面是一个`do while`循环控制结构的示例，注意其中括号，空格和花括号的位置。

```php
<?php

do {
    // structure body;
} while ($expr);
```

#### 5.4 `for`

下面是一个`for`循环控制结构的示例，注意其中括号，空格和花括号的位置。

```php
<?php

for ($i = 0; $i < 10; $i++) {
    // for body
}
```

#### 5.5 `foreach`

下面是一个`for`循环控制结构的示例，注意其中括号，空格和花括号的位置。

```php
<?php

foreach ($iterable as $key => $value) {
    // foreach body
}
```

#### 5.6 `try`, `catch`, `finally`

下面是一个`try catch`异常处理控制结构的示例，注意其中括号，空格和花括号的位置。

```php
<?php

try {
    // try body
} catch (FirstThrowableType $e) {
    // catch body
} catch (OtherThrowableType $e) {
    // catch body
} finally {
    // finally body
}
```

### 6. 操作符

所有的二元和三元运算符前后必须有一个空，字符串连接符除外。包括所有的[算术运算符](http://php.net/manual/en/language.operators.arithmetic.php),
[比较运算符](http://php.net/manual/en/language.operators.comparison.php), [赋值运算符](http://php.net/manual/en/language.operators.assignment.php), [位运算符](http://php.net/manual/en/language.operators.bitwise.php), [逻辑运算符](http://php.net/manual/en/language.operators.logical.php) (除了 `!`)
和 [类型运算符](http://php.net/manual/en/language.operators.type.php).

Other operators such as string concatenation operators are left to interpetation.

```php
<?php

if ($a === $b) {
    $foo = $bar ?? $a ?? $b;
} elseif ($a > $b) {
    $variable = $foo ? 'foo' : 'bar';
}
```

### 7. 闭包

声明闭包时所用的`function`关键字之后`必须`要有一个空格，而`use`关键字的前后都要有一个空格。

闭包的左花括号`必须`跟其在同一行，而右花括号`必须`在闭包主体的下一行。

闭包的参数列表和变量列表的左括号后面`不可`有空格，右括号的前面也`不可`有空格。

闭包的参数列表和变量列表中逗号前面`不可`有空格，而逗号后面则`必须`有空格。

闭包的参数列表中带默认值的参数`必须`放在参数列表的结尾部分。

下面是一个闭包的示例。注意括号，空格和花括号的位置。

```php
<?php

$closureWithArgs = function ($arg1, $arg2) {
    // body
};

$closureWithArgsAndVars = function ($arg1, $arg2) use ($var1, $var2) {
    // body
};
```

参数列表和变量列表`可以`被拆分成多个缩进了一级的子行。如果要拆分成多个子行，列表中的第一项`必须`放在下一行，并且每一行`必须`只放一个参数或变量。

当列表（不管是参数还是变量）最终被拆分成多个子行，右括号和左花括号之间`必须`要有一个空格并且自成一行。

下面是一个参数列表和变量列表被拆分成多个子行的示例。

```php
<?php

$longArgs_noVars = function (
    $longArgument,
    $longerArgument,
    $muchLongerArgument
) {
   // body
};

$noArgs_longVars = function () use (
    $longVar1,
    $longerVar2,
    $muchLongerVar3
) {
   // body
};

$longArgs_longVars = function (
    $longArgument,
    $longerArgument,
    $muchLongerArgument
) use (
    $longVar1,
    $longerVar2,
    $muchLongerVar3
) {
   // body
};

$longArgs_shortVars = function (
    $longArgument,
    $longerArgument,
    $muchLongerArgument
) use ($var1) {
   // body
};

$shortArgs_longVars = function ($arg) use (
    $longVar1,
    $longerVar2,
    $muchLongerVar3
) {
   // body
};
```

把闭包作为一个参数在函数或者方法中调用时，依然要遵守上述规则。

```php
<?php

$foo->bar(
    $arg1,
    function ($arg2) use ($var1) {
        // body
    },
    $arg3
);
```

### 8. 匿名类

Anonymous Classes MUST follow the same guidelines and principles as closures
in the above section.


```php
<?php

$instance = new class {};
```

The opening bracket MAY be on the same line as the `class` keyword so long as
the list of `implements` interfaces does not wrap. If the list of interfaces
wraps, the bracket MUST be placed on the line immediately following the last
interface.

```php
<?php

// Bracket on the same line
$instance = new class extends \Foo implements \HandleableInterface {
    // Class content
};

// Bracket on the next line
$instance = new class extends \Foo implements
    \ArrayAccess,
    \Countable,
    \Serializable
{
    // Class content
};
```

[PSR-1]: http://www.php-fig.org/psr/psr-1/
[PSR-2]: http://www.php-fig.org/psr/psr-2/
[keywords]: http://php.net/manual/en/reserved.keywords.php
[arithmetic]: http://php.net/manual/en/language.operators.arithmetic.php
[assignment]: http://php.net/manual/en/language.operators.assignment.php
[comparison]: http://php.net/manual/en/language.operators.comparison.php
[bitwise]: http://php.net/manual/en/language.operators.bitwise.php
[logical]: http://php.net/manual/en/language.operators.logical.php
[type]: http://php.net/manual/en/language.operators.type.php

## 附录

### php-cs-fixer

[https://github.com/FriendsOfPHP/PHP-CS-Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer)

安装

```
composer.phar global require fabpot/php-cs-fixer
```

File > Settings > Tools > External Tools

![QQ截图20151226115156.jpg](https://ooo.0o0.ooo/2015/12/25/567e0f1881501.jpg)

`--level=psr2 --verbose fix "$FileDir$/$FileName$"`

`$ProjectFileDir$`

File > Settings > Keymap 设置快捷键

### 其他文档推荐

[PHP之道](http://www.phptherightway.com/)
[PHP设计模式](https://github.com/domnikl/DesignPatternsPHP)
[前端开发规范手册](http://zhibimo.com/read/Ashu/front-end-style-guide/)
[《SQL编程风格》](http://pan.baidu.com/share/link?shareid=1023640994&uk=3861181332)

### php-cs-fixer的一些fixer含义

* **encoding** [PSR-1]

源文件中php代码的编码格式`必须`只使用不带`字节顺序标记(BOM)`的`UTF-8`。

* **short_tag** [PSR-1]

PHP代码`必须`只使用`长标签(<?php ?>)`或者`短输出式标签(<?= ?>)`；而`不可`使用其他标签。

* **braces** [PSR-2]

`类(class)`的左花括号`必须`放到其声明下面自成一行，右花括号则`必须`放到类主体下面自成一行。

`方法(method)`的左花括号`必须`放到其声明下面自成一行，右花括号则`必须`放到方法主体的下一行。

控制结构的左花括号`必须`跟其放在同一行，右花括号`必须`放在该控制结构代码主体的下一行。控制结构的左括号之后`不可`有空格，右括号之前也`不可`有空格。

* **class_definition** [PSR-2]

在定义`类(class)`、`特性(trait)`和`接口(interface)`时，关键词左右`必须`有一个空格。

* **elseif** [PSR-2]

`推荐`用`elseif`来替代`else if`，以保持所有的条件控制关键字看起来像是一个单词。

* **eof_ending** [PSR-2]

所有PHP源文件`必须`以一个空行结束。

* **function_call_space** [PSR-2]

`函数(function)`的关键字的后面`不可`有空格。

* **function_declaration** [PSR-2]

声明闭包时所用的`function`关键字之后`必须`要有一个空格，而`use`关键字的前后都要有一个空格。

* **indentation** [PSR-2]
    
代码`必须`使用4个空格，且`不可`使用制表符来作为缩进。

> 注意：代码中只使用空格，且不和制表符混合使用，将会对避免代码差异，补丁，历史和注解中的一些问题有帮助。空格的使用还可以使通过调整细微的缩进来改进行间对齐变得更加的简单。

* **line_after_namespace** [PSR-2]
    
`命名空间(namespace)`的声明后面`必须`有一行空行。

* **linefeed** [PSR-2]

所有的PHP源文件`必须`使用Unix LF(换行)作为行结束符。

* **lowercase_constants** [PSR-2]

PHP常量`true`, `false`和`null` `必须`使用小写字母。

* **lowercase_keywords** [PSR-2]
    
PHP关键字([keywords](http://php.net/manual/en/reserved.keywords.php))`必须`使用小写字母。

* **method_argument_space** [PSR-2]
   
`方法(method)`的参数列表中，逗号之前`不可`有空格，而逗号之后则`必须`要有一个空格。

* **multiple_use** [PSR-2]

一句声明中，`必须`只有一个`导入(use)`关键字。

* **parenthesis** [PSR-2]
    
左括号之后`不可`有空格，右括号之前也`不可`有空格。

* **php_closing_tag** [PSR-2]
    
纯PHP代码源文件的关闭标签`?>` `必须`省略。

* **single_line_after_imports** [PSR-2]

所有的`导入(use)`声明`必须`放在`命名空间(namespace)`声明的下面。

在`导入(use)`声明代码块后面`必须`有一行空行。

* **switch_case_space** [PSR-2]

`case`和值之间`必须`只有一个空格。

* **trailing_spaces** [PSR-2]
 
在非空行后面`不可`有空格。

* **visibility** [PSR-2]

所有的`属性(property)`和`方法(method)`都`必须`声明其可见性。

`属性名(property name)`和`方法名(method name)` `不推荐`用单个下划线作为前缀来表明其`保护(protected)`或`私有(private)`的可见性。

当用到`抽象(abstract)`和`终结(final)`来做类声明时，它们`必须`放在可见性声明的前面。

而当用到`静态(static)`来做类声明时，则`必须`放在可见性声明的后面。