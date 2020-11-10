---
title: linux基础_10.日志管理
date: 2020-10-10 17:39:10
tags: linux
categories: linux基础
---

## 日志管理简介

### 日志服务
centos 6.x中日志服务已经由rsyslogd取代了syslogd服务

<!--more-->

**rsyslogd新特点**

1. tcp协议传输，更安全
2. 日志消息及时的分析框架
3. 后台数据库
4. 配置文件中可以写简单的逻辑判断
5. 向下兼容（syslog）

**确定服务启动**

默认启动和自启动

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010175945.png" alt="image-20201010175945906" style="zoom:60%;" />

```shell
setup设置+*或								#启动
systemctl start rsyslog
systemctl status rsyslog
systemctl enabled  rsyslog		#自启动
systemctl is-enabled  rsyslog#查询是否自启动
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010180607.png" alt="image-20201010180607789" style="zoom:67%;" />

自启动检查时使用`chkconfig --list|grep rsyslog`失败

### 常见日志作用

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010181149.png" alt="image-20201010181149657" style="zoom:50%;" />

- /var/log/cron		系统定时任务相关日志

- /var/log /cups	打印信息日志

- /var/log /dmesg		开机自检信息

- /var/log /btmp		错误登录日志，二进制文件，不能直接vi打开需要使用命令lastb查看

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010181238.png" alt="image-20201010181238238" style="zoom:47%;" />

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010181341.png" alt="image-20201010181341906" style="zoom:55%;" />

- /var/log/lastlog		所有用户最后登录时间，二进制文件，使用lastlog查看

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010181608.png" alt="image-20201010181608483" style="zoom:60%;margin: 0 auto;" />

  伪用户Never loged in

- /var/log/maillog			记录邮件信息

- /var/log/message			记录系统重要信息，系统出现问题首先检查的日志文件
  

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010181832.png" alt="image-20201010181832758" style="zoom: 50%;" div align=center />

- /var/log/secure			验证和授权方面的信息，设计账户密码登录,eg.系统登录，ssh,su切换用户，sudo授权，添加修改用户密码都会记录再这个日志文件中

- /var/log/wtmp			永久记录所有用户登录/注销信息，系统启动关机重启时间。二进制文件，last查看

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010182136.png" alt="image-20201010182136448" style="zoom:50%;" />

- /var/log/utmp			当前以登录用户信息，随用户登录注销不断变化，只记录当前登录用户信息，不能使用vi查看，可用`w`,`who`,`users`




除了系统默认日志，采用rmp格式安装的系统服务也会默认把日志记录在/var/log/目录中（源码包安装的服务日志再源码包指定目录中）。这些日志不是由rsyslogd服务记录和管理，而是使用自己的日志管理文档记录自身日志

- /var/log/httpd/			
- /var/log/mail/			
- /var/log/samba/			rpm安装的samba服务的日志目录		
- /var/log/sssd/			守护进程安全服务目录

> [**守护进程**](https://www.cnblogs.com/mickole/p/3188321.html)
>
> ​		Linux Daemon（守护进程）是运行在后台的一种特殊进程。它独立于控制终端并且周期性地执行某种任务或等待处理某些发生的事件。它不需要用户输入就能运行而且提供某种服务，不是对整个系统就是对某个用户程序提供服务。Linux系统的大多数服务器就是通过守护进程实现的。常见的守护进程包括系统日志进程syslogd、 web服务器httpd、邮件服务器sendmail和数据库服务器mysqld等。
>
> ​		守护进程一般在系统启动时开始运行，除非强行终止，否则直到系统关机都保持运行。守护进程经常以超级用户（root）权限运行，因为它们要使用特殊的端口（1-1024）或访问某些特殊的资源。
>
> ​		一个守护进程的父进程是init进程，因为它真正的父进程在fork出子进程后就先于子进程exit退出了，所以它是一个由init继承的孤儿进程。守护进程是非交互式程序，没有控制终端，所以任何输出，无论是向标准输出设备stdout还是标准出错设备stderr的输出都需要特殊处理。
>
> 守护进程的名称通常以d结尾，比如sshd、xinetd、crond等

## rsyslogd 日志服务

### 日志文件格式
事件产生时间	发生事件的服务器的主机名	 产生事件的服务器或程序名 	时间的具体信息

​	eg./var/log/message

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010185128.png" alt="image-20201010185128047" style="zoom:67%;" />

### /etc/rsyslog.config配置文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010185640.png" alt="image-20201010185640893" style="zoom:50%;" />

```shell
# The authpriv file has restricted access.
authpriv.*                   /var/log/secure
认证相关服务.所有日志等级				记录位置

格式
服务名称[连接符号]日志等级			记录位置

```

- 服务名称

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010191034.png" alt="image-20201010191034266" style="zoom:40%;" /> 

  需要什么日志，将服务写进去即可

- 连接符
  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010191723.png" alt="image-20201010191723108" style="zoom:50%;" />
  
- 日志等级
  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010192253.png" alt="image-20201010192253580" style="zoom:50%;" />

  （从上到下）等级越高，信息量越小，处理等级越高，危害越大

- 记录位置
  - 日志文件的绝对路径，eg:/var/log/secure
  - 系统设备文件，eg:/dev/lp0
  - 转发给远程主机，eg:@192.168.0.210：514
  - 用户名，root
  - 忽略或丢弃日志，如~



<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010193627.png" alt="image-20201010193627661" style="zoom:50%;" />

内核日志默认不记录，想记录可打开

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010193735.png" alt="image-20201010193735034" style="zoom:49%;" />

message:记录任何等级高于info的日志，mail,authpriv,cron不记录

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010193953.png" alt="image-20201010193953116" style="zoom:50%;" />

疼痛等级发送给任何人



## 日志轮替

网站PV(点击量)上万，日志不做处理，硬盘占用

### 处理

1. 切割：每天的日志单独写

2. 删除轮替：旧日志删除腾出空间记录新日志

apache自带支持日志切割不支持轮替

### 日志文件命名规则

1. 日志配置文件中拥有`dateext`参数时，会用日志日期作为日志文件后缀。eg.secure-20130605

   日志名不会重叠，无需改名，只需要保存指定个数，删除多余文件即可

2. 配置文件中没有`dateext`参数，则需要改名，保证日志不会覆盖。
   轮替时：(1th)secure改为secure.1,(2th)secure.1改为secure.2,当然会新建新的日志secure,以此类推。

### logrotate配置文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010200901.png" alt="image-20201010200901078" style="zoom:47%;" />

- 参数

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010202318.png" alt="image-20201010202317947" style="zoom:50%;" />

- {}外是基本配置，{}内重叠按{}内生效

- rpm包安装的服务默认支持，源码包安装的服务在安装目录下，要想轮替需要加入

  eg.

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010210246.png" alt="image-20201010210246497" style="zoom:50%;" />

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010210339.png" alt="image-20201010210339023" style="zoom:50%;" />

### logrotate命令
```shell
logrotate [选项] 配置文件
					-v		显示日志轮替过程
					-f		强制日志轮替，不管条件是否符合，配置文件中所有日志强制轮替
不加选项=按照配置文件中的条件进行日志轮替
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010210843.png" alt="image-20201010210843407" style="zoom:45%;" />

显示有20个日志需要轮替，下图中apache日志轮替也加入

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010211027.png" alt="image-20201010211027100" style="zoom:40%;" />

修改下时间再次查看

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010211214.png" alt="image-20201010211214547" style="zoom:50%;" />

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010211445.png" alt="image-20201010211445630" style="zoom:50%;" />

记得校准时间`ntpdate pool.ntp.org` 通过ntp服务自动获取网络时间并同步