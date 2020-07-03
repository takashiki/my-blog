+++
title= "新手学WEB开发杂记（六）——透明边框的实现"
draft = false
date= "2013-04-24 19:59:00"
+++

  现在网页布局中使用弹出层的十分多，jquery弹出层插件也一抓一大把，其中一部分弹出层有漂亮的透明边框，而透明边框的实现方法各不相同，主要有一下几类：
  一是将每一边的边框作为一个div来处理，设置背景色和透明度，一种方便些，直接在弹出层下方设置一个比弹出层大一圈的div，设置成透明。这两种都要添加额外的div和写相当多的css。
  实际上在css3中有一种方法是最简单的，即`#lightbox { background: white; border: 20px solid rgba(0,0,0,0.3); }` ， 但是这样写有一个问题，即弹出层背景色会一直扩散到边框上，所以在css中需加一条 `background-clip: padding-box; `
详见此文：http://www.yangzblog.com/DIV-CSS/transparentBorder.html 
 
 