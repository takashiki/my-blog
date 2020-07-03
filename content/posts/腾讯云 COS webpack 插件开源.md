+++
title= "腾讯云 COS webpack 插件开源"
draft = false
date= "2018-01-14 22:13:00"
+++

今天想把一个老的 Yii2 项目改成比较时髦的前后端分离的开发模式，于是试用了 webpack，感觉还不错。

项目线上我是想直接把编译后的文件传到带 cdn 的对象存储上，因为服务器用的是腾讯云的 cvm，所以对象存储就顺便选择了 cos。

Github 上搜了下没有现成的 webpack 插件，不过有几个现成的七牛的，比较了一下发现 [https://github.com/lyfeyaj/qn-webpack](https://github.com/lyfeyaj/qn-webpack) 这个项目的代码最简洁清晰，于是就在这个项目的基础上自己改出了一个 cos 的 webpack 插件并开源了出来：[https://github.com/takashiki/cos-webpack](https://github.com/takashiki/cos-webpack)。

npm 发布包的步骤参考：[手把手教你用npm发布一个包](https://www.jianshu.com/p/36d3e0e00157)。

下面是该插件的安装和使用方式：

## 前提

需要 Node 版本在 v4.0 以上，COS V4 以上（APPID 为 125 开头）

## 安装

```sh
npm i -D cos-webpack
```

## 使用方法

支持的配置项:

+ `secretId` COS SecretId
+ `secretKey` COS SecretKey
+ `bucket` COS 存储对象名称，格式为对象名称加应用 ID，如：`bucket-1250000000`
+ `region` COS 存储地域，参见[官方文档](https://cloud.tencent.com/document/product/436/6224)
+ `path` 存储路径， 默认为 `[hash]`，也可以指定 hash 长度，如: `[hash:8]`
+ `exclude` 可选，排除特定文件，正则表达式，如: `/index\.html$/`
+ `include` 可选，指定要上传的文件，正则表达式，如: `/app\.js$/`
+ `batch` 可选，批量上传文件并发数，默认 20

***注: Webpack 的 `output.publicPath` 要指向 COS（或自定义的）域名地址***

```js
// 引入
const CosPlugin = require('cos-webpack');

// 配置 Plugin
const cosPlugin = new CosPlugin({
  secretId: 'my-secret-id',
  secretKey: 'my-secret-key',
  bucket: 'my-125000000',
  region: 'ap-chengdu',
  path: '[hash]/'
});

// Webpack 的配置
module.exports = {
 output: {
    // 此处为 COS 访问域名(bucket-1250000000.file.myqcloud.com) 加上 path([hash]/)
    publicPath: "http://bucket-1250000000.file.myqcloud.com/[hash]/"
    // ...
 },
 plugins: [
   cosPlugin
   // ...
 ]
 // ...
}
```