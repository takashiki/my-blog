+++
title= "Vultr忘记root密码重置方法及多备份安装脚本报unzip不存在解决方法"
draft = false
date= "2016-01-18 13:48:00"
+++

Vultr如果忘记了root密码，可以通过进入单用户模式重置密码，这是官方的教程链接： [https://www.vultr.com/docs/boot-into-single-user-mode-reset-root-password](https://www.vultr.com/docs/boot-into-single-user-mode-reset-root-password)。

对于Ubuntu流程如下：

 1. 点击`View Console`然后发送`CTRL+ALT+DEL`重启服务器，
 2. 重启时点击`ESC`键进入GRUB启动选项，
 3. 按`e`键来编辑第一个启动选项，
 4. 在以"linux /boot/"开通的那一行结尾加上`init="/bin/bash"`
 5. 按`F10`或`CTRL-X`启动
 6. 输入`mount -rw -o remount /`后使用passwd重置root密码，然后再重启就好了

在使用多备份的时候，遇到一个蛋疼的问题，就是明明安装了unzip，但是却报unzip未安装，这时候只要直接去掉下载下来的sh文件里的这一段验证脚本就行了。