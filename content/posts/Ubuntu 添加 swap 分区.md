+++
title= "Ubuntu 添加 swap 分区"
draft = false
date= "2018-05-14 11:19:33"
+++

前段时间上车了腾讯云 360 买三年多的学生机的活动，加上降配总共获得 6 年，然而内存降到 1G 后，跑个 mysql 时间长了内存都不够。而且腾讯云的 ubuntu 不知道什么原因 1G 内存实际只有 800+M，更加雪上加霜。

终于前两天服务器由于内存爆了而又没有开 swap 崩了，几乎死机状态，ssh 都连不上，控制台强制重启才恢复正常。为了防止再次出现这种情况，我就给服务器加了个 swap。

参考文档：[https://askubuntu.com/questions/33697/how-do-i-add-a-swap-partition-after-system-installation/796997#796997](https://askubuntu.com/questions/33697/how-do-i-add-a-swap-partition-after-system-installation/796997#796997)

具体步骤和命令如下：

```shell
# 创建一个空文件，具体大小的话对于小内存机器建议为内存的两倍 (例子中 1K * 4M = 4 GiB).
sudo mkdir -v /var/cache/swap
cd /var/cache/swap
sudo dd if=/dev/zero of=swapfile bs=1K count=4M
sudo chmod 600 swapfile

# 将新建的文件转换为 swap 文件.
sudo mkswap swapfile

# 开启 swap.

sudo swapon swapfile

# 通过 swapon 或者 top 命令进行验证:
swapon -s
# 或者
top -bn1 | grep -i swap
# 会显示类似信息: KiB Swap:  4194300 total,  4194300 free

# 禁用 swap 时可以使用 sudo swapoff swapfile.

# 将该分区设置成开机加载.
echo "/var/cache/swap/swapfile none swap sw 0 0" | sudo tee -a /etc/fstab

# 测试开机加载:
sudo swapoff swapfile
sudo swapon -va
```