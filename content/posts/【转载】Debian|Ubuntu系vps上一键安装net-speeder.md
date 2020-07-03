+++
title= "【转载】Debian/Ubuntu系vps上一键安装net-speeder"
draft = false
date= "2015-07-17 21:47:00"
+++

> 全文转载自 [http://www.tennfy.com/3495.html](http://www.tennfy.com/3495.html)。 

> **小尾巴** 通过[该链接](https://www.conoha.jp/referral/?token=mrBOqqw4yzeJSyoPloAjAim8mQQPBp6XY5E8lx4ir2hW.K81KX4-49S)注册conoha后充值500日元以上可获得1000日元优惠券。

tennfy之前在[Linode debian系统下安装锐速教程](http://www.tennfy.com/3134.html)一文中介绍过锐速，锐速使用效果确实非常好，可以有效的提升本地到VPS的连接速度。但是，锐速在KVM或XEN VPS中方可使用，对于众多OPENVZ vps用户来说未免有些遗憾。本文就来介绍一下锐速在OPENVZ vps环境下的替代品–net-speeder。

## net-speeder介绍

---

net-speeder是一款与锐速类似的TCP加速程序，且具有锐速不具备的优势：可以用于OPENVZ虚拟化的vps中。但是，相对于锐速可以通过丢包判断及预测、准确估算路径带宽等方式智能发包，net-speeder采用了更为简单粗暴的方式，强制双倍发包。这样的做法有利有弊，优点在高延迟不稳定链路上（如电信到美国VPS）可以有效的降低丢包率，但是双倍发包就意味着耗费双倍流量，对于VPS流量有限的朋友来说需要慎重。

net-speeder github项目地址：[https://github.com/snooda/net-speeder](https://github.com/snooda/net-speeder)

## net-speeder的安装及使用

---

### net-speeder的安装

登入VPS后，下载net-speeder安装脚本

```shell
wget --no-check-certificate https://raw.githubusercontent.com/tennfy/debian_netspeeder_tennfy/master/debian_netspeeder_tennfy.sh
```

执行该脚本

```shell
chmod a+x debian_netspeeder_tennfy.sh
bash debian_netspeeder_tennfy.sh
```

### net-speeder的使用

脚本安装完成后，会自动运行net-speeder。可以通过如下命令查看net-speeder运行状态及停止net-speeder。

查看net-speeder是否运行

```shell
ps aux|grep net_speeder|grep -v grep
```

停止net-speeder

```shell
killall net_speeder
```

启动net-speeder（OPENVZ环境）

```shell
nohup /root/net_speeder venet0 "ip" >/dev/null 2>&1 &
```

## 设置net-speeder定时开关

---

net-speeder实际上是颇有争议的，双倍发包会导致网络拥堵，有点损人利己的感觉。因此，tennfy给出一个折中的方案，就是在晚上高峰期的时候开启net-speeder,空闲时间关闭。

### 1、设置时区

由于美国的VPS时区跟中国是不一致的，因此需要给VPS设置一下时区。
执行以下命令

```shell
echo "Asia/Shanghai" >/etc/timezone
```

输入date命令查看VPS上显示的时间是否与本地相同。

### 2、设置net-speeder定时开关

我们设定19点开启，24点关闭。执行以下命令：

```shell
echo '0 19 * * * root nohup /root/net_speeder venet0 "ip" >/dev/null 2>&1 &' >>/etc/crontab
echo "0 0 * * * root killall net_speeder" >>/etc/crontab
/etc/init.d/cron restart
```

## net-speeder注意事项

---

以下几种情况不适合使用net-speeder:
1、服务器流量较小，因为使用net-speeder会消耗双倍流量。
2、主要提供网页、图片等小文件访问。net-speeder对于下载大文件、代理访问视频网站等效果比较好，而对小文件加速效果不明显。
3、需要使用pptpd等不支持双倍发包的网络软件。net-speeder会造成这些软件无法正常使用。
4、如果线路本身很好，不存在延迟较大情况，使用net-speeder效果会适得其反。