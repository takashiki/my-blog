+++
title= "Git提交文件时肉眼看不出变化的文件状态却为被修改的可能原因"
draft = false
date= "2016-03-15 09:44:47"
+++

### 文件的换行符改变

在Windows上最容易出现这种问题，由于*nix系统的换行符为`LF(\n)`，而Windows的换行符为`CRLF(\r\n)`，所以在Windows上的默认配置的Git会在`git pull`时将`LF`换行符换为`CRLF`，而`git push`时会再将换行符换回去。然而，当文件中含有中文时Git的这个功能会出现问题，pull时能正常转换，push时却无法正常执行，这时就会出现文件比对时整个文件内容都改变了，但肉眼却无法看出。

解决方法很简单，直接执行以下命令进行全局配置就可以了：

```shell
git config --global core.autocrlf false
```

更详细的内容可以看这篇博客：[http://blog.jobbole.com/46200/](http://blog.jobbole.com/46200/)。

### 文件模式的改变

有的时候我们可能会对项目文件进行chmod操作或者在转移项目文件的过程中无意地改变了文件的模式，这时候文件状态也会变成被修改，但diff也没什么不同的地方。