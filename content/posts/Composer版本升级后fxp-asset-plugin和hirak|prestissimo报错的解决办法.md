+++
title= "Composer版本升级后fxp-asset-plugin和hirak/prestissimo报错的解决办法"
draft = false
date= "2016-05-26 20:26:04"
+++

首先卸载并重新安装`hirak/prestissimo`：

```shell
composer global remove hirak/prestissimo  --no-plugins
composer global require hirak/prestissimo  --no-plugins
```

然后更新`fxp/composer-asset-plugin`：

```php
composer global update fxp/composer-asset-plugin --no-plugins
```