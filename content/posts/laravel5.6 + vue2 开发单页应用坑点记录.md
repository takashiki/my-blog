+++
title= "laravel5.6 + vue2 开发单页应用坑点记录"
draft = false
date= "2018-06-24 12:13:10"
+++

### node-sass 在 windows 上的编译问题

node-sass 在 windows 上遇到的问题蛮多，如果顺利的话可以通过 `npm rebuild node-sass --force` 解决，但是重新编译的过程中可能会报 `python executable file not found` 类似的问题，然后提示通过设置 `python` 环境变量解决。但奇怪的是报错里面写的 python 可执行文件路径命名是正确的，本来准备放弃在 windows 上用 npm 准备直接在 docker 里操作了，不过搜索出来一个解决方案结果成功了。

通过管理员权限打开 PowerShell 然后执行以下命令之后重新编译 node-sass 即可：

```shell
npm --add-python-to-path='true' --debug install --global windows-build-tools
```

不一定适用于所有人，参考链接：

[Can't find Python executable "python" after installing #56](https://github.com/felixrieseberg/windows-build-tools/issues/56)

### 修改 vue 的组件文件后 BrowserSync 不会自动刷新

我目前在 `webpack.mix.js` 文件中按照查到的资料添加了如下部分，但是依旧不行：

```js
mix.webpackConfig({
    devServer: {
        watchOptions: {
            poll: true
        }
    }
});
```

改成用 `npm run watch-poll` 也不行，而且如果是 win10 上的话，这个模式会不停地弹 toast。

参考链接：

[Hot Reload not responding to changes on components #378](https://github.com/vuejs-templates/webpack/issues/378)

[watch is not working in windows #349](https://github.com/vuejs-templates/webpack/issues/349)

[关于webpack在docker容器内监听文件更改](https://www.jianshu.com/p/04eca89456d9)