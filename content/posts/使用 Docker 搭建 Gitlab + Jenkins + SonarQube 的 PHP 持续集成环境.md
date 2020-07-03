+++
title= "使用 Docker 搭建 Gitlab + Jenkins + SonarQube 的 PHP 持续集成环境"
draft = false
date= "2017-12-20 17:19:00"
+++

对于开源 PHP 项目，现在比较成熟的一套持续集成方案是使用 Github + TravisCI + StyleCI + Scrutinizer + coveralls，不过这套方案如果想要用于私有项目的话就抓狂了，个个要买套餐，其中很多还不便宜。而且对于公司内使用的项目来说，内部搭建的 Gitlab 方案更为常见，对于这种情况，我们可以使用 Gitlab + Jenkins + SonarQube 来进行代替。

### 安装 SonarQube

```shell
$ docker pull postgres

$ docker run --name db -e POSTGRES_USER=sonar -e POSTGRES_PASSWORD=sonar -d postgres

$ docker pull sonarqube

$ docker run --name sq --link db -e SONARQUBE_JDBC_URL=jdbc:postgresql://db:5432/sonar -p 9000:9000 -d sonarqube
```

执行完毕上面的命令后通过浏览器进入 SonarQube，默认用户名和密码都是 admin，进去后会有一段引导，里面会让你生成一个 access token，这个后面的配置 Jenkins 时会用到。

如果没有记下来的话，可以点右上角的用户头像里面的 My Account > Security 标签中可以生成一个新的。

### 配置 Jenkins

Jenkins 需要在全局的 系统设置 里面添加 SonarQube Server，填下对应的访问地址和上一步获取的 access token 即可。服务器地址填写 localhost 可能会有问题，填 ip 会比较好些。

然后需要在 系统管理 的 Global Tool Configuration 菜单中配置 SonarQube Scanner 安装，这个直接选择自动安装就好了，十分方便。

这两步配好之后就到对应的项目配置中添加构建步骤，下拉选择 Execute SonarQube Scanner，然后对于 2.1 版本以上的 SonarQube Scanner 就只需要配置 Analysis properties 这一项就可以了，比较常用的参数包括 `sonar.projectKey` (用来确定 该项目在 SonarQube 中叫什么名字) 和 `sonar.sources=`(用来指定需要扫描的目录)。

配完之后选择构建即可，可以去当前构建的 Console Output 里面查看有没有报错，正常执行完成的话，在 SonarQube 项目面板中就可以看到一个新增的命名为配置的  `sonar.projectKey` 的 项目了。

### 注意点：

- SonarPHP 自定义检查规则需要用 java 来写扩展，比较新的版本内置了 psr2 的规则基本够用，内置的 Quality Profiles 是可以复制一个出来进行自定义的
- Sonar 嗅探出的一些问题可能实际上并没有什么影响，比如变量名中含有 ‘pwd’ 等，如果原本使用方式确实合理则可适当忽略

### 参考链接：

- [使用 Docker 搭建代码质量检测平台 SonarQube](http://www.jianshu.com/p/a1450aeb3379)
- [使用GIT+JENKINS+DOCKER+SONAR+DISCONF+HARBOR+TOMCAT实现持续部署CD(上)](http://www.52devops.com/chuck/1404.html)
- [使用GIT+JENKINS+DOCKER+SONAR+DISCONF+HARBOR+TOMCAT实现持续部署CD(下)](http://www.52devops.com/chuck/1422.html)
- [[转]配置sonar、jenkins进行持续审查](http://www.cnblogs.com/zhuhongbao/p/4197974.html)
- [SonarQube+Jenkins,搭建持续交付平台](https://www.cnblogs.com/wangxin37/p/6397755.html)