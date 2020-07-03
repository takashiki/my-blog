+++
title= "MySQL大数据量表中删除重复记录"
draft = false
date= "2013-12-10 21:21:00"
+++

   最近工作中需要抓取大量新闻，抓取的数据中由于一些原因存在一些重复数据，而整个数据表的记录数接近10万条，大小接近1个G，又在我自己的渣渣本本上，查询速度十分不理想，想要完成一个最基本的查询都很困难。在看了一些相关资料后终于找到解决方法，分享给大家参考。
   首先说一下新闻表的大概结构，主要是包含id、title、content等字段，其中title字段使用较为频繁，并且需要用该字段判断重复记录，所以我们先给title字段添加索引。添加索引后我们可以使用以下语句来很快地查询出哪些title是重复的：
```sql
SELECT `title` FROM `info` GROUP BY `title` HAVING COUNT( `title` ) >1
```
 但如果要一次查出重复字段的id的话就需要用到子查询了，可是子查询的效率很低，明显是不合适的，所以我们可以先建一个临时表：
```sql
CREATE TABLE `tmptable` AS (SELECT `title` FROM `info` GROUP BY `title` HAVING COUNT( `title` ) >1);
```
 有了重复字段的标题接下来就可以查出重复字段的id了，我这里为了方便又建了一个临时表：
```sql
CREATE TABLE `idtable` AS ( SELECT min(a.`id`) AS id, a.`title` FROM `info` a, `tmptable` t WHERE a.`title` = t.`title` GROUP BY a.`title`);
```
 这样删除重复字段就很容易了：
```sql
DELETE a FROM `info` a,`idtable` t WHERE a.`id` = t.`id`;
```
 
 不过我这篇文章中的方法只适用于记录只重复了一次的情况，不过稍微改改就可以删除重复次数较多的记录，这里就不在赘述。