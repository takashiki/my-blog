+++
title= "Fork过来的项目拉取源项目的更新"
draft = false
date= "2016-05-26 14:08:00"
+++

1. 在`Fork`的代码库中添加上游代码库的`remote`源，其中`upstream`表示上游代码库名，可以任意：

```shell
git remote add upstream https://github.com/lj2007331/lnmp.git
```

2. 将本地的修改提交 `commit`

3. 在每次 `Pull Request` 前做如下操作，即可实现和上游版本库的同步。

```shell
git remote update upstream
git rebase upstream/{branch name}
```

需要注意的是在`rebase`操作之前，一定要将`checkout`到`{branch name}`所指定的`branch`，

4. `Push`代码