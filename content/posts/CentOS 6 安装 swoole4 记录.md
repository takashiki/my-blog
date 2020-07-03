+++
title= "CentOS 6 安装 swoole4 记录"
draft = false
date= "2018-10-10 15:57:28"
+++

首先需要将 gcc 的版本升级到 4.8，参考 [CentOS yum安装或者升级GCC到4.8](https://blog.csdn.net/ljxfblog/article/details/80119228)。

具体步骤如下：

```shell
# 下载源并进行 yum 安装
wget http://people.centos.org/tru/devtools-2/devtools-2.repo -O /etc/yum.repos.d/devtools-2.repo
yum install devtoolset-2-gcc devtoolset-2-binutils devtoolset-2-gcc-c++

# 替换系统默认软链至新版本位置
ln -s /opt/rh/devtoolset-2/root/usr/bin/gcc /usr/bin/gcc
ln -s /opt/rh/devtoolset-2/root/usr/bin/c++ /usr/bin/c++
ln -s /opt/rh/devtoolset-2/root/usr/bin/g++ /usr/bin/g++

# 查看当前版本
gcc --version
```

这一步可能遇到报错：

```
http://people.centos.org/tru/devtools-2/6Server/x86_64/RPMS/repodata/repomd.xml:` [Errno 14] PYCURL ERROR 22 - "The requested URL returned error: 404"
Trying other mirror.
Error: Cannot retrieve repository metadata (repomd.xml) for repository: testing-devtools-2-centos-6Server. Please verify its path and try again
```

可以通过修改 `/etc/yum.repos.d/devtools-2.repo` 中的路径解决，参考 [https://gist.github.com/giwa/b1fb1e44dc0a7d270881](https://gist.github.com/giwa/b1fb1e44dc0a7d270881)：

```
# 将
http://people.centos.org/tru/devtools-2/$releasever/$basearch/RPMS
# 修改为
http://people.centos.org/tru/devtools-2/6/x86_64/RPMS
```

再次执行第一步的 yum install 命令即可。

之后就可以正常编译安装 swoole4 了。