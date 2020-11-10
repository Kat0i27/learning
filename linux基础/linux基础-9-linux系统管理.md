---
title: linux基础_9.linux系统管理
date: 2020-10-10 11:03:26
tags: linux
categories: linux基础
---

## 进程管理

### 进程查看
#### 进程
正在运行当中的程序/命令，每个进程都是一个运行的实体，有自己的地址空间，占用一定系统资源

猜猜ls运行会产生进程吗 ~

#### 进程管理作用
##### 判断服务器健康状态（主）

<!--more-->

  win下查看内存占用和利用率

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013120107.png" alt="image-20201010111003742" style="zoom:50%;" />

  正常进程占用过高--终止

  非法进程--判断进程，找到病毒主体，手工/杀软删除。单纯杀死不推荐

**linux**

```shell
top [选项]
-d 				#指定更新间隔秒数
?或h			 #显示交互模式帮助
P					#以CPU使用率排序，默认
M					#以内存使用率排序
N					#以PID排序
q					#退出
```

![image-20201010114003552](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010114003.png)

每3s更新,Cpu占用率高-靠上

- 第一行 系统

  系统当前时间19:39:52	开机已2h07m	用户数量	**系统在1m/5m/15m前的平均负载**(<1,一般认为较小(单核),多核(eg.8)超过8可视为高负载)

- line2 进程

  系统总进程数	正在运行的进程数	睡眠进程	正在停止进程	僵尸进程(正在终止,还未完全停止,长时间存在证明卡死,判断后手工终止)

- line3 CPU

  用户模式占用率us	系统占用sy	改变过优先级的用户进程占用百分比ni	**空闲id**	等待输入/出wa	hi硬中断占用	si软中断占用	st虚拟cpu占用

- line4 真实物理内存

  物理内存总大小(KB)	已使用	**空闲**	缓冲

- line5 交换分区

  交换分区(虚拟内存)总大小	已使用	空闲	缓存

默认按Cpu占用率排序


##### 查看系统中所有进程

  win下
  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013120108.png" alt="image-20201010111559592" style="zoom:50%;" />

**linux**

```shell
ps aux		#BSD格式查看系统所有进程(unix)
ps -le		#Linux标准命格式查看
```

![image-20201010111931437](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013120109.png)

每行代表一个系统进程

- USER：进程由哪个用户产生

- PID：进程ID，/usr/lib或/sbin/init(软链)是系统启动运行的第一个进程,PID永远是1

![image-20201010113022804](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013120110.png)

- CPU：占用CPU资源百分比

- MEM:占用物理内存百分比

- VSZ:占用虚拟内存百分比,KB

- RSS:占用实际物理内存大小,KB

- TTY:在那个终端进行,?不是由终端调用,由进程直接调用

  tty1-tty7:本地终端(tty1-tty6本地字符界面,tty7是图形终端)

  pts0-255:虚拟终端,远程

![image-20201010113615149](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013120111.png)

- STAT:进程状态,R允许,S休眠,T停止,s包含子进程,+位于后台
- START:启动时间,超过24h显示月日
- TIME:占用CPU时间,时间越长代表进程越耗资源
- COMMEND:产生进程的命令



tree查看目录树,pstree查看进程树
```shell
pstree	[选项]
-p	PID
-u	所属用户
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010120016.png" alt="image-20201010120016214" style="zoom:50%;" />


##### 杀死进程 `kill`
  使用场景：正常终止失效(eg.service stop 服务)
	


### 终止进程

```shell
kill -l	PID		#查看可用的进程信号
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010120500.png" alt="image-20201010120500440" style="zoom: 50%;" />

```shell
kill -1 PID		重启
kill -9 PID		终止
```

- PID查询`ps aux`, 不认识的进程避免随意终止可能引起系统崩溃

杀死父进程,子进程被杀; 杀死子进程,不影响父进程

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010151224.png" alt="image-20201010151224051" style="zoom:50%;" />           <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010151436.png" alt="image-20201010151436630" style="zoom:50%;" />

-l 重启之后子进程PID改变

```shell
killall [选项][信号] 进程名
				-i		交互式,询问是否要杀死某个进程
				-I		忽略进程名的大小写
killall -9 httpd
```

```shell
pkill  [选项] [信号] 进程名
				-t 终端号			按照终端号踢出用户
其余用法同killall

# w 查询用户
```
<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010152702.png" alt="image-20201010152701987" style="zoom: 67%;" />

**kill虽然可以中止命令,但不是标准正常终止,正常service stop 服务**


## 工作管理
### 把进程放入后台(2)
类似win下最小化

**方法1**

命令+`&`
```shell
tar -zcf etc.tar.gz /etc &
```
**方法2**

执行命令过程中,ctrl+z

区别:
方法1放入后台继续运行,ctrl+z后台中止

### 查看后台工作
```shell
jobs -l		#-l显示PID
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010153556.png" alt="image-20201010153556875" style="zoom: 67%;" />

(ctrl+z top)

- +代表最后一个放入后台的工作,-表示倒数第二个.恢复时首先恢复+,再-

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010154352.png" alt="image-20201010154352091" style="zoom:67%;" />

### 恢复后台暂停的工作

**到前台**

```shell
fg %工作号
```
**到后台**

```shell
bg % 工作号
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010154557.png" alt="image-20201010154557362" style="zoom:67%;" />

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010154729.png" alt="image-20201010154729482" style="zoom: 50%;" />

top命令是系统健康状态,必须在前台与用户交互,后台不能正常运行.类似的还有vi.

后台执行的命令一般是打包,查找

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010154706.png" alt="image-20201010154706125" style="zoom:50%;" />

`bg`,`fg`使用时可省略%,` jobs 工作号`可查询对应工作的运行状态



## 系统资源查看
#### vmstat-监控系统资源
```shell
vmstat[刷新延时 刷新次数]
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010155547.png" alt="image-20201010155547545" style="zoom:67%;" />

#### dmesg-开机时内核检查信息

```shell
dmesg
输出过多,添加grep过滤
dmesg|grep CPU
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010155909.png" alt="image-20201010155909942" style="zoom:60%;" />

#### free-查看内存使用状态

```shell
free [-b-k-m-g]
选项可不加,调整显示单位[字节(默认)/KB/MB/GB]
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010160112.png" alt="image-20201010160111934" style="zoom:67%;" />

used=缓冲和缓存buff/cache(只能被内核直接调用)+free

**cache和buff区别**

cache: 加速数据从"硬盘"读取,

buff: 加速数据写入硬盘



#### 查看CPU信息

```shell
cat /proc/cpuinfo
```

dmesg看到的是cpu的启动基本信息,cpuinfo中保存的更加详细的信息,每次开机检测写入,断电释放



#### uptime-显示系统启动时间和平均负载

![image-20201010161236122](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010161236.png)

同`top`命令和`w`第一行



#### 查看系统和内核相关信息

##### uname

```shell
uname []
			-a		系统所有相关信息
			-r		内核版本
			-s		内核名称
```

![image-20201010161542357](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010161542.png)

##### 系统位数

```shell
file /bin/ls
```

使用`file`命令查看一个系统外部命令,就会顺带显示位数

![image-20201010161717237](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010161717.png)

##### 查询当前linux发行版本

```shell
lsb_release -a
```

![image-20201010161912535](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010161912.png)

##### 进程调用文件

```shell
lsof []
			-c 字符串			只列出字符串开头的进程打开的文件
			-u 用户名			只列出某个用户的进程打开的文件
			-p pid				列出某个PID进程打开的文件
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010162231.png" alt="image-20201010162231099" style="zoom: 62%;" />

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010162301.png" alt="image-20201010162301018" style="zoom:67%;" />



## 系统定时任务

类似win下任务计划

#### crond服务管理与访问控制(属xinetd)

```shell
/sbin/service crond start
/sbin/service crond stop
/sbin/service crond restart
/sbin/service crond reload
或者
systemctl restart crond.service  
systemctl status crond.service		#状态检查

systemctl enable crond.service		#自启动设置
或者setup 内+*
systemctl is-enabled crond.service		#状态查询
```

![image-20201010163719701](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010163719.png)

#### crontab设置定时任务
```shell
crontab [选项]
				-e		编辑crontab定时任务
				-l		查询
				-r		删除当前用户的所有crontab任务，删一行可用vim
```
```shell
格式:
* * * * * command
|_|_|_|_|____|________一小时中的第几分钟0-59
	|_|_|_|____|________一天当中的第几小时0-23
		|_|_|____|________一个月当中的第几天1-31
			|_|____|________一年当中的第几月1-12
				|____|________一周当中的星期几0-7,0&7均代表星期日
        		 |________定时任务/命令
即
分钟 小时 天 月 周 命令
```

特殊符号

```shell
*		指任意
,		不连续时间,eg."0 8,12,16 * * * 命令"指每天8:00,12:00,16:00执行
-		连续时间	0 5 * * 1-6 命令		周一-周6的5:00执行
*/n		每隔多久执行
```

- 注意像表示整点执行的时候第一位需写0,否则写*表示每分钟执行

例子

```shell
10 * * * * 命令			每小时第10分钟
45 22 * * * 命令		22:45分执行命令
0 17 * * 1 命令			每星期一17:00执行命令
0 5 1,15 * * 命令		每月1号和15号5:00执行
40 4 * * 1-5 命令		周一-周5 4:40执行
*/10 4 * * * 命令		每天凌晨4点,每10分钟执行
0 0 1,15 * 1 命令		每月1号和15号,每周1的00:00执行命令

*/5 * * * /bin/echo "ll" >> /tmp/test		每5分钟写"ll"入文件test
5 5 * * 2 /sbin/shutdown -r now					每周2 05:05重启
0 5 1,10,15 * * /root/sh/autobak.sh			每月1，10，15号05:00执行脚本
```

- aurobak.sh    

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010172330.png" alt="image-20201010172330272" style="zoom:70%;" />

  crontab中%有特殊含义，故脚本中转义 %y%m%d年月日

  脚本将日期，文件大小写入配置文件，进入备份目录下，将备份文件和日志文件压缩（输出丢入回收站），删除日志文件

- 注意像eg7,星期几和每月几号(建议)最好不要再同一个定时任务中出现,容易使管理员混淆
- 定时任务最小识别单位分钟
- 定时任务会判断系统是否繁忙，可能不会立刻执行


