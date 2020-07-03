+++
title= "扩展未使用LVM的ext4格式的Linux分区"
draft = false
date= "2016-06-06 17:32:18"
+++

自用的虚拟机上磁盘空间不够了，在VMWare的配置里给虚拟机的硬盘又加了20G，但是原来的磁盘没有使用 LVM，又是 ext4 格式的分区。如果使用了 Logical Volume Manager（逻辑卷管理）的话，扩展起来就比较方便了，ext3 格式的话就可以直接用 parted 来扩展分区。

查看磁盘分区信息：

```shell
# 查看分区大小、是否使用了LVM
fdisk -l

# 查看分区格式
df -hT
```

对于未使用 LVM 的 ext4 格式的分区，我们只能先把这个分区删除，然后再创建新的分区，分区的删除操作并不会影响磁盘上的数据，操作完成后也不会造成数据的损失。

```shell
fdisk /dev/sda
# 使用d命令删除分区
# 使用n命令创建分区，还是选择 p-主分区
# 其他保持默认就可以
# w命令保存修改

reboot

resize2fs /dev/sda1
```

参考文章： [https://thewiringcloset.wordpress.com/2013/01/09/extending-a-root-filesystem-in-linux-without-lvm/](https://thewiringcloset.wordpress.com/2013/01/09/extending-a-root-filesystem-in-linux-without-lvm/)