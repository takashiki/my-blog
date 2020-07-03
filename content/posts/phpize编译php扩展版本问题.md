+++
title= "phpize编译php扩展版本问题"
draft = false
date= "2015-08-24 15:17:00"
+++

今天在编译php的amqp扩展时遇到一个问题，就是加载扩展时php-fpm报出如下错误：

```shell
NOTICE: PHP message: PHP Warning:  PHP Startup: amqp: Unable to initialize module
Module compiled with module API=20121212
PHP    compiled with module API=20131226
These options need to match
 in Unknown on line 0

```

之前也遇到过类似的问题，原因是ubuntu自带了低版本的php，而我平时使用的php版本则为高版本的。

遇到这个情况也比较好解决，只要在编译命令里带上高版本phpize目录及php-config文件目录即可，对于我的情况即将命令改为类似以下形式：

```shell
/usr/local/php/bin/phpize && ./configure --with-amqp --with-php-config=/usr/local/php/bin/php-config && make && make install
```

注意编译之前需要删除上一次编译时make生成的文件，可能还要执行`phpize -clean`命令，否则即使修改了命令行中的路径也不会有效果。