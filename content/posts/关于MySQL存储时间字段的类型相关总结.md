+++
title= "关于MySQL存储时间字段的类型相关总结"
draft = false
date= "2017-05-17 15:25:00"
+++

一般我们用 MySQL 来存储时间时会考虑使用 datetime、timestamp、int 几种类型。

### int

用 int 类型的字段时，我们一般是存储 10 位数字的时间戳，也可以用 bigint 存储精确到毫秒的时间戳。

优势：无关乎时区；占用存储空间小，查询效率稍高
劣势：可读性差

在一些数据量很大，对性能要求较高的场景可以考虑使用。

### datetime

datetime 类型在 MySQL 的不同版本直接有一定差异，

- MySQL 5.6.4 支持存储微秒，详见 [MySQL 5.6.4 ChangeLog](http://dev.mysql.com/doc/refman/5.6/en/news-5-6-4.html)
- MySQL 5.6 支持默认值为 `CURRENT_TIMESTAMP` 和 `NOW()`

优势：不存在 `2038 年问题`；可读性高；时间精度高；不对时区处理，原样存储
劣势：性能稍差一些，不过随着 MySQL 性能越来越高，这点劣势也逐渐不重要起来

### timestamp 

劣势：存在 `2038 年问题`；时区存储存在转换

不太推荐使用

### 性能比较

[MySQL 5.4 MyISAM](http://gpshumano.blogs.dri.pt/2009/07/06/mysql-datetime-vs-timestamp-vs-int-performance-and-benchmarking-with-myisam/)

[MySQL 5.4 InnoDB](http://gpshumano.blogs.dri.pt/2009/07/06/mysql-datetime-vs-timestamp-vs-int-performance-and-benchmarking-with-innodb/)

[MySQL Date Format: What Datatype Should You Use? We Compare Datetime, Timestamp and INT](http://www.vertabelo.com/blog/technical-articles/what-datatype-should-you-use-to-represent-time-in-mysql-we-compare-datetime-timestamp-and-int)

参考文档：

[MySQL存储时间用int、timestamp还是datetime?](http://codecloud.net/17541.html)



