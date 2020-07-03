+++
title= "分享一个自写的Yii2扩展——Yii2 IDE Helper"
draft = false
date= "2016-11-23 09:21:29"
+++

虽然github上已经有了几个yii2的ide helper，如：https://github.com/iiifx-production/yii2-autocomplete-helper，不过自己使用下来感觉不是特别好用，于是便自己实现了一个：https://github.com/takashiki/yii2-ide-helper。

使用说明：

### 安装

用以下命令添加 composer 依赖:

```
composer require mis/yii2-ide-helper --dev
```

或者在 composer.json 文件的 `require-dev` 中添加如下内容后执行 `composer update`

```
"mis/yii2-ide-helper": "*"
```

### 使用

把如下配置加入应用的 console 配置文件中：

```php
'bootstrap' => ['log', 'ideHelper'],
...
'components' => [
    'ideHelper' => [
      	'class' => 'Mis\IdeHelper\IdeHelper',
    ],
  ...
],
```

之后就可以通过如下命令生成 IDE Helper 文件了:

```
php yii ide-helper/generate
```

### 可选配置列表

```php
'ideHelper' => [
    'class' => 'Mis\IdeHelper\IdeHelper',
    'filename' => '_ide_helper',
    'format' => 'php',
    'rootDir' => dirname(__DIR__),
    'configFiles' => [
        'console/config/main.php',
        'console/config/main-local.php',
    ],
],
```

默认配置文件路径:

```php
protected $defaultConfigFiles = [
    'config/web.php',
    'config/main.php',
    'config/main-local.php',
    'common/config/main.php',
    'common/config/main-local.php',
    'frontend/config/main.php',
    'frontend/config/main-local.php',
    'backend/config/main.php',
    'backend/config/main-local.php',
];
```
