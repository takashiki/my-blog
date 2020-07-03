+++
title= "博客迁移至Vultr并启用https"
draft = false
date= "2016-04-02 12:23:00"
+++

SAE现在开始对应用和共享型MyQL收费了，如果应用数比较多，使用SAE的性价比就很低了，于是便重新开始把自己的站点迁移到vps上。之前也试用了很多家的vps，详见[http://blog.skyx.in/category/VPS/](http://blog.skyx.in/category/VPS/)，最终还是决定使用[Vultr](http://www.vultr.com/?ref=6875759)东京节点，原因主要有几个，一个是vultr最低价套餐的内存较大一些，一个是vultr东京通过[微林](https://vnet.link/?rc=17569)中转速度不错（cn3、cn4、hk1的节点都可以），一个是vultr现在有免费的快照，备份方便。

站点的迁移本身没什么好说的，为了方便部署，我自己写了一个简单的基于git@osc的webhook的[部署脚本](http://blog.skyx.in/archives/158/)。

迁移至vps后终于可以开启https了，我用的是let's encrypt的免费证书，使用的脚本为[https://github.com/Neilpang/le](https://github.com/Neilpang/le)，这个脚本十分傻瓜化，可以非常简单地完成证书的申请和更新。

cdn我使用的是[又拍云](https://www.upyun.com/)，加入[又拍云联盟](https://www.upyun.com/zh/league.html)，也即在自己的网站上放上又拍云的图标和链接，就可以享受每月15G流量的免费额度，个人博客足够使用了，使用过程详见[http://blog.skyx.in/archives/202/](http://blog.skyx.in/archives/202/)。

唯一有点遗憾的是原本使用的评论系统畅言因为不支持https不能使用了，多说被收购后半死不活的，而disqus在国内的大环境也并不十分好用，于是换回了typecho的原生评论。

最终效果参见本博客和[https://skyx.in/](https://skyx.in/)。



