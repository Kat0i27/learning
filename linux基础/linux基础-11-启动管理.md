---
title: linux基础_11.启动管理
date: 2020-10-10 17:39:23
tags: linux
categories: linux基础
---

## Centos6.3启动管理

### 运行级别
|0| 1    | 2    | 3    | 4    | 5    | 6    |
|----| ---- | ---- | ---- | ---- | ---- | ---- |
|  关机    |   单用户模式，类似win安全模式，用于修复系统   |  不完全的命令行模式，不含NFS    |  完全的命令行模式，标准字符界面    | 系统保留     |   图形界面   |重启动|

**运行**

<!--more-->

```shell
runlevel			#查看运行级别
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010213339.png" alt="image-20201010213339479" style="zoom: 60%;" />

`N 5`表示开机直接进入图形界面，如果是从5到3，则显示`5 3`

```shell
init 0			#关机，不保存正在运行的状态，不推荐
init 运行级别			#改变
```

**系统默认运行级别**

修改init配置文件`/etc/inittab`(centos7之后不再使用)

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010214007.png" alt="image-20201010214006985" style="zoom:50%;" />

centos7定义在/lib/systemd/system下

![](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010223127.png)

## 启动引导程序grep

[Centos7启动过程](https://developer.aliyun.com/article/516752)

![image-20201010214217860](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010214217.png)

加电自检----主引导修复----grub启动引导程序----加载内核（压缩）----内核解压缩，自检(dmessg)----initranfs读取建立仿真目录----加载驱动-挂载真正根目录-系统启动进程调用`/sbin/init`----进一步调用`/etc/init/rcS.conf`----调用`rc.sysinit`系统初始化（最基本功能）---- 确定运行级别----不同界面对应的附加程序

- linux驱动包含在内核中，不需要手工安装，除非已包含驱动中没有
  windows只安装操作系统，驱动需要另外安装

- IDE接口驱动，直接在内存中，可直接识别加载
  现有大多数计算机硬盘SATA/SCSI，linux内核认为不是必须，作为模块放在/lib下，内核需要从/lib下读取驱动才能识别硬盘。（类似钥匙锁在房间里开门）
  initranfs文件系统有一个模拟根目录，内核先加载文件系统将常见驱动加载到内核，建立仿真目录，加载硬盘分区，加载其他分区（类似找开锁公司配假钥匙开门），该文件实际在/boot/下

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010215732.png" alt="image-20201010215732335" style="zoom:50%;" />

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010220238.png" alt="image-20201010220238327" style="zoom:51%;" />
  
  ```shell
  cpio -ivcdu < ...		#解压缩
  ```

	<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010220513.png" alt="image-20201010220513473" style="zoom:50%;" />

  






- /sbin/init运行用户空间的第一个应用程序

  init:

  Centos 5: SysV init       配置文件：/etc/inittab

  Centos 6: Upstart        配置文件：/etc/inittab;/etc/init/*.conf(主要）

  Centos 7: systemd       配置文件：/etc/systemd/system;/usr/lib/systemd/system

  

- 系统初始化

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010221758.png" alt="image-20201010221758282" style="zoom:50%;" /><img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010221812.png" alt="image-20201010221812887" style="zoom:50%;" />

- rcx.d/			软链接

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010222129.png" alt="image-20201010222129704" style="zoom:45%;" />

- centos7运行级别

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010223127.png" alt="image-20201010223127022" style="zoom:67%;" />


## 系统修复模式-grub配置文件

### grep中分区的表示

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010222523.png" alt="image-20201010222523342" style="zoom:60%;" />


Centos6

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201010224309.png" alt="image-20201010224309067" style="zoom: 67%;" />

- default:默认选择的系统，0-第一个，1-下一个（如果有2个）
- timeout：等待选择时间
- 背景图保存位置，h(0,0)=/boot/
- 标题	\启动程序的保护分区/主目录		\	/(boot)内核加载时的选项(默认，一般不调整)	\指定内存文件系统镜像文件位置