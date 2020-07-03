+++
title= "Ubuntu 安装 Kong 和 Cassandra"
draft = false
date= "2016-07-20 17:46:58"
+++

参考链接：

[https://getkong.org/install/ubuntu/](https://getkong.org/install/ubuntu/)
[https://www.digitalocean.com/community/tutorials/how-to-install-cassandra-and-run-a-single-node-cluster-on-ubuntu-14-04](https://www.digitalocean.com/community/tutorials/how-to-install-cassandra-and-run-a-single-node-cluster-on-ubuntu-14-04)

安装 Kong ：

```shell
apt update
apt upgrade
apt install netcat openssl libpcre3 dnsmasq procps
wget https://github.com/Mashape/kong/releases/download/0.8.3/kong-0.8.3.xenial_all.deb
dpkg -i kong-0.8.3.xenial_all.deb
```

安装 Cassandra ：

```shell
echo "deb http://www.apache.org/dist/cassandra/debian 22x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
echo "deb-src http://www.apache.org/dist/cassandra/debian 22x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
gpg --keyserver pgp.mit.edu --recv-keys F758CE318D77295D
gpg --export --armor F758CE318D77295D | sudo apt-key add -
gpg --keyserver pgp.mit.edu --recv-keys 2B5C1B00
gpg --export --armor 2B5C1B00 | sudo apt-key add -
gpg --keyserver pgp.mit.edu --recv-keys 0353B12C
gpg --export --armor 0353B12C | sudo apt-key add -
apt update
apt upgrade
apt install cassandra
```