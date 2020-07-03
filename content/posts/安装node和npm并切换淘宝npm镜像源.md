+++
title= "安装node和npm并切换淘宝npm镜像源"
draft = false
date= "2016-02-22 15:12:00"
+++

目前在大多数linux发行版内使用默认的包管理器和源安装node的时候，所安装上的node和npm的版本都会比较低，不能符合很多新项目的需求，所以我们只有到node的官网下载所需版本的node源码进行编译安装。

编译安装完成之后执行以下命令将node和npm加入/usr/bin：

```shell
ln -s /usr/local/bin/node /usr/bin/node
ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/bin/npm
```

此时通过以下命令查看版本，判断是否已正确安装：

```shell
node --version
npm --version
```

npm官方源由于不可避免的原因比较慢，而淘宝对npm做了镜像，我们可以使用这个镜像来替换官方源。使用这个源的方式有很多，不过需要注意的是，直接npm全局安装cnpm的话是会出现问题的，这可能是因为淘宝的cnpm的版本和当前npm的版本相比落后较多造成的。

如果直接替换npm的源可以使用如下命令：

```shell
npm config set registry https://registry.npm.taobao.org
```
如果想使用cnpm，而不是直接替换npm的源，比较推荐的方式有两种，一种是在.bashrc结尾添加alias，退出后重新进入或`source .bashrc`后生效

```shell
alias cnpm="npm --registry=https://registry.npm.taobao.org \
  --cache=$HOME/.npm/.cache/cnpm \
  --disturl=https://npm.taobao.org/dist \
  --userconfig=$HOME/.cnpmrc"
```

另外一种是编辑.npmrc文件，在其中添加

```shell
registry =https://registry.npm.taobao.org
```

---

2018.03.14 更新：

现在可以通过 `nrm` 这个包来切换镜像，十分方便。

```shell
npm i -g nrm #全局安装 nrm
nrm ls #查看可以使用的镜像列表
nrm use taobao #使用淘宝镜像源
```
