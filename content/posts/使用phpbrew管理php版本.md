+++
title= "使用phpbrew管理php版本"
draft = false
date= "2016-10-09 13:50:26"
+++

参考文档：[http://rmingwang.com/php-version-management-phpenv.html](http://rmingwang.com/php-version-management-phpenv.html)

安装

```shell
curl -L -O https://github.com/phpbrew/phpbrew/raw/master/phpbrew
chmod +x phpbrew
sudo mv phpbrew /usr/bin/phpbrew
```

初始化

```shell
phpbrew init

sudo vim ~/.bashrc
#文件最后,插入下面这行代码
source ~/.phpbrew/bashrc
```

安装php版本

```shell
phpbrew known

phpbrew install 7.0.11 +default +fpm +pdo +mysql +sqlite +gd
```

初步用下来感觉不是特别好用，建议使用docker。