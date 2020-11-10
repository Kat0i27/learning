---
title: linux基础_8.linux服务管理.md
date: 2020-10-09 19:10:38
tags: linux
categories: linux基础
---

## 服务简介与分类

### 服务分类

- rpm包默认安装的服务

  安装完成后与系统默认值一致

  <!--more-->

  - 独立的服务

    服务在内存中，用户访问直接响应，快但耗费内存资源

  - 基于xinetd的服务

    通过xinetd访问其管理的服务（本身不占用内存），优缺点相反

- 源码包安装

  类似第三方

>[**Xinetd服务**](https://www.cnblogs.com/lsgxeva/p/9280777.html)
>
>​	xinetd即extended internet daemon，xinetd是新一代的网络守护进程服务程序，又叫超级Internet服务器。经常用来管理多种轻量级Internet服务。xinetd提供类似于inetd+tcp_wrapper的功能，但是更加强大和安全。

### 查询已安装服务

**查看自启动状态（可附带查看所有已安装rpm包服务）**

```shell
chkconfig --list		#查看服务自启动状态，限rpm包安装服务
-------------------

netconsole      0:off   1:off   2:off   3:off   4:off   5:off   6:off
network         0:off   1:off   2:on    3:on    4:on    5:on    6:off
```

- 0~6：关机，单用户，不完全多用户，字符界面，未分配，重启
- 2~5：on，不代表已经启动，指下次运行或重启系统时服务自启动

**查看已启动服务**

```shell
ps -aux|grep crond
```

```shell
netstat -tuln
```

缺点：netstat无法查看守护进程（没有端口）

**源码包安装服务**

查看服务安装位置，一般在/usr/local下

### RPM安装服务与源码安装服务区别

- 安装位置不同（导致管理方法不同）
  - 源码包安装在指定位置，一般是/usr/local
  - rpm包安装在默认位置，/etc（配置文件）	
                     /etc/.rc.d/init.d(启动脚本)		约定俗成

- 删除
	- rpm  需要-e选项，安装包到处都是
	- 源码包，直接删除指定位置文件，不会有垃圾信息

service可启动rpm包安装的服务



## RPM包安装服务的管理
### 文件位置
**通用位置**

/etc/rc.d/init.d启动脚本位置（独立）
/etc/init.d:启动脚本位置（独立同上，均为软连接）
/etc/sysconfig:初始化环境配置文件位置
/etc/:默认配置文件

/etc/xinetd.d服务的启动脚本
/etc/xinetd.conf：xinetd配置文件
/var/lib:服务产生数据的位置
/var/log/:日志

**特殊位置-约定俗成**

/var/www/html



### 独立服务
#### 启动

```shell
/etc/inid.d/服务文件名 start|stop|restart|status		#status指查看启动状态

service 独立服务名 start|stop|restart|status		#到目录下寻找，redhat专有命令，简化操作
service --status-all	#列出系统所有rpm安装的服务启动状态
```

#### 自启动(3)
**方法1**

```shell
chkconfig --level 2345 httpd on|off		#设置自启动，设置完成后目前服务不一定启动
chkconfig  httpd on|off			#级别默认
```

**方法2**

修改文件`/etc/rc.d/rc.local`(系统启动后，所有启动程序运行完成后输入用户名密码前，读取文件)
```shell
/etc/inid.d/服务文件名 start			#添加
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201009205748.png" alt="image-20201009205748160" style="zoom:50%;" />

touch：第一次-新建文件，第二/n次：修改文件最后修改时间

**方法3**

使用ntsysv命令管理自启动，可管理独立/xinetd服务即rpm包服务，源码包服务默认不可设定

（rethat专有命令）

加*：自启动，去\*:取消自启动

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201009210246.png" alt="image-20201009210246881" style="zoom:50%;" />

推荐**方法2**。陌生服务器，打开文件即可知道系统自启动哪些服务；有助于源码包和rpm包统一管理，避免chkconfig和配置文件之间设置产生冲突

### xinetd

#### xinetd启动守护进程

最适合的应该是那些常用的网络服务，同时，这个服务的请求数目和频繁程度不会太高。系统默认使用xinetd的服务可以分为如下几类。

- 标准Internet服务：telnet、ftp。
- 信息服务：finger、netstat、systat。
- 邮件服务：imap、imaps、pop2、pop3、pops。
- RPC服务：rquotad、rstatd、rusersd、sprayd、walld。
- BSD服务：comsat、exec、login、ntalk、shell、talk
- 内部服务：chargen、daytime、echo、servers、services、time。
- 安全服务：irc。
- 其他服务：name、tftp、uucp。

具体使用xinetd的服务可在/etc/services文件中指出



#### 启动
基于`xinetd`的服务越来越少（eg.不安全的远管telnet-server,sync网络备份)，默认未安装`xinetd`服务
```shell
yum -y install xinetd
yun -y install telnet-server
```

检测是否安装

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201009222736.png" alt="image-20201009222736076" style="zoom:50%;" />

启用服务,Telnet，xinetd和telnet服务安装完成后是默认禁用（disbale）的。

```shell
systemctl enable xinetd.service			#同时开机自启动

systemctl enable telnet.socket
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201009223025.png" alt="image-20201009223025188" style="zoom:67%;" />

```shell
vi /etc/xinetd.d/telnet
#不存在可自行创建

#服务名称
#将语句 disable = yes 改成 disable = no 保存退出。激活 telnet 服务
#标志位REUSE，TCP/IP socket可重用
#使用tcp协议数据包，流数据
#允许多个连接同时连接
#启动服务用户为root
#服务的启动程序
#登陆失败后，记录用户UID
service telnet
{
	disable = no
	flags = REUSE
	socket_type = stream
	wait = no
	user = root
	server = /usr/sbin/in.telnetd
	log_on_failure += USERID
}
```
重启xinetd

```shell
service xinetd restart
或者
systemctl restart xinetd.service		#重新启动xinetd服务
```
启动服务

```shell
systemctl start telnet.socket
systemctl status telnet.socket
```

```shell
chkconfig --list
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201009230550.png" alt="image-20201009230550400" style="zoom: 50%;" />

#### 自启动(2)

**方法1**

```shell
chkconfig telnet on
```

实际上xinetd启动和自启动通用

**方法2**

```shell
ntsysv
```



### 源码包安装服务的管理

#### 启动
绝对路径调用启动脚本，不通过源码包启动脚本位置不同
```shell
/usr/local/apache2/bin/apachectl start|stop
```
查看源码包安装方法/源码包需要手动下载

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010093428.png" alt="image-20201010093421853" style="zoom:67%;" />

进入解压后的安装包，查看启动方式

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010205427.png" alt="image-20201010205427542" style="zoom: 50%;" />

```shell
PREFIX- 变量，指安装位置，可以随意指定默认/usr/local
安装位置/bin/apachectl start
```

![image-20201010205338255](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010205338.png)

报错不影响

如果用`service httpd start`启动源码包安装，报错80端口冲突

![image-20201010095949291](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013120053.png)


#### 自启动

类似rpm包安装的服务自启动，修改文件

```shell
vi /etc/rc.d/rc.local		加入
/usr/local/apache2/bin/apachectl start
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013120054.png" alt="image-20201010100611407" style="zoom:67%;" />


### 命令通用
#### 源码包服务被服务管理命令(service)识别
软连接到init.d
```
ln -s /us/local/apache2/bin/apachectl /etc/init.d/apache
```

service命令归根结底是在搜索库/etc/init.d

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013120055.png" alt="image-20201010100841976" style="zoom:67%;" />

该目录下均为rpm包安装的服务

#### 源码包apache服务能被chkconfig与ntsysv命令管理自启动

![image-20201010105034736](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010105034.png)

```shell
# vi /etc/init.d/apache
# chkconfig:35 86 76
# 指定运行顺序，启动顺序，关闭顺序		不能与系统现有顺序冲突
#description:source package apache
#说明
```

![image-20201010105801671](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010105801.png)

查看系统现有顺序

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010105612.png" alt="image-20201010105612164" style="zoom:67%;" />

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010105549.png" alt="image-20201010105548959" style="zoom: 80%;" />

查看状态，自启动

![image-20201010105836681](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010105836.png)



## 服务管理总结

### rpm包安装的服务
**启动**

均可使用

```shell
service 服务名 start|stop|restart
```

`xinetd` 服务本身也可以用service，其包含的服务需要用`systemctl `, 例如

```shell
systemctl start|restart|stop (服务名)sshd.service
```

启用/禁用服务

```shell
systemctl enable xinetd.service			#同时开机自启动
systemctl disable xinetd.service			
```

**自启动(独立服务)**

`chkconfig修权限`

```shell
chkconfig  httpd on|off			#级别默认
```

修改文件 `/etc/rc.d/rc.local`,加入

```shell
/etc/inid.d/服务文件名 start			#添加
```

`ntsysv`命令，[+-]*

**自启动(xinetd)**

```shell
chkconfig telnet(服务名) on
```

`ntsysv`命令

```
systemctl enable xinetd.service
```


### 源码包安装的服务
**启动**

绝对路径调用启动脚本(启动方法可在安装文件中的INSTALL中查看)

```shell
/usr/local/apache2/bin/apachectl start|stop
```

**自启动**

修改文件`vi /etc/rc.d/rc.local	`

