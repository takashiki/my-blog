+++
title= "WSL2 使用体验"
draft = false
date= "2020-04-16 11:39:55"
+++

去年全面转向 Windows 设备之后，为了追求更友好的开发体验，我就开始尝试了还处在 Preview 阶段的 WSL2。到现在 Win10 2004 中 WSL2 全面可用，我也算重度使用了快半年了。

作为一个被 WSL 一代伤过的人，一开始对于 WSL2 其实也没有抱太高的预期，也正因为如此，微软在 WSL2 上下的功夫倒是给了我不少惊喜，而且这半年的时间能明显感觉到 WSL2 在变得越来越好用。

WSL2  最核心的变化，自然是这一代使用了跑在虚拟机中的完整 Linux，在各方面和原生的 Linux 区别已经很少了（具体见参考链接），可以支持更底层的应用，也不需要为了兼容性做各种 trick，这也使得 Windows 版的 Docker 在代码改动量很少的情况下就支持了使用 WSL2 做 backend。

在性能方面 WSL2 也有着大幅的提升，降低了进程启动的开销，本地文件系统的读写能力也大大提高，可以充分享受高性能 SSD 的爽快感。不过 /mnt 下挂载的 Windows 磁盘因为改成通过网络协议进行交互，所以读写性能反而下降了，尤其是在大量小文件读写比如使用 git 或者较重的 web 框架的情况下，慢到简直怀疑人生。

不过 /mnt 磁盘性能慢的问题基本是可以规避掉的，所有的项目开发都放在 WSL2 本地盘就好了。现在 VS Code 和 JetBrains 家的 IDE 对 WSL2 的支持都不错，不仅项目的打开和管理没什么区别，而且如果把这两者的 Terminal 换成 WSL 的话，更是如同直接在使用 Linux。

这种顺滑的体验也要归功于微软在 WSL2 与 Win10 系统集成度上的打磨。现在 Win10 在文件目录下按住 Shift 时弹出的右键菜单中直接就有“在此处打开 Linux Shell”选项，这在去年早期的时候还是没有的。而接下来的一个预览版里更是会加入直接在 Windows 资源管理器中访问 WSL 文件系统的功能。

另外通过配置可以让 WSL 挂载的 Windows 文件系统在 WSL 里面不再全都是 777 的权限，这也进一步降低了在 Win10 当中 Windows 和 WSL 两者的割裂感。你们可能不知道让用户能在 Windows 上拥有 Linux 的开发体验是什么概念，我们一般只会用两个字来形容这种公司：巨硬！

虽然 WSL2 现在还是存在一些问题，比如和部分代理软件会有冲突、挂载磁盘性能低等，不过鉴于整体体验已经很棒了，还是应该给巨硬倒一杯卡布奇诺。

参考：

- [Installation Instructions for WSL 2](https://docs.microsoft.com/en-us/windows/wsl/wsl2-install)
- [没忍住，还是上了 wsl2 的车，说下体验](https://www.v2ex.com/t/588377)
- [WSL 使用中遇到的问题及解决方案 #2 - DrvFs 文件系统权限问题](https://p3terx.com/archives/problems-and-solutions-encountered-in-wsl-use-2.html)
- [WSL 和 WSL2 简单对比](http://www.mocihan.ml/archives/267/)