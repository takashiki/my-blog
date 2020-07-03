+++
title= "PHP项目开发实践总结内部分享大纲"
draft = false
date= "2016-12-15 11:44:00"
+++

### 项目部署相关

- 项目命名： 域名中 `.` 替换为 `_`，如： `app.domain.com` 项目名为 `app_domain_com`。关于分支，`deploy`分支用于部署到正式环境，如有测试环境的需要可以添加`test`分支，如果测试环境对稳定性有需求的话可以开`develop`分支，如果是多人协作的项目中有周期较长的功能模块需要开发则可以单独新开分支。
- 所有在上线时需要忽略的文件都写到`.gitignore`里，这样运维在配置发布系统时也比较方便
- 如果开启了 opcache，则每次新代码上线之后都需要清空 opcache 缓存（`service php-fpm reload` 或者通过调用cgi的opcache），否则上线后没有效果。
- 如果在`composer.json`中添加了自定义的自动加载项，如使用了git subtree的情况下，每次上线后可能都需要重新 `composer dump-autoload` 一遍。该问题可复现，但具体出现原因不明
- 服务器若仅有内网，外网是通过proxy进行访问的情况下需注意代码的行为可能会和预期的不一致（主要curl等操作）
- 服务器在使用了内网`namedserver`的情况下，如果 nginx 使用`unix socket`的方式调用`php-fpm`的话，可能不生效

### 性能优化相关

- php7（php 各版本新特性的分享中提到过 php7 的性能对照）
- opcache（开启了 opcache 的 php7 才能展现出真正的高性能）
- composer dump-autoload -o （能一定程度上提升第三方库的加载效率，尤其是在未开启 opcache 的情况下）
- 项目配置（如主要提供 api 的项目可以关闭 session 以提升性能）
- redis/memcache缓存（尤其适用于查询接口较多的项目，性能提升明显）

### 静态资源部署

- protocol relative url（方便地切换 http 和 https）
- 版本号（日期时间序列或hash）
- 静态资源域名采用特定的静态资源域名，防止 cookie 过大对加载时间造成影响
- 浏览器对相同域名的并发连接数限制，一般浏览器是6个，http2是一个服务器一个连接而不是一个资源一个连接所以对于复杂页面性能提升很大，http2的硬性要求是https

### 编码风格相关

- php-cs-fixer用法，已分享
- phpstorm自带代码风格检查设置，Settings > Editor > Code Style > PHP > Set from...，快捷键（windows Ctrl + Alt + L）

### 数据库设计相关

- 数据一致性要求不严格的场景下不要使用外键、unique等，在代码中进行逻辑控制，这一点在快速迭代的项目中尤其适用
- 联合索引的第一列如果不能将范围缩至六分之一（具体数字记不得了）以内则会全表扫描
- 数据库字符集utf8mb4加索引时需注意varchar类型的长度，mysql索引长度最多1000字节，varchar类型默认长度255，utf8mb4的情况下最多占用1020字节超出限制，migration运行会报错
- collate中unicode_ci和general_ci的注意点，查询时的相等判定（`1`和`①`，`A`和`À`）
- 表名和字段名无特殊含义或专有名词的情况下建议使用单数形式，如：user、game
- 所有资源类的数据表都可能会需要如下字段：
created_at、created_by、updated_at、updated_by，这些字段在yii2的model中可以通过
TimestampBehavior、BlameableBehavior进行自动控制。
status字段表示软删除，引用SoftDeleteTrait即可

- 表示与其他表id字段进行关联的字段建议命名为：表名_id，如：user_id、category_id，代码中对id的命名也建议采用如：\$user_id，$userId 之类的方式避免产生混淆
- 需要与其他表进行关联的字段添加索引时，两表中的对应字段类型应保持一致

### composer相关

- 使用国内镜像进行加速，[http://pkg.phpcomposer.com/](http://pkg.phpcomposer.com/)
- composer根目录路径不要有中文（windows环境上），否则会出现一些问题。修改composer默认根目录可以通过设置`COMPOSER_HOME`实现
- composer.json中常见配置字段含义和作用讲解，composer.lock文件的作用讲解(minimum-stability、require版本通配符、require-dev、autoload、scripts、extra)

### yii2框架相关

- 何时采用basic模板何时采用advanced模板，在session分离并且数据互通的情况下应采用多应用端的advanced模板结构，若session互通则使用basic模板分模块进行开发
- Model中rules、behaviors、scenarios作用和相互之间的联系
- Model中的relations使用
- Components的编写和使用（https://github.com/takashiki/yii2-ide-helper）
- Controller中responseFormat的使用
- ActiveQuery中使用`->limit(1)->one()`来提升性能

### 设计模式相关

- 工厂模式，在有完善的依赖注入框架的情况下使用场景较少
- 单列模式，维护配置文件、数据字典等仍会经常用到
- 策略模式（框架的缓存实现）
- 适配器模式（不同游戏的进入游戏加币等）

### 学习相关

最快的提升方式就是去看别人的优质代码：

[https://github.com/trending](https://github.com/trending)
[https://github.com/ziadoz/awesome-php](https://github.com/ziadoz/awesome-php)
[http://www.phptherightway.com/](http://www.phptherightway.com/)
[https://github.com/domnikl/DesignPatternsPHP](https://github.com/domnikl/DesignPatternsPHP)
[http://www.digpage.com/](http://www.digpage.com/)
[https://github.com/samdark/yii2-cookbook](https://github.com/samdark/yii2-cookbook)
[https://github.com/forecho/awesome-yii2](https://github.com/forecho/awesome-yii2)
[http://www.yiichina.com/](http://www.yiichina.com/)
[https://getyii.com/](https://getyii.com/)
[http://laravelacademy.org/](http://laravelacademy.org/)
[https://laravel-china.org/](https://laravel-china.org/)
[http://www.laruence.com/](http://www.laruence.com/)

PHP基础的提升则要多看官方手册：
[http://php.net/](http://php.net/)

建议多看英文文档，英文文档在即时性、准确性和详细程度上一般都有优势，PHP官方文档也是如此，比如：
[http://php.net/manual/en/function.serialize.php](http://php.net/manual/en/function.serialize.php)
[http://php.net/manual/zh/function.serialize.php](http://php.net/manual/zh/function.serialize.php)
