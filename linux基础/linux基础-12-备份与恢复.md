---
title: linux基础_12.备份与恢复
date: 2020-10-10 17:54:38
tags: linux
categories: linux基础
---

### 需要备份的数据

- /root/
- /home/
- /var/spool/mail/
- /etc/
- 其他/var/log等

<!--more-->

- 安装服务的数据（eg.）

  apache：配置文件，网页主目录，日志文件

  myslq：(源码包安装)/usr/local(或安装目录)/mysql/data(5.5);(rpm安装)/var/lib/mysql

备份：不放在同一个篮子里----异地备份

### 备份策略

1. 完全备份

   全部备份，取决于数据重要性。
   理论上最好，恢复备份方便，但需要考虑备份时间，占用硬盘空间

2. 增量备份

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010233029.png" alt="image-20201010233029033" style="zoom:50%;" />

   理论上备份占用空间最小，但恢复并比较麻烦

   每次备份与上次相比

2. 差异备份

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010233218.png" alt="image-20201010233218779" style="zoom:50%;" />

   每次备份与原始数据相比

   比完全备份少点，恢复比增量方便

### 常见备份命令dump，恢复restore

#### dump

查看是否安装

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010233632.png" alt="image-20201010233632051" style="zoom:60%;" />

```shell
yum -y install dump								#安装
```
```shell
dump [] 备份后文件名 文件/目录
			-level			0-9备份级别，0完全备份，1增量备份，1-第一次，2-第二次...
			-f file			指定备份后的文件名
			-u					(常用)备份成功之后，记录备份时间在/etc/dumpdates
			-v					详细输出信息
			-j					(常用)备份文件压缩为.bz2
			-W					显示允许被dump的分区的备份等级及时间
```

```shell
 dump -0uj -f /root/boot.bak.bz2 /boot/
 #完全备份，写入时间，压缩，指定备份后文件名 备份目录
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010234609.png" alt="image-20201010234609568" style="zoom:50%;" />

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011091637.png" alt="image-20201010234735466" style="zoom:47%;" />

在/boot/内加入数据/boot/temp(约20k)进行增量备份

```shell
dump -1uj -f /root/boot.bak1.bz2 /boot/
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010235746.png" alt="image-20201010235746022" style="zoom:60%;" />

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010235904.png" alt="image-20201010235904693" style="zoom:64%;" />

```shell
dump -W							查询整个分区备份情况
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011000019.png" alt="image-20201011000018999" style="zoom:67%;" />

备份文件或目录，只能完全备份，不再支持增量

```shell
dump -0j -f /root/etc.dump.bz2 /etc/
```

dump命令只有在备份分区时才可以增量备份

#### restore恢复

```shell
restore [模式选项][选项]
(不可混用)-C:比较备份数据与实际数据变化
				-i:进入交互模式，手工选择要恢复的文件
				-t:查看模式，查看备份文件中拥有哪些数据
				-r:还原模式，用于数据还原
									-f 指定备份文件名
```

实例：

```shell
#修改/boot目录中内核进行文件名(记得保留原名，用于最后恢复，否则下次开机崩溃)
mv /boot/initramfs-3.10.0-957.el7.x86_64.img /boot/initramfs-3.10.0-957.el7.x86_64.img.bak
#比较现有文件和备份数据变化,restore发现内核镜像文件丢失
restore -C -f /root/boot.bak.bz2
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011001307.png" alt="image-20201011001307484" style="zoom:67%;" />

```shell
mv /boot/initramfs-3.10.0-957.el7.x86_64.img.bak /boot/initramfs-3.10.0-957.el7.x86_64.img
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011001426.png" alt="image-20201011001425952" style="zoom:67%;" />

查看模式

```shell
restore -t -f boot.bak.bz2
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011001549.png" alt="image-20201011001549509" style="zoom:50%;" />

还原模式

```shell
# 还原boot.bak.bz2分区备份
# 1.先还原完全备份的数据
mkdir boot.test
cd boot.test/
restore -r -f /root/boot.bak.bz2		#原始数据恢复，同时解压缩
restore -r -f /root/boot.bak1.bz2		#恢复增量备份
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011001938.png" alt="image-20201011001938236" style="zoom:65%;" />

还原文件

```shell
#还原/etc/目录备份etc.dump.bz2,创建进入目录
restore -r -f etc.dump.bz2
```

