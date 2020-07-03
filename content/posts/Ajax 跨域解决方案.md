+++
title= "Ajax 跨域解决方案"
draft = false
date= "2018-01-11 18:56:00"
+++

### document.domain

该方案只能适用于跨子域的情况，无法跨不同二级域名。

### window.name

利用同一窗口打开的所有 frame 共享同一个 window.name 来传递数据，只能传递字符串。

### jsonp

比较常见的一种跨域解决方案，利用 &lt;script&gt; 标签可以跨域的特性实现 ajax 请求跨域。

### 服务端设置 CORS 头

这种方式多见于上传文件的服务器，比如图床、云存储等。

### 代理请求

一般前端开发人员使用 node 进行代理比较方便，也可以用 php 等，也可以直接用 nginx 做反代。

### postMessage

这个 html5 中新增的 api 非常强大，不仅可以用作跨域，最重要的是还能实现跨窗口消息传递，现在很多 h5 游戏平台都是用这个 api 来实现自己的 js sdk 来和 cp 进行对接的。

参考文档：

- [ajax跨域，这应该是最全的解决方案了](https://segmentfault.com/a/1190000012469713)
- [Web开发之跨域与跨域资源共享](http://www.devsai.com/2016/11/24/talk-CORS/)
- [跨域资源共享 CORS 详解](www.ruanyifeng.com/blog/2016/04/cors.html)