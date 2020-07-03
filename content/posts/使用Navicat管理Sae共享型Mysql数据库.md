+++
title= "使用Navicat管理Sae共享型Mysql数据库"
draft = false
date= "2015-08-23 22:10:18"
+++

[Sae](http://sae.sina.com.cn/)在国内PaaS方面可以说一直是处于领军地位的，虽然现在不像之前通过开发者认证就每月都有免费云豆领了，不过如果想用PaaS平台，Sae依旧是不错的选择。

Sae自带的phpmyadmin版本比较老了，估计很多人都希望能有个更好的工具来进行数据库管理，最近研究了一下用Navicat的http tunnel来连接sae的数据库，最终捣鼓成功了，在这里分享给大家。

首先安装Navicat，在安装根目录找到ntunnel_mysql.php文件，将该文件放到自己的项目中，可以自由重命名。

然后对该文件的以下内容进行修改，大约在193行左右：

```php
$hs = $_POST["host"];
if( $_POST["port"] ) $hs .= ":".$_POST["port"];
$conn = mysql_connect($hs, $_POST["login"], $_POST["password"]);
$errno_c = mysql_errno();
if(($errno_c <= 0) && ( $_POST["db"] != "" )) {
	$res = mysql_select_db( $_POST["db"], $conn);
	$errno_c = mysql_errno();
}
```

修改为：

```php
$username = 'yourusername';
$password = 'yourpassword';
if ($_POST["login"] == $username && $_POST["password"] == $password) {
    $hs = SAE_MYSQL_HOST_M . ':' . SAE_MYSQL_PORT;
    $conn = mysql_connect($hs, SAE_MYSQL_USER, SAE_MYSQL_PASS);
    $errno_c = mysql_errno();
    if(($errno_c <= 0)) {
        $res = mysql_select_db(SAE_MYSQL_DB, $conn);
        $errno_c = mysql_errno();
    }
} else {
    EchoHeader(401);
    echo GetBlock("Authentication failed");
    exit();
}
```

注意将上面代码中的$username和$password定义成你自己想要设置的用户名和密码，这个只是做校验用，下面Navicat连接时会用到。修改好后就将文件上传至sae，注意该文件要能被访问。

接下来就可以到Navicat里新增链接了，主机名和端口随便填即可，但不能为空，用户名和密码即为上一步的$username和$password，注意修改为自己设置的。

![QQ截图20150823222243.jpg](https://ooo.0o0.ooo/2015/08/23/55d9d8de75b61.jpg "QQ截图20150823222243.jpg")

接下来在高级标签里选择使用高级连接，点击添加数据库，数据库名即为下图中红框标出来的部分，可以在sae自带的phpmyadmin的界面中看到。

![QQ截图20150823222800.jpg](https://ooo.0o0.ooo/2015/08/23/55d9d8de969d1.jpg "QQ截图20150823222800.jpg")

![QQ截图20150823222539.jpg](https://ooo.0o0.ooo/2015/08/23/55d9d8de9d2c1.jpg "QQ截图20150823222539.jpg")

在http标签中选择使用http通道，通道地址即为你项目中该ntunnel_mysql.php文件的路径。

![QQ截图20150823222849.jpg](https://ooo.0o0.ooo/2015/08/23/55d9d8dede8b9.jpg "QQ截图20150823222849.jpg")

最后点击连接测试，不出意外此时就能使用Navicat来管理sae数据库了。