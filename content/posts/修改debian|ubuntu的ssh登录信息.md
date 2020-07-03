+++
title= "修改debian/ubuntu的ssh登录信息"
draft = false
date= "2016-03-23 10:10:00"
+++

[https://nickcharlton.net/posts/debian-ubuntu-dynamic-motd.html](https://nickcharlton.net/posts/debian-ubuntu-dynamic-motd.html)

修改`/etc/update-motd.d/`内的文件，详见上述教程，修改后记得需要将该文件夹内的所有文件赋可执行权限，然后执行即可看到效果：

```shell
chmod +x /etc/update-motd.d/ -R
run-parts /etc/update-motd.d/
```

还有一个注意点就是，要将 `/etc/motd` 文件软链接到 `/var/run/motd`，要不然每次登陆时都不会有登录信息。