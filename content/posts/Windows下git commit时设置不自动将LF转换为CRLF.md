+++
title= "Windows下git commit时设置不自动将LF转换为CRLF"
draft = false
date= "2016-01-22 16:39:00"
+++

在php的psr规范中规定了文件中的换行符必须为LF（linefeed - 换行）而不能是CRLF（carriage return - 回车，linefeed - 换行），在phpstorm中我们可以在 File > Settings > Editor > Code Style 中设置换行符（Line Separator）为LF。

但是在git提交代码时会报如下警告信息：

```
LF will be replaced by CRLF
```

也即window上git会自动将LF替换为CRLF解决方法为：
```
git config --global core.autocrlf false
```