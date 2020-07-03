+++
title= "使用 fork 和 pull request 参与维护开源项目代码"
draft = false
date= "2018-10-29 17:49:39"
+++

### 与原项目代码保持同步

我们 fork 出的项目 clone 到本地之后，需要在本地项目的 remote 源中添加原项目的地址。

注意将 project-git-path 替换为实际路径，其中 upstream 是上游源的命名，这个命名可以自定义，不过和默认的 remote 源叫 origin 一样，这个 upstream 也是约定俗称的命名。

```
git remote add upstream <project-git-path>
```

当原项目的代码更新时可以通过下面的命令同步原项目的代码：

```
git fetch upstream
git checkout master
git merge upstream/master -no-ff
```

其中 merge 时的 `--no-ff` 参数是关闭默认的快速合并模式，为什么要使用这个参数可以查看参考文档中的“Git 分支管理策略”。

### 使用 pull request

首先对于 fork 的项目我们一般会新建一个分支进行维护，编码完成之后将代码 push 到自己的项目之前注意先同步原项目代码。

代码 push 上去之后就可以在 github 的界面上操作 pull request 了：

1. 到原项目的 pull request 页面，点击右上角的 `New pull request` 按钮
2. 点击 `compare across forks` 以选择我们 fork 的项目
3. 左边 `base` 选择原项目的主分支，右边 `compare` 选择我们 fork 出的项目里自己创建的分支
4. 这时页面上会展示出两个分支间的 diff 信息，确认无误后点击创建按钮并填写描述信息即可

### 参考文档

- [github fork 代码同步与pull request](https://www.jianshu.com/p/ce8496320c21)
- [Git分支管理策略](http://www.ruanyifeng.com/blog/2012/07/git.html)
- [Make-a-Pull-Request](https://github.com/rishabh-bansal/Make-a-Pull-Request)
- [About pull requests（Github 官方）](https://help.github.com/articles/about-pull-requests/)