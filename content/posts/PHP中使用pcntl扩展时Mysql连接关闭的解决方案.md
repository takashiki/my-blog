+++
title= "PHP中使用pcntl扩展时Mysql连接关闭的解决方案"
draft = false
date= "2016-06-07 15:48:51"
+++

PHP官方的手册里也记载了该问题及其解决方法：[http://php.net/manual/zh/function.pcntl-fork.php#70721](http://php.net/manual/zh/function.pcntl-fork.php#70721)。

产生该问题的原因就是子进程会关闭父进程的数据库连接，所以需要在子进程中重新进行数据库连接，官方文档里给出的示例代码如下：

```php
// Create the MySQL connection 
$db = mysql_connect($server, $username, $password); 

$pid = pcntl_fork(); 
             
if ( $pid == -1 ) {        
    // Fork failed            
    exit(1); 
} else if ( $pid ) { 
    // We are the parent 
    // Can no longer use $db because it will be closed by the child 
    // Instead, make a new MySQL connection for ourselves to work with 
    $db = mysql_connect($server, $username, $password, true); 
} else { 
    // We are the child 
    // Do something with the inherited connection here 
    // It will get closed upon exit 
    exit(0); 
```

如果是使用框架的话，也需要进行类似的操作，比如说Yii1中可以这么写，参考链接[http://www.yiiframework.com/forum/index.php/topic/3460-pcntl-fork-mysql-and-yii/](http://www.yiiframework.com/forum/index.php/topic/3460-pcntl-fork-mysql-and-yii/):

```php
Yii::app()->getDb()->setActive(false);
$pid = pcntl_fork();
Yii::app()->getDb()->setActive(true);
```

