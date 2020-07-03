+++
title= "Linux下安装Kafka和PHP的相关扩展"
draft = false
date= "2016-05-31 17:50:00"
+++

以下操作在 Ubuntu 16.04 下进行，其他系统可能略有不同：

### 安装kafka

1. 配置防火墙，开启9092端口，编辑 `\etc\iptables.up.rules` 文件，添加一行：

```shell
-A INPUT -p tcp -m state --state NEW -m tcp --dport 9092 -j ACCEPT
```

保存后执行：

```shell
iptables-apply /etc/iptables.up.rules
```

2. Ubuntu 16.04 自带 JDK，其他系统如果未安装则需要安装。

3. 安装 kafka

kafka 最新的发行版本下载地址可以在 [http://archive.apache.org/dist/kafka/](http://archive.apache.org/dist/kafka/) 里找。

```shell
cd /tmp
wget http://archive.apache.org/dist/kafka/0.10.0.0/kafka_2.11-0.10.0.0.tgz
tar -xzvf kafka_2.11-0.10.0.0.tgz
mv kafka_2.11-0.10.0.0 /usr/local/kafka
```

4. 启动 zookeeper 和 kafka

这两者的配置这里就先不研究了，直接启动试试看：

```shell
nohup /usr/local/kafka/bin/zookeeper-server-start.sh /usr/local/kafka/config/zookeeper.properties &
nohup /usr/local/kafka/bin/kafka-server-start.sh /usr/local/kafka/config/server.properties &
```

### 安装PHP相关扩展

#### zookeeper 扩展

1. 安装 libzookeeper_mt

```shell
cd /tmp
wget -N http://archive.apache.org/dist/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz; tar zxvf zookeeper-3.4.6.tar.gz; rm -f zookeeper-3.4.6.tar.gz
cd zookeeper-3.4.6/src/c
./configure --prefix=/usr/local/zookeeper
make
sudo make install
```

2. 安装 PHP 的 zookeeper 扩展：

```shell
cd /tmp
gid clone https://github.com/jbboehr/php-zookeeper.git
# 如果是 PHP7：
# git checkout php7
phpize
./configure --with-php-config=/usr/local/php/bin/php-config  --with-libzookeeper-dir=/usr/local/zookeeper
make
sudo make install
```

然后就可以使用这个包了：[https://github.com/nmred/kafka-php](https://github.com/nmred/kafka-php)。

#### rdkafka 扩展

1. 安装 librdkafka：

```shell
cd /tmp
wget -N https://github.com/edenhill/librdkafka/archive/master.zip -O librdkafka.zip; unzip librdkafka.zip; rm -f librdkafka.zip
cd librdkafka-master
./configure
make
sudo make install
```

2. 安装 php-rdkafka 扩展：

```shell
git clone https://github.com/arnaud-lb/php-rdkafka.git
cd php-rdkafka
# 如果是 PHP7
# git checkout php7
phpize
./configure
make all -j 5
sudo make install
```

### 参考文档：

- [http://www.osyunwei.com/archives/9345.html](http://www.osyunwei.com/archives/9345.html)
- [https://github.com/Qihoo360/logkafka/tree/master/docs](https://github.com/Qihoo360/logkafka/tree/master/docs)
- [http://blog.programster.org/install-zookeeper-php-extension/](http://blog.programster.org/install-zookeeper-php-extension/)