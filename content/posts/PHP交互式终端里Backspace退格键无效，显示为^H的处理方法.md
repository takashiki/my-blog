+++
title= "PHP交互式终端里Backspace退格键无效，显示为^H的处理方法"
draft = false
date= "2016-07-07 11:28:00"
+++

参考链接：
- [http://stackoverflow.com/questions/28733733/arrow-keys-not-working-in-shell](http://stackoverflow.com/questions/28733733/arrow-keys-not-working-in-shell)
- [http://unix.stackexchange.com/questions/43103/backspace-tab-not-working-in-terminal-using-ssh](http://unix.stackexchange.com/questions/43103/backspace-tab-not-working-in-terminal-using-ssh)

如果使用 PHP 的交互式命令行（如：laravel 的 tinker）时出现类似的问题可使用如下命令：

```sehll
rlwrap php artisan tinker
```

其他情况可以尝试使用以下命令，注意其中 `^H` 不是直接输入，而是通过 `Ctrl - v` + `Backspace` 输入的：

```shell
stty erase ^H
```