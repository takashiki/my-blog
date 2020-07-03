+++
title= "实用shell脚本整理（不定期更新）"
draft = false
date= "2015-07-24 14:39:00"
+++

## 转换时间和unix时间戳

```shell
#时间转时间戳
date -d "2015-07-24 12:25:00" +%s

#时间戳转时间
date -d "@1437711900"
```

## 分析nginx日志

```shell
#查看访问地址次数排行
awk -F\" '{print $2}' blog_access.log | awk '{print $2}' | sort | uniq -c | sort -rn
```

## 输出当前目录下各个子目录所使用的空间

```shell
du -h --max-depth=1
```

## 文件夹下文件按大小排序

```shell
du -sh /dir/* | sort -rn (后面还可以接 head、tail 之类的命令)
```

## 查找文件内容

```shell
grep "search" filename

#从文件内容查找与正则表达式匹配的行：
grep –e “/pattern/” filename

#查找时不区分大小写：
grep –i "search" filename

#查找匹配的行数：
grep -c "search" filename

#从文件内容查找不匹配指定字符串的行：
grep –v "search" filename

#结合find
find . -name "*.php" | xargs grep "function"
```