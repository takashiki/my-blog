+++
title= "使用mkdocs生成项目文档静态站点"
draft = false
date= "2016-04-23 14:54:00"
+++

[mkdocs](http://www.mkdocs.org/)是一个使用python写的将markdown文档生成静态站点的工具，用mkdocs来生成项目文档是十分方便的。

这是它的[中文文档](http://markdown-docs-zh.readthedocs.org/zh_CN/latest/)。

安装mkdocs首先要安装python和pip，这里就不多说了。

```shell
pip install mkdocs

mkdocs new docs-center

cd docs-center

mkdocs serve --dev-addr 192.168.0.0:8000
```

参考文章：[http://www.wwjie.cn/archives/259](http://www.wwjie.cn/archives/259)