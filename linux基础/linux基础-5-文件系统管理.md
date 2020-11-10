---
title: linux基础_5.文件系统管理
date: 2020-10-11 09:22:17
tags: linux
categories: linux基础
---

### 分区

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011093730.png" alt="image-20201001135647240" style="zoom:50%;" />

<!--more-->

#### 分区划分实例

##### 划分eg1

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011093731.png" alt="image-20201001140530228" style="zoom:50%;" />

##### 划分eg2

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011093732.png" alt="image-20201001140838652" style="zoom:50%;" />

即便主分区+扩展分区<4，逻辑分区也只能从sd?5开始




##### 设备文件名命名规则

| 设备              | 设备文件名                                      |
| ----------------- | ----------------------------------------------- |
| IDE硬盘           | /dev/hd[a-d]                                    |
| SCSI/SATA/USB硬盘 | /dev/sd[a-p]                                    |
| u盘               | /dev/sd[a-p]                                    |
| 软驱              | /dev/fd[0-1]                                    |
| 打印机            | 25针：/dev/lp[0-2]<br />USB：/dev/usb/ lp[0-15] |
| 鼠标              | USB:/dev/usb/mouse[0-15]<br />PS2: /dev/psaux   |
| CD-ROM/DVD        | /dev/cdrom                                      |
| 当前鼠标          | /dev/mouse                                      |
| 磁带机            | IDE:/dev/ht0<br />SCSI:/dev/st0                 |

##### 硬盘设备命名规则

| **设备文件** | **对应设备**                         |
| ------------ | ------------------------------------ |
| sda          | a 表示第一个出现的硬盘，代表一个硬盘 |
| sda1         | 第一个硬盘中的第一个分区             |
| sda2         | 第一个硬盘中的第二个分区             |
| sda3         | 第一个硬盘中的第三分区               |

| **设备文件** | **对应设备**                         |
| ------------ | ------------------------------------ |
| sdb          | b 表示第二个出现的硬盘，代表一个硬盘 |
| sdb1         | 第二个硬盘中的第一个分区             |
| sdb2         | 第二个硬盘中的第二个分区             |

------------------

### 文件系统

#### 文件系统	ext->ext4版本发展

| ext  |                                                              |
| ---- | ------------------------------------------------------------ |
| ext2 | 1. ext2升级版，1993年发布<br />2. red hat linux7.2以前默认文件系统ext2<br />3. 最大支持16TB分区，2TB文件 |
| ext3 | 1. 与ext2最大区别：带日志功能，系统突然停止时可提高文件系统可靠性<br />2. 最大支持16TB分区，2TB文件 |
| ext4 | 1. 在性能，伸缩性，可靠性方面有重大改进<br />2. 向下兼容ext3，无限数量子目录，extents连续数据块，多块/延迟/持久预分配，快速fsck，日志校验，无日志模式，在线碎片整理，inode增强，默认启用barrier...<br />3. 最大1EB文件系统分区，16TB文件（1EB=1024PB=1024*1024TB）<br />4.默认文件系统entos6.3 |



### 文件系统常用命令

#### 文件系统查看 df

```shell
df [选项]	[挂载点]
	-a	显示所有文件系统信息，包括特殊文件系统（eg./proc, /sysfs等)
	-h	人性化显示，KB，MB，GB
	-T	显示文件系统类型
	-m	以MB为单位显示容量
	-k	  KB(默认)
```

-h修改 文件大小单位

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012141658.png" alt="image-20201012141658507" style="zoom:50%;" />

-a参数可查看所有文件系统，包括虚拟文件系统

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012141850.png" alt="image-20201012141850106" style="zoom:50%;" />



#### 统计目录或文件大小du

ll -h 目录命令统计一级文件名+子文件名占用空间大小，不统计数据，与du有所区别

```shell
du [选项]	[目录/文件名]
		-a	显示每个子文件磁盘占用量，默认只统计子目录
		-h	人性化显示占用量
		-s	统计总占用量，不列出子文件/目录占用量
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012141935.png" alt="image-20201012141935934" style="zoom: 60%;" />

du -sh在统计前需扫描目录，属于高负载命令（大规模数据读写/扫描）

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012142314.png" alt="image-20201012142314204" style="zoom:67%;" />

##### 注意

**Q:df与du检测出的`/`占用空间大小不同？**

du检测/得到的大小是9.1G，df检测得到的大小是8.1G

**S:du与df区别：**[du与df](https://www.cnblogs.com/f-ck-need-u/p/8659301.html)

- df：面向文件系统，考虑文件占用的空间+系统/进程/命令/程序占用空间（eg.文件删除但进程调用没有释放空间），多用于统计剩余空间。读取每个分区的superblock获取空闲块，已使用数据块，计算空闲空间和已使用空间

- du：面向文件，只计算文件/目录占用空间，多用于统计文件占用大小(包括挂载文件。根据命令stat统计文件占用和。

  一般来说，df要比du大

  

#### 文件系统修复命令fsck

```shell
fsck [选项]	分区设备文件名
		-a:不同显示用户提示，自动修复文件系统
		-y:自动修复。与-a作用一致，只不过某些文件系统支支持-y
```

重启自动进行,用户一般不设置

#### 检测磁盘状态命令dumpe2fs

```shell
dumpe2fs	分区设备文件名
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012173649.png" alt="image-20201012173649023" style="zoom:50%;" />




#### 挂载命令，光盘/u盘mount

##### 查询与自动挂载

```shell
mount [-l]		查询系统中已挂载设备，-l显示卷标名
			-a			依据配置文件/etc/fstab内容自动挂载
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012174019.png" alt="image-20201012174019488" style="zoom: 50%;" />



##### 挂载命令

```shell
mount [-t 文件系统] [-L 卷标名]	\ [-o 特殊选项]  设备文件名 挂载点
			-t 文件系统		加入文件系统类型指定挂载类型，eg.ext3,ext4,ios9660
			-L 卷标名		挂载指定卷标的分区，而非安装设备文件名挂载
			-o 特殊选项		指定挂载的额外选项，多个选项，分割
			eg: -o remount,rw 挂载点
					-o exec 挂载点
			
```

- []中内容非必须

- 特殊选项：

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011093735.png" alt="image-20201001161444801" style="zoom: 50%;" />
  
  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012174855.png" alt="image-20201012174855356" style="zoom:50%;" />
  
  



##### 挂载光盘

光盘，u盘，移动硬盘不会自动挂载，因为不能保证每次开机都连接到设备。需要手动挂载。但现在较新的linux系统中光驱设备可自动挂载（在/media/cdrom下）

`mount`查看可见挂载信息,通过挂载点可查看光盘内容

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012174956.png" alt="image-20201012174956453" style="zoom:67%;" />

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012175127.png" alt="image-20201012175127416" style="zoom: 70%;" />

若没有自动挂载可在Workstation-虚拟机-设置中勾选已连接（不选相当于未上电），选择光盘文件保存

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011093734.png" alt="image-20201001145530189" style="zoom: 50%;" />



终端中新建挂载点挂载。（iso9660 是光盘的默认文件系统。由于linux系统可以自动识别光盘的文件系统，故“-t iso9660”也可以省略不写）

```shell
mkdir /mnt/cdrom		#建立挂载点
mount -t iso9660 /dev/cdrom /mnt/cdrom/		#挂载光盘
mount /dev/sr0 /mnt/cdrom		#设备文件名/dev/sr0与/dev/cdrom(软链接)等同
```

##### 卸载命令

```shell
umount 设备文件名/挂载点	(一旦挂载，二者建立连接，断开哪一边效果等同)
umount /mnt/cdrom
```

##### 挂载u盘

```shell
fdisk -l	#查看设备文件名
mount -t vfat(u盘文件系统类型可查看属性) /dev/sdb1 /mnt/usb
```

- 挂载u盘时不能用远程工具，需用linux虚拟机，因为本机和虚拟机识别u盘存在竞争关系
- u盘文件类型：linux默认不支持NTFS文件系统。ntfs和exfat需安装支持。

**支持NTF文件系统**

linux系统自动识别加载驱动，常见驱动都包含在内核中 ，但默认不支持NTFS

**解决方法：**

1. 重新编译内核，手动加载驱动（比较麻烦，推荐2）

2. 插件ntfs-3g

   ```shell
   wget  https://tuxera.com/opensource/ntfs-3g_ntfsprogs-2017.3.23.tgz	#官方安装包下载 
   tar -zxvf ntfs-3g_ntfsprogs-2017.3.23.tgz		#解压缩
   cd ntfs-3g_ntfsprogs-2017.3.23			#编译安装
   ./configure
   make 
   make install
   ```

   如报错需要gcc支持，安装gcc即可`yum install gcc`

   ```shell
   mount -t ntfs-3g 分区设备文件名 挂载点
   ```

### fdisk分区

#### 分区过程

**添加新硬盘**

虚拟机断电，在设置中添加即可（此处添加硬盘类型为SCSI）

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012175844.png" alt="image-20201012175844062" style="zoom: 40%;" />

**查看分区情况**

`fdisk -l`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012180237.png" alt="image-20201012180236963" style="zoom: 50%;" />

**分区**

```
fdisk 待分区设备文件名
```

fdisk交互指令说明：

基础操作：n,d,p,l,w,q

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012181812.png" alt="image-20201012181224614" style="zoom:40%;" />

1. 配置新硬盘/dev/sdb

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012181813.png" alt="image-20201012181505910" style="zoom:50%;" />

2. 输入l显示已知文件系统类型

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012181814.png" alt="image-20201012181619024" style="zoom: 50%;" />

   输入p查看分区列表，目前为空

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012181815.png" alt="image-20201012181714589" style="zoom: 50%;" />

3. 新建分区n

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012181923.png" alt="image-20201012181923221" style="zoom:50%;" />

   选择主分区p

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012181958.png" alt="image-20201012181958406" style="zoom:67%;" />

   起始扇区默认，结束扇区 +2G

   输入p查看分区列表

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012182104.png" alt="image-20201012182104735" style="zoom: 50%;" />

4. 新建扩展分区,输入n-->e。分区序号最好按顺序，起始扇区默认从上个分区末尾进行，结束扇区默认，即把剩余空间全部分给扩展分区。

   ![image-20201012182404377](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012182404.png)

5. 扩展分区建好后就可以开始分逻辑分区了。

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012182730.png" alt="image-20201012182730781" style="zoom:50%;" />

6. w保存退出

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012182819.png" alt="image-20201012182819475" style="zoom:67%;" />

7. 生效需重启系统或者重新读取分区表信息(省去重启过程)

   `partprobe`

   ![image-20201012182936239](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012182936.png)

8. 格式化mkfs

   分区将“大柜子”分割成“小柜子”，格式化在“小柜子”中打入“隔断”

   `mkfs -t ext4 /dev/sdb1`格式化分区sdb1

   `mkfs -t ext4 /dev/sdb5`格式化分区sdb5

   ![image-20201012183052512](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012183052.png)

**挂载分区**

目前分区情况

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012183216.png" alt="image-20201012183216920" style="zoom:50%;" />

创建目录disk1和disk5分别用来挂载sdb1和sdb5。

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012184904.png" alt="image-20201012184904933" style="zoom:50%;" />

额，这里挂载逻辑分区报错是因为忘记格式化那个分区了，格式化后再次挂载即可。

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012185100.png" alt="image-20201012185100156" style="zoom: 50%;" />

 fdisk只能看到分区是否被正常分配，不能看到挂载。**mount或df可查看挂载情况**

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012185211.png" alt="image-20201012185211338" style="zoom:50%;" />

mount查看

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012185422.png" alt="image-20201012185422254" style="zoom:50%;" />

 df

![image-20201012185312518](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012185312.png)

  

问题：手动挂载重启分区消失需要重新挂载，永久需要写入文件/etc/fstab


#### 自动挂载与fstab文件修复

![image-20201012185528602](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012185528.png)

格式：

分区设备文件名/UUID(硬盘通用唯一识别码)    挂载点	文件系统名称	挂载参数/特殊权限	指定分区dump备份[0不1每天备份2不定期备份]		是否被fsck检测[0不检测其他num检测优先级]

##### UUID查看

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012185704.png" alt="image-20201012185704793" style="zoom:67%;" />

太长可配合grep使用

##### 自动备份       挂载点下lost+found

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012185831.png" alt="image-20201012185831022" style="zoom: 50%;" />

- 自动挂载修改/etc/fstab文件eg:

```shell
/dev/sdb1       /disk1  ext4    defaults        1 2
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012190032.png" alt="image-20201012190032370" style="zoom:67%;" />



- 文件写错或删除/disk 会使系统崩溃

```shell
mount -a	#依据配置文件/etc/fstab内容自动挂载分区，
					#可在修改文件后执行进行检验是否成功修改
```

#### 修复

情景：修改文件fstab后重启后报错，输入root密码

修复：vi修改fstab文件

如文件只读，不可保存修改则重新挂载根目录/,加入读写权限

```shell
mount -o remount,rw /
```

**局限性**：只能修复文件报错；若根分区错误，无法修改

