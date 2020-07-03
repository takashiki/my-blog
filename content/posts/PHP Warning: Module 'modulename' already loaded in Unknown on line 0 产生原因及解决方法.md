+++
title= "PHP Warning: Module 'modulename' already loaded in Unknown on line 0 产生原因及解决方法"
draft = false
date= "2016-06-12 11:31:00"
+++

在以 cli 模式执行 PHP 脚本时，如果发现了如下的报错：

```shell
PHP Warning: Module 'modulename' already loaded in Unknown on line 0
```

那就说明该扩展在编译 PHP 时已经 enable 了，但是在 php.ini 中又写了动态调用该扩展的 so 文件。

这时候我们可以查看一下 phpinfo ：

```shell
php -i | grep 'modulename'
php -i | grep 'php.ini'
```

然后去对应的 php.ini 文件中去掉该扩展即可。