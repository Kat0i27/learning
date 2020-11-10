---
title: linux基础_1.常用命令
date: 2020-10-11 09:21:08
tags: linux
categories: linux基础
---

### 目录处理命令

#### ls

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011104521.png" alt="image-20201011104521670" style="zoom: 50%;" />

<!--more-->

   ```
ls  []
		-a	显示隐藏文件
   	-h	人性化阅读，文件大小转为MB/GB，原为数据块
   	-l	相当于ll，长列表类型展示文件信息
   	-d	显示目录
   ```

- ls命令查询得到的文件大小部分

  文件--文件大小

  目录--目录文件名占用的字节数，并非目录内数据大小

`ls -al `和 `ls -alh`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011104543.png" alt="image-20201011104543195" style="zoom: 45%;" />

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011105048.png" alt="image-20201011105048302" style="zoom:48%;" />

`ls -dl lib	`	以长列表形式显示目录lib

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011104656.png" alt="image-20201011104656879" style="zoom:58%;" />


#### mkdir和rmdir

   ```
mkdir -p 递归创建目录
rmdir 删除目录 
rm -rf  强制删除						
   ```

`mkdir -p test/test1`	，假设test目录不存在，则递归创建，先创建test,再创建test1

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011105801.png" alt="image-20201011105801725" style="zoom:67%;" />

如果目录下有内容，删除父目录会报错

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011110231.png" alt="image-20201011110231944" style="zoom:60%;" />

原可用`rmdir -f`强制删除，但在centos7中不再支持该选项。不过使用`rm -rf`也可以达到同样的效果

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011110430.png" alt="image-20201011110430489" style="zoom:60%;" />



#### pwd显示当前目录

#### cp拷贝

   ```
cp	[] 源文件 目标文件路径
		-r	拷贝目录
   	-p	拷贝属性
   ```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011110802.png" alt="image-20201011110801998" style="zoom:50%;" />

拷贝目录test到当前路径下` cp -r test test1`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011111141.png" alt="image-20201011111141396" style="zoom:50%;" />

但是两个目录属性不同(创建时间不一)，只复制了内容。使用`cp -pr test test2`拷贝得到

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011111700.png" alt="image-20201011111700328" style="zoom:50%;" />

复制目录不加`-r`参数会出现如下报错：cp: omitting directory ‘test’

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011111737.png" alt="image-20201011111713682" style="zoom:60%;" />



#### rm

   ```
rm	-r	删除目录
   	-f  强制删除
   ```

#### ln链接

>摘自[linux命令大全-ln](https://man.linuxde.net/ln)
>
>Linux具有为一个文件起多个名字的功能，称为链接。被链接的文件可以存放在相同的目录下，但是必须有不同的文件名，而不用在硬盘上为同样的数据重复备份。另外，被链接的文件也可以有相同的文件名，但是存放在不同的目录下，这样只要对一个目录下的该文件进行修改，就可以完成对所有目录下同名链接文件的修改。对于某个文件的各链接文件，我们可以给它们指定不同的存取权限，以控制对信息的共享和增强安全性。文件链接有两种形式，即硬链接和符号链接。
>
>**硬链接**
>
>​		创建硬链接后，己经存在的文件的I节点号（Inode）会被多个目录文件项使用。一个文件的硬链接数可以在目录的长列表格式的第二列中看到，无额外链接的文件的链接数为l。
>
>​		在默认情况下，ln命令创建硬链接。ln命令会增加链接数，[rm](http://man.linuxde.net/rm)命令会减少链接数。一个文件除非链接数为0，否则不会从文件系统中被物理地删除。
>
>对硬链接有如下限制：
>
>- 不能对目录文件做硬链接。
>- 不能在不同的文件系统之间做硬链接。就是说，链接文件和被链接文件必须位于同一个文件系统中。
>
>**符号链接/软链接**
>
>符号链接也称为软链接，是将一个路径名链接到一个文件。这些文件是一种特别类型的文件。事实上，它只是一个文本文件（如图中的abc文件），其中包含它提供链接的另一个文件的路径名。另一个文件是实际包含所有数据的文件。所有读、写文件内容的命令被用于符号链接时，将沿着链接方向前进来访问实际的文件。
>
>​		与硬链接不同的是，符号链接确实是一个新文件，当然它具有不同的I节点号；而硬链接并没有建立新文件。
>
>​		符号链接没有硬链接的限制，可以对目录文件做符号链接，也可以在不同文件系统之间做符号链接。
>
>符号链接保持了链接与源文件或目录之间的区别：
>
>- 删除源文件或目录，只删除了数据，不会删除链接。一旦以同样文件名创建了源文件，链接将继续指向该文件的新数据。
>- 在目录长列表中，符号链接作为一种特殊的文件类型显示出来，其第一个字母是l。
>- 符号链接的大小是其链接文件的路径名中的字节数。
>- 当用`ln -s`命令列出文件时，可以看到符号链接名后有一个箭头指向源文件或目录，例如`lrwxrwxrwx … 14 jun 20 10:20 /etc/motd->/original_file`其中，表示“文件大小”的数字“14”恰好说明源文件名`original_file`由14个字符构成。
>
>

   ```
ln [选项] target link
   -s 生成软连接，类似win快捷方式，权限ugo均rwx,文件小，删除源文件软链接失效
   ```

- 默认无参数时生成硬链接
- target：指定连接的源文件。创建软连接，“源文件”可以是文件或者目录。创建硬连接时，则“源文件”参数只能是文件；
- 用`ln -s`命令建立符号链接时，源文件最好用绝对路径名。这样可以在任何工作目录下进行符号链接。而当源文件用相对路径时，如果当前的工作路径与要创建的符号链接文件所在路径不同，就不能进行链接。

##### 创建一个硬链接实例

将目录/root/temp/test下的文件aa链接到/root/temp/test2下的文件bb(执行命令前，bb并不存在)

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011113105.png" alt="image-20201011113105060" style="zoom:50%;" />

查看两个文件aa和bb，-i参数表示显示Node节点号。可见两个文件节点号相同，链接数+1（无额外链接的文件链接数=1），文件类型位置没有特殊标记。

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011113204.png" alt="image-20201011113204473" style="zoom:67%;" />



##### 创建一个软链接实例

将目录test1链接到test2下的符号链接文件ab(无需事先创建，执行命令时写明链接文件路径即可)，即使./test2/ab指向目录./test1。

```
ln -s /root/temp/test1 /root/temp/test2/ab
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011120135.png" alt="image-20201011115420891" style="zoom:50%;" />

此时test1中存放的文件可通过软链接文件ab访问。但实际上两个目录inode不同，证明符号链接是一个新文件。文件类型为l,代表软链接

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011120136.png" alt="image-20201011115810534" style="zoom:67%;" />

目录内文件inode相同是因为通过ab访问的文件aa的过程就是ab沿着符号链接的方向访问实际目录test1内的aa。



#### 目录作用

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011121001.png" alt="image-20201011121001014" style="zoom:67%;" />

|    目录    | 作用                                                         |
| :--------: | ------------------------------------------------------------ |
|   /bin/    | 从存放系统命令（$#）                                         |
|   /sbin/   | 与系统环境相关的命令（#)                                     |
|   /usr/    | 系统软件资源目录                                             |
| /usr/bin/  | 存放系统命令（与系统启动无关）                               |
| /usr/sbin/ | 根系统文件中不必要的管理命令                                 |
|   /boot/   | 系统启动目录（内核文件，启动引导程序，group文件）            |
|   /dev/    | 设备文件保存位置                                             |
|   /etc/    | 配置文件保存位置                                             |
|   /var/    | 动态数据存放位置（缓存，日志，软件运行产生的文件）           |
|   /proc/   | 虚拟文件系统，存在内存中，保存系统内核，进程，外部设备状态，网络状态灯<br />eg./proc/cpuinfo    cpu, /proc/devices    设备驱动列表，/proc/filesystem文件系统列表, /proc/net/网络协议 |
|   /sys/    | 虚拟文件系统，保存内核相关信息                               |
|   /root/   | root用户家目录                                               |
|   /srv/    | 服务数据目录                                                 |
|   /tmp/    | 临时存放文件位置，所有用户均可访问                           |

   

### 文件处理命令

#### find	

```shell
find  目录 条件 文件名
					-name		#名字配合通配符使用，*?
   		 	  -iname		#不区分大小写
   		 	  -a -o			#且 或    
   		  	-size +50M -size -100M	#查找文件>50M且<100M的文件
				  -type f d l
          -inum n		#节点	
					-amin/cmin/mmin				#n分钟前被访问/文件数据元(例如权限)被修改/前曾被修改内容
          -atime 50		#最近50天访问的文件
          -mtime +50 -mtime -100	#查找修改时间>50且<100的文件										
					-perm 0777	#查找权限为777的所有文件
					-user root -name test.c	#查找所有者为root的所有文件,文件名为test.c的所有文件
   				-group	developer   				                
          -empty		#寻找文件大小为0 Byte的文件，或目录下没有任何子目录或文件的空目录
          -exec/ok	#	找出文件后执行指定命令，搭配其他命令使用
```

- 不指明目录则在当前目录下寻找

##### 文件name或正则匹配regex

  `find .`列出当前目录及子目录下所有文件和文件夹

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011131402.png" alt="image-20201011130829343" style="zoom:50%;" />

`find / -name init`   搜索文件名为init的文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011123658.png" alt="image-20201011123658464" style="zoom:55%;" />

`find / -name *init*`	查找文件名中包含init的文件。通配符*，匹配任意个字符

`find / -name *init???` 查找文件名为 "任意字符+init+三个字符"的文件。通配符？，匹配一个任意字符

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011123815.png" alt="image-20201011123815581" style="zoom:50%;" />

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011125422.png" alt="image-20201011125422850" style="zoom:50%;" />

`find . -name "*.txt" -o -name "*.pdf" `当前目录及子目录下查找所有以.txt和.pdf结尾的文件

`find . ! -name "*.txt"`	当前目录下不以.txt结尾的文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011133439.png" alt="image-20201011133439383" style="zoom:50%;" />

`find /usr/ -path "*local"`	匹配文件路径或者文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011131601.png" alt="image-20201011131600994" style="zoom:67%;" />

`find . -regex ".*\(\.txt\|\.pdf\)$"`基于正则表达式匹配文件路径，加i可忽略大小写

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011133006.png" alt="image-20201011133006434" style="zoom:67%;" />

##### 根据类型匹配type

f 文件 d目录 l 链接

`find / -name init??? -type f`			查找文件名为init+3个任意字符的文件(排除目录)

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011130126.png" alt="image-20201011130126150" style="zoom:50%;" />

##### 根据文件大小匹配size

b块（512字节）/c字节/w字(字)/k/M/G

+大于-小于不指明则等于

`find / -size +50M -size -100M`			搜索/下>50且<100的文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011130016.png" alt="image-20201011130015998" style="zoom:50%;" />

`find / -mtime +50 -mtime -100`	查找修改时间>50且<100的文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011130409.png" alt="image-20201011130409365" style="zoom:67%;" />

##### 文件时间戳检索[a/c/m]min/time

**访问时间**（-atime/天，-amin/分钟）：用户最近一次访问时间。
**修改时间**（-mtime/天，-mmin/分钟）：文件最后一次修改时间。
**变化时间**（-ctime/天，-cmin/分钟）：文件数据元（例如权限等）最后一次修改时间。

+大于，-小于，不指明即等于

`find . -type f -atime 7`     搜索恰好在七天前被访问过的所有文件

`find . -type f -atime +7`	搜索超过七天内被访问过的所有文件

`find . -type f -atime -7`		搜索最近七天内被访问过的所有文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011134435.png" alt="image-20201011134435148" style="zoom:50%;" />

` find . -type f -amin +50`		搜索访问时间超过50分钟的所有文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011135149.png" alt="image-20201011135149268" style="zoom:50%;" />

`find . -type f -newer test/aa`		找出比aa修改时间更长/新的所有文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011134759.png" style="zoom:50%;" />

##### 删除匹配文件

` find . -type f \( -name "*.txt" -o -name "*.pdf" \) -delete`

删除当前目录及子目录下查找所有以.txt和.pdf结尾的文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011135639.png" alt="image-20201011135638996" style="zoom: 50%;" />



##### 根据perm(权限),user,group匹配

当前目录下搜索出权限为777的文件，这里bb是aa的硬链接

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011140110.png" alt="image-20201011140110264" style="zoom:67%;" />

 `find . -type f -name "*.php" ! -perm 644`		找出当前目录下权限不是644的php文件

`find . -type f -user jen`		找出当前目录用户jen拥有的所有文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011140540.png" alt="image-20201011140540426" style="zoom:60%;" />

`find . -type f -group jen`		找出当前目录用户组jen拥有的所有文件

##### 搜索文件后执行命令 exec/ok

-ok作用与-exec相同，但是ok需要确认执行的过程

`find / -type f -perm 777 -exec/-ok	rm -f {} \;`	#删除/root/temp下权限为777的文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011141309.png" alt="image-20201011141309008" style="zoom:50%;" />

`find -type f -name "*.mp3" -exec rm -f {} \;`		删除当前目录下后缀名为.mp3的文件



##### empty搜索空文件/目录

`find /root/temp -type f -empty	`#        查找目录下所有空文件	  

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011141629.png" alt="image-20201011141629750" style="zoom:55%;" />

#### locate

   ```shell
locate	#在文件库中查找，快，可能不即时
updatedb	#更新数据库
					-i	忽略大小写
   ```

`locate pwd`	查找与pwd相关的所有文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011143004.png" alt="image-20201011143004122" style="zoom:60%;" />

`locate  /etc/sh`	#搜索etc目录下所有以sh开头的文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011143053.png" alt="image-20201011143053666" style="zoom:70%;" />


#### whereis

   搜索方法类似locate,比find快。可执行文件b、源代码文件s、帮助文件m在文件系统中的位置。

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011143621.png" alt="image-20201011143621611" style="zoom: 55%;" />



#### which

`which 命令`  显示命令路径(PATH变量)，别名

`which ls`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011143214.png" alt="image-20201011143213988" style="zoom:65%;" />


#### grep

```shell
grep -i(忽略大小写)	-v 查找不匹配指定字符串的行	
```

##### grep规则表达式说明

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011151728.png" alt="image-20201011151728668" style="zoom: 40%;" />

##### 实例

过滤文件注释行			`grep ^[^#] /etc/xinetd.conf`或`grep -v ^# /etc/xinetd.conf    `

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011145017.png" alt="image-20201011145017754" style="zoom:50%;" />        <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011145106.png" alt="image-20201011145106365" style="zoom:47%;" /> 



` cat myfile|grep ^[^u]`		查找非u开头的行内容

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011144849.png" alt="image-20201011144848968" style="zoom:60%;" />

`ps -ef|grep svn`		查找指定进程

加-c参数查找指定进程的个数

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013120155.png" alt="image-20201011145449302" style="zoom:60%;" />



  ` cat test.txt | grep -f test2.txt`			指定规则文件，其内容含有一个或多个规则样式，让grep查找符合规则条件的文件内容，格式为每行一个规则样式

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011145838.png" alt="image-20201011145838697" style="zoom:60%;" />

按照test2的格式匹配test中符合要求的行

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011145947.png" alt="image-20201011145924293" style="zoom:67%;" />

`grep -n 'linux' test.txt`		从文件中查找含有关键字的行并显示行号

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011150308.png" alt="image-20201011150308876" style="zoom:67%;" />

`cat test.txt | grep -E"ed|at"`	#显示包含ed或at的字符行

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011150414.png" alt="image-20201011150414885" style="zoom:67%;" />



`grep '[a-z]\{7\}' *.txt`	#当前目录下以.txt 结尾的文件中的所有包含至少有7个连续小写字符的字符串所在行，因为在bash中{}有特殊含义使用需要转义

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011150533.png" alt="image-20201011150533406" style="zoom:67%;" />



### 权限管理命令

#### chmod

   ```shell
chmod [{ugoa}{+-=}{rwx}][文件或目录]
   ```
`chmod g-w,o-w test`		

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011152119.png" alt="image-20201011152119326" style="zoom: 50%;" />

`chmod 777 myfile`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011152229.png" alt="image-20201011152229768" style="zoom: 50%;" />

`chmod -R`			目录权限递归一次修改

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011152615.png" alt="image-20201011152615452" style="zoom: 50%;" />

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011152840.png" alt="image-20201011152828702" style="zoom: 50%;" />

- 目录权限&目录下文件权限不同。

#### chown

   ```shell
chown [用户]  [目录/文件]	#改变文件所有者，只有管理员可改
   ```

`chown root myfile`	#文件所有者设置为root

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011153143.png" alt="image-20201011153143018" style="zoom:50%;" />

`chown root:root myfile`	#同时修改文件所有者root,所属组root

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011153242.png" alt="image-20201011153242285" style="zoom:50%;" />

useradd
passwd

#### chgrp   改变文件所属组

如果用户不是该文件的文件主或超级用户(root)，则不能改变该文件的组。

**默认权限**	创建者=文件所有者	缺省组(默认组，与创建者同名)=文件所有组

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011153520.png" alt="image-20201011153520914" style="zoom:50%;" />



#### umask 查看设置缺省权限

`umask -S `#查看新建目录缺省权限。文件-x，   linux新建文件默认没有执行权限				

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011153920.png" alt="image-20201011153920664" style="zoom:67%;" />

权限首位0 为特殊权限数字

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011154058.png" alt="image-20201011154058370" style="zoom:67%;" />





### 帮助命令

#### man

>man 可以查询不同类型的帮助手册，当目标存在多个不同类型的帮助手册时，我们可以指定要查找的手册类型，也可以不指定，此时 man 会搜索所有类型的帮助手册，但是只会按照预定义的顺序展示第一个。预定义的顺序可以使用环境变量 $MANSECT 或配置文件 /usr/local/etc/man_db.conf 中的 SECTION 指令指定，默认为：
>
>`1 8 3 2 5 4 9 6 7`
>
>1	可执行程序或 Shell 命令
>
>5	文件格式和约定，如 /etc/passwd


   ```shell
man 命令	#NAME 作用 /选项
		配置文件	#NAME 存放信息  文件格式
   ```

`man 5 passwd`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011155252.png" alt="image-20201011155252025" style="zoom:47%;" />



#### whatis

   ```shell
whatis 命令	#显示作用（简）
   ```

`whatis cp`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011155409.png" alt="image-20201011155409408" style="zoom:50%;" />



#### apropos

   ```shell
apropos 配置文件 	#显示配置文件作用
   ```

`apropos  ntp.conf`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011155537.png" alt="image-20201011155537873" style="zoom:67%;" />

#### --help 查看常用选项

#### info

#### help

#### date与man date

`man date`		得到日期格式

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011155649.png" alt="image-20201011155649167" style="zoom:67%;" />

根据指定格式MMDDhhmm修改时间

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011155808.png" alt="image-20201011155808566" style="zoom:67%;" />

恢复标准时间		`ntpdate pool.ntp.org`



### 用户管理命令

#### useradd&passwd

`useradd u1`添加用户u1		`passwd`修改密码

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011160305.png" alt="image-20201011160305452" style="zoom:67%;" />

管理员外的普通用户密码需要满足一定复杂度要求

#### who

登录用户信息

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011160458.png" alt="image-20201011160458715" style="zoom:67%;" />

列2为终端号，pts/0-255表示远程/虚拟终端，tty1-7表示本地

#### w(详细版who)

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011160640.png" alt="image-20201011160640190" style="zoom:67%;" />

第一行：开机时间点，已开机22h32分钟，登录用户，平均负载（5/10/15min）

  

### 解压缩命令

#### gzip	(压缩率大)

```shell
.gz
解压1：gunzip FileName.gz
解压2：gzip -d FileName.gz
压缩：gzip FileName

gzip -rf temp		
gunzip -rf temp或 gzip -drf temp  
#-r递归压缩，用于压缩目录;-f强制压缩，忽略链接文件警告;-v显示指令执行过程。
```
```shell
.tar.gz
解压：tar zxvf FileName.tar.gz
压缩：tar zcvf FileName.tar.gz DirName
```


#### tar

```shell
.tar
解包：tar -xvf FileName.tar									#-v显示涉及的文件;-f指定压缩文件
打包：tar -cvf FileName.tar DirName	
```

#### zip

```shell
.zip
解压：unzip FileName.zip
压缩：zip FileName.zip DirName
```

#### bzip2

```shell
.bz2
解压1：bzip2 -d FileName.bz2
解压2：bunzip2 -k FileName.bz2				#-k 解压缩后保留原文件
压缩： bzip2 -z FileName


```
```shell
.tar.bz2
解压：tar -jxvf FileName.tar.bz2
压缩：tar -jcvf FileName.tar.bz2 DirName
```

### 网络命令

#### write 用户名

   “写信/聊天”，ctrl+D保存结束聊天

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011164547.png" alt="image-20201011164547883" style="zoom:67%;" />

#### wall 广播

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011165011.png" alt="image-20201011165011584" style="zoom:50%;" />

#### ping



#### ifconfig查看网卡配置信息

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011165207.png" alt="image-20201011165207660" style="zoom: 50%;" />

- ens33是第一块网卡
- UP（代表网卡开启状态）RUNNING（代表网卡的网线被接上）MULTICAST（支持组播）MTU:1500（最大传输单元）：1500字节

- inet addr 用来表示网卡的IP地址，此网卡的 IP地址是 192.168.72.88，广播地址， Bcast:192.168.72.255，掩码地址Mask:255.255.255.0 
- 连接类型：Ethernet（以太网）HWaddr（硬件mac地址）
- 接收、发送数据包情况统计
- 接收、发送数据字节数统计信息
- lo表示本地回环地址，一般用于测试网络程序



##### 启动关闭指定网卡

练习的时候，ssh登陆linux服务器操作要小心，关闭了就不能开启了，除非你有多网卡。

```shell
ifconfig ens33 up
ifconfig ens33 down
```

##### 为网卡配置ip地址

```shell
ifconfig ens33 198.168.8.250		#修改网卡ens33 ip为198.168.8.250
ifconfig ens33 192.168.120.56 netmask 255.255.255.0 
 ifconfig ens33 192.168.120.56 netmask 255.255.255.0 broadcast 192.168.120.255
```

##### 为网卡配置和删除ipv6地址

```shell
ifconfig ens33 add 33ffe:3240:800:1005::2/64
ifconfig ens33 del 33ffe:3240:800:1005::2/64
```

##### 修改Mac地址

```shell
ifconfig ens33 hw ether 00:AA:BB:CC:DD:EE
```



#### mail  

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011170701.png" alt="image-20201011170700945" style="zoom:50%;" />

发送邮件 `mail 用户名`

接收：`mail` 查看邮件信息后回车显示邮件详情

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011170829.png" alt="image-20201011170829512" style="zoom:67%;" />

看完后ctrl+D保存退出

#### last 目前与过去登入系统的用户信息

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011171124.png" alt="image-20201011171124412" style="zoom: 50%;" />



#### lastlog特定用户登陆时间

`lastlog -u uid`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011171433.png" alt="image-20201011171433068" style="zoom:50%;" />



#### traceroute

`tarceroute hostname`

#### netstat

`netstat -rn`	#查看本机路由表

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011171904.png" alt="image-20201011171904725" style="zoom:67%;" />

` netstat -tuln`		tcp和udp服务监听

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011172039.png" alt="image-20201011172039429" style="zoom:50%;"/> 

`netstat -an`	#显示所有网络连接

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011172315.png" alt="image-20201011172315583" style="zoom:50%;" />

- netstat的输出结果可以分为两个部分：

  一个是Active Internet connections，称为有源TCP连接，其中"Recv-Q"和"Send-Q"指的是接收队列和发送队列。这些数字一般都应该是0。如果不是则表示软件包正在队列中堆积。这种情况只能在非常少的情况见到。

  另一个是Active UNIX domain sockets，称为有源Unix域套接口(和网络套接字一样，但是只能用于本机通信，性能可以提高一倍)。

  Proto显示连接使用的协议,RefCnt表示连接到本套接口上的进程号,Types显示套接口的类型,State显示套接口当前的状态,Path表示连接到套接口的其它进程使用的路径名。

- 套接口类型

  -t ：TCP

  -u ：UDP

  -raw ：RAW类型

  --unix ：UNIX域类型

  --ax25 ：AX25类型

  --ipx ：ipx类型

  --netrom ：netrom类型

- **状态说明：**

  **LISTEN**：侦听来自远方的TCP端口的连接请求

  SYN-SENT：再发送连接请求后等待匹配的连接请求（如果有大量这样的状态包，检查是否中招了）

  SYN-RECEIVED：再收到和发送一个连接请求后等待对方对连接请求的确认（如有大量此状态，估计被flood攻击了）

  **ESTABLISHED**：代表一个打开的连接

  FIN-WAIT-1：等待远程TCP连接中断请求，或先前的连接中断请求的确认

  FIN-WAIT-2：从远程TCP等待连接中断请求

  CLOSE-WAIT：等待从本地用户发来的连接中断请求

  CLOSING：等待远程TCP对连接中断的确认

  LAST-ACK：等待原来的发向远程TCP的连接中断请求的确认（不是什么好东西，此项出现，检查是否被攻击）

  TIME-WAIT：等待足够的时间以确保远程TCP接收到连接中断请求的确认

  CLOSED：没有任何连接状态

#### ~~setup 配置网络~~ nmtui

`setup`在centos7版本里已经没有网络配置选项，使用`nmtui`进入

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011173835.png" alt="image-20201011173835711" style="zoom:50%;" />

进入编辑

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011174044.png" alt="image-20201011174043984" style="zoom: 40%;" />

回车进入配置网卡

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011174120.png" alt="image-20201011174120060" style="zoom:50%;" />

回到网络编辑界面激活

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011174214.png" alt="image-20201011174214088" style="zoom:50%;" />



#### mount [-t文件系统]  设备文件名

`mount -t 文件系统 设备文件名 挂载点/mnt/xxx`

1. `fdisk -l` 查看设备文件名

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011174622.png" alt="image-20201011174621982" style="zoom:67%;" />

2. 插入可移动设备(这里用u盘演示)

   出现提示

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011175340.png" alt="image-20201011175340344" style="zoom:50%;" />

   关机修改虚拟机设置usb兼容3.1,重启即可

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011175643.png" alt="image-20201011175630756" style="zoom:50%;" />

   

检查与虚拟机连接状态，若未连接(连接到主机)，

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011174758.png" alt="image-20201011174758836" style="zoom:50%;" />

linux系统不能识别ntfs/exfat文件系统，检查u盘类型(win下查看u盘属性)，安装支持

    mount unknown filesystem type ntfs
    解决：安装支持包
    wget https://tuxera.com/opensource/ntfs-3g_ntfsprogs-2017.3.23.tgz
    tar -zxf ntfs-3g_ntfsprogs-2017.3.23.tgz
    cd ntfs-3g_ntfsprogs-2017.3.23
    ./configure;make;make install 
    
    mount -t ntfs-3g 设备文件名 挂载点
    
    exfat
    yum install -y http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
    yum install exfat-utils fuse-exfat
    mount -t exfat 设备文件名 挂载点

重新检查分区情况，得到u盘设备文件名

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011180006.png" alt="image-20201011180006769" style="zoom:50%;" />

在/mnt下创建目录空usb来挂载u盘

`mount -t ntfs-3g 设备文件名 挂载点` 	（ntfs）

`mount -t exfat /dev/sdb1 /mnt/usb`	(exfat)

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011185213.png" alt="image-20201011185213349" style="zoom:67%;" />

可通过挂载点访问u盘

取消挂载

`umount 设备文件名/挂载点`



出现的一些问题：

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011180952.png" alt="image-20201011180952149" style="zoom:67%;" />

提示设备错误，连接主机，查看了下u盘属性发现是exfat格式，linux识别不了，上面命令指定的文件系统也不对。好吧，装一下exfat的支持

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011183437.png" alt="image-20201011183437281" style="zoom:67%;" />

报错挂在目标已使用，额实际上已经挂载了，这里出问题的原因是我在另一个终端正在换源造成的，结束后就能正常挂载了



### 关机重启命令

#### shutdown

   ```shell
shutdown -c 取消前一个关机命令
shutdown -h 关机
shutdown -r 重启
   ```

#### halt

#### poweroff

#### logout

#### reboot

#### init 0和init 6

- 系统运行级别

  0关机，1单用户，2不完全多用户，3完全多用户，4未分配，5图形界面，6重启

   ```shell
cat　/etc/inittab
runlevel	#查看当前系统运行级别
   ```

   

### 其他小问题

终端提示符显示的是-bash-4.2# 而不是root@主机名 + 路径的显示方式原因是root在/root下面的几个配置文件丢失，丢失文件如下：1、.bash_profile2、.bashrc以上这些文件是每个用户都必备的文件。使用以下命令从主默认文件重新拷贝一份配置信息到/root目录下
cp /etc/skel/.bashrc /root/

cp /etc/skel/.bash_profile  /root/

然后重新登录就恢复正常了。

检查后发现是因为额我把这部分文件压缩了，解压后再次打开终端就正常了