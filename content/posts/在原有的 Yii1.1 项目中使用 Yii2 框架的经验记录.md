+++
title= "在原有的 Yii1.1 项目中使用 Yii2 框架的经验记录"
draft = false
date= "2017-09-07 14:25:14"
+++

目前公司由于历史原因，之前很多主体项目都是使用 Yii1.1 开发的，Yii1.1 在使用上还是有很多不便，为了使用 Yii2 的一些新特性，我决定在一个规模比较小的项目上尝试 Yii1.1 和 Yii2 共存并逐渐使用 Yii2 替代原有 Yii1.1 代码进行项目升级的方案。

主要的参考文档在 google 上搜了下就只有官方文档的一节 [Using Yii 2 with Yii 1 ](http://www.yiiframework.com/doc-2.0/guide-tutorial-yii-integration.html#using-both-yii2-yii1)。

最主要的是创建一个自定义的 Yii 类文件，这个类继承自 Yii2 的 BaseYii 类，而类里面需要手工把 Yii1.1 的 YiiBase 类中的代码复制过来，这样这个类就同时拥有 Yii1.1 和 Yii2 的属性和方法了。
然后最下面三行是为了能在项目中使用 Yii2 的自动加载机制和依赖注入容器，一定不能写错。

```php
$yii2path = '/path/to/yii2';
require($yii2path . '/BaseYii.php'); // Yii 2.x

$yii1path = '/path/to/yii1';
require($yii1path . '/YiiBase.php'); // Yii 1.x

class Yii extends \yii\BaseYii
{
    // 这里要把 Yii1.1 中 YiiBase 类里的代码全部复制过来
}

Yii::$classMap = include($yii2path . '/classes.php');
// 通过 Yii1.1 的方法注册 Yii2 的自动加载器
Yii::registerAutoloader(['yii\BaseYii', 'autoload']);
// 创建依赖注入容器
Yii::$container = new yii\di\Container();
```

这个文件我们可以放在 `components\Yii.php`，然后我们就需要修改项目原先的 `index.php` 入口文件了，修改过后的关键代码如下：

```php
// 引入上一步创建好的自定义 Yii 类文件
require(__DIR__ . '/../components/Yii.php');

// 首先读取 Yii2 的配置，实际配置可能更多，这里只是参考
$yii2Config = require(__DIR__ . '/../config/yii2/web.php');
// 不要调用 run() 方法，Yii2 只作为服务定位器使用
new yii\web\Application($yii2Config);

// 读取 Yii1.1 配置，实例化 Application 并运行
$yii1Config = require(__DIR__ . '/../config/yii1/main.php');
Yii::createWebApplication($yii1Config)->run();
```

配好这些就可以开始使用了，项目的目录组织的话可以根据实际项目情况而定，在编写 Yii2 代码时，我们可以无视原来的 Yii1.1 的所有代码，将项目作为一个常规的 Yii2 项目来看，这样的话目录结构就很清晰了。

这种方案要求 php 版本至少在 `5.4` 以上，我建议将 Yii1.1 的框架版本升级到最新的 `1.1.19` 这个版本可以支持 php7.0 和 php7.1。

总的来说并不困难，不过参考资料较少，实际使用过程中可能会遇到坑点，不过也都比较好解决，老项目这样一配可以说是枯木逢春，写起新功能来要舒服太多了。