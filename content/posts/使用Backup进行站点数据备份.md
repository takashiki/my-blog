+++
title= "使用Backup进行站点数据备份"
draft = false
date= "2016-01-28 20:38:00"
+++

[Backup](https://github.com/backup/backup)是一个使用ruby编写的多功能备份工具，加上一个支持七牛的扩展[backup2qiniu](https://github.com/lidaobing/backup2qiniu)，我们就可以很方便地将站点数据备份到七牛上。

首先系统上需要安装ruby，ubuntu上可以

```shell
apt-get install ruby ruby-dev
```

在centos上则是：

```shell
yum install ruby ruby-devel
```

然后安装backup和其扩展backup2qiniu：

```shell
gem install backup
gem install backup2qiniu
```

安装完成后创建配置文件：

```shell
backup generate:config
backup generate:model --trigger=backup2qiniu
```

修改 ~/Backup/models/backup2qiniu.rb 内容如下，注意修改其中的配置项：

```ruby
require 'rubygems'
gem 'backup2qiniu'
require 'backup2qiniu'

Backup::Model.new(:backup2qiniu, 'backup vps data to qiniu') do
  database MySQL do |db|
    db.name = 'xxx'
    db.username = 'root'
    db.password = 'xxx'
    db.host = 'localhost'
    db.port = 3306
    db.socket = '/tmp/mysql.sock'
  end

  archive :web do |archive|
    archive.use_sudo
    archive.root '/data'
    archive.add 'wwwroot/web'
    archive.exclude 'wwwroot/web/vendor'
  end

  compress_with Gzip

  store_with Qiniu do |q|
    q.keep = 7
    q.access_key = 'xxx'
    q.access_secret = 'xxx'
    q.bucket = 'xxx'
    q.path = 'xxx'
  end
end
```

使用如下命令即可触发备份
```shell
backup perform -t backup2qiniu
```
