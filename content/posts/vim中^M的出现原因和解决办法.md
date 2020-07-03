+++
title= "vim中^M的出现原因和解决办法"
draft = false
date= "2016-01-27 10:57:00"
+++

vim中会出现^M是因为，在Windows中文件的换行符是\r\n（CRLF，回车换行），而linux中是\n（LF，换行），所以Windows下编辑的文件到了linux中每行都会多出一个\r。

解决的方法也很简单，就是批量替换，`:%s/\r//g`。

或者直接使用`dos2unix`工具，该工具在常见的linux发行版上都可以通过包管理工具安装。