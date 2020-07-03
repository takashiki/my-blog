+++
title= "Windows 安装 Xshell 失败修复方法"
draft = false
date= "2017-10-20 09:35:46"
+++

参考资料：

[xshell5老是出现安装程序组件错误，好心人帮忙解决下](http://bbs.csdn.net/topics/391959404)
[xshell 安装过卸载了，然后再安装的时候报错 -1605错误](https://tieba.baidu.com/p/4610927590)

遇到的问题是在新装的 Win7 系统上安装 Xshell 时，安装到快结束那步提示 “安装程序集组件{...}时出错”，然后重新运行安装程序无论选哪个选项都提示 “此操作只对目前安装的产品有效”。

解决方法如下：

到 C:\Program Files (x86)\InstallShield Installation Information
这个目录下，删了这个文件夹 {F3FDFD5A-A201-407B-887F-399484764ECA}

将以下命令保存为 bat 文件并以管理员身份运行

```cmd
sc config wuauserv start= auto
sc config bits start= auto
sc config DcomLaunch start= auto
net stop wuauserv
net start wuauserv
net stop bits
net start bits
net start DcomLaunch 
```

然后重新运行 Xshell 的安装包，注意语言不要选择简体中文

这样如果不出意外即可成功安装，Xftp 等遇到类似问题也可以按照同样的方法解决。