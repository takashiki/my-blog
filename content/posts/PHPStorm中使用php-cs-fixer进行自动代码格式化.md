+++
title= "PHPStorm中使用php-cs-fixer进行自动代码格式化"
draft = false
date= "2016-02-22 15:32:00"
+++

参考文档：[https://hackernoon.com/how-to-configure-phpstorm-to-use-php-cs-fixer-1844991e521f](https://hackernoon.com/how-to-configure-phpstorm-to-use-php-cs-fixer-1844991e521f)

[PHP-CS-Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer)是一款对php代码进行风格检查和自动格式化的工具，支持psr和symfony编码规范。

安装

```shell
composer global require fabpot/php-cs-fixer
```

在phpstorm的`File > Settings > Tools > External Tools`菜单内进行php-cs-fixer的配置：

![QQ截图20151226115156.jpg](https://ooo.0o0.ooo/2015/12/25/567e0f1881501.jpg)

`name`和`description`可自行填写

`program`需要填写php-cs-fixer的可执行文件地址，Windows上是`用户目录\Roaming\Composer\composer\vendor\bin\php-cs-fixer.bat`，linux和mac上是`~/.composer/vendor/bin/php-cs-fixer`

`parameters`填`--rules=@Symfony --verbose fix "$FileDir$/$FileName$"`，其中 `rules` 字段具体可以查看 php-cs-fixer 的官方文档，但是由于 Windows 的 cmd 有诸多限制，所以只能传入一些简单的规则，如果需要配置复杂规则建议使用配置文件来完成。

`working directory`填`$ProjectFileDir$`

插件配置好后，到 `File > Settings > Keymap` 设置快捷键，快捷键设置好后就可以找个文件试一试了。

