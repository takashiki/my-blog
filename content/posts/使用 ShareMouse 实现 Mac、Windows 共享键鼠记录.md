+++
title= "使用 ShareMouse 实现 Mac、Windows 共享键鼠记录"
draft = false
date= "2018-07-23 21:51:58"
+++

在多台电脑间共享键鼠相对来说是个比较小众的需求，所以这方面的软件数量并不很多，其中最为有名的要数 [Synergy](https://symless.com/synergy) 了。Synergy 貌似最初是开源免费的，现在收费好像也逐渐提高了，不过它是一次性买断终身使用权的，其实也算比较实惠了。

之前用过一段时间 Synergy，整体来说体验也算还可以，但是长期使用时还是发现存在一些问题：

- 有 Server 和 Client 的区别，只能将 Server 的键鼠共享给 Client
- 配置相对较麻烦，需要自己手工添加 Screen，并且需要配置正确 Screen 的名字
- 有时在 Client 上操作会有延迟和卡顿
- 复制粘贴也不太稳定有时能用有时有点异常，比如粘贴出现乱码等
- 拖拽文件可以从 mac 拖到 Windows 但是反之可能有问题，并且 utf8 的文件名可能乱码以及文件夹的处理不够完善

因为存在比较多的问题，所以我一直没有将 Synergy 作为常规方案来日常使用。周末的时候突然发现 [ShareMouse](http://www.keyboard-and-mouse-sharing.com/) 这款软件，试用了一下发现它比起 Synergy 真的要强大很多，上面列出的 Synergy 的问题我一天体验下来基本都能解决，真的是十分完美了。

不过要说缺点的话也是有的，一个是相对来说比较贵，不过虽然 ShareMouse 的授权是按年卖的，但是我看官网说明是授权到期仍可使用，但是发布新版本之类的维护就享受不到了。另外 ShareMouse 除了默认的 BroadCast 方式连接各台电脑之外只支持通过具体的 ip 和 port 进行连接，这对于部分 ip 通过 dhcp 获取的网络环境的用户来说就不太方便了。

ShareMouse 和 Synergy 更多的评测可以参考这篇文章：[多机共享键鼠软件横向测评](http://blog.shrp.me/Multi-Computer-Mouse-and-Keyboard-sharing.html)，这篇文章评测了多款键鼠共享软件，包括微软自家出的针对 Windows 机器间的 Mouse without Borders，如果全部是 Windows 机器的话，用这个会更适合。

至于 ShareMouse 的安装和配置也十分简单，一般就是直接安装好安装包之后，同网段内的电脑启动服务后即可自动连接上，连接不上的话可以在 Settings > Clients 里手动添加。其他的配置基本看看描述也就大概知道是干嘛的了，另外值得一提的是在 mac 的客户端里已经可以配置按键映射了，这个也算是把之前的一个短板给补上了。