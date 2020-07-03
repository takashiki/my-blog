+++
title= "FinalSpeed使用感受"
draft = false
date= "2016-01-23 20:28:26"
+++

在FinalSpeed出现之前，给服务器加速的方案常见的有[锐速](http://www.serverspeeder.com/)和[net-speeder](https://github.com/snooda/net-speeder)等，但锐速对系统内核版本有要求，openvz的vps是用不了的，非openvz的也得是特定内核的少数linux发行版才可以支持。两者的优化效果我之前都有体验过，但都没有[finalspeed](https://github.com/d1sm/finalspeed)这么惊艳。

一开始让我使用FinalSpeed我是拒绝的，因为finalspeed需要客户端支持。然而今天折腾了一下发现效果真的是杠杠的，美国的vps在shell里敲命令再也不卡了，就是偶尔连接会断掉，但不是什么大问题。而且finalspeed的客户端端口映射还带来一个隐藏的好处就是服务器ip变化时只需要改下finalspeed里的服务器ip就好了，再也不用一个一个地改本地的ss、navicat、xshell里的服务器地址了，简直棒呆。