---
title: linux基础_4.权限管理
date: 2020-10-11 09:22:17
tags: linux
categories: linux基础
---

### ACL权限

Access Control List (访问控制列表）它在UGO权限管理的基础上为文件系统提供额外的、更灵活的权限管理机制。ACL允许你给任何的用户或用户组设置任何文件/目录的访问权限。

#### 查看分区ACL权限是否开启

1. 查看分区

   `df -h`

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012085002.png" alt="image-20201012085002549" style="zoom:50%;" />

   <!--more-->

2. 查看ACL权限

   ` dumpe2fs -h /dev/sda2`  查看分区情况

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012085102.png" alt="image-20201012085102883" style="zoom: 67%;" />

##### 临时开启分区ACL权限

```shell
mount -o remount,acl /#重新挂载根分区，并加入ACL权限
```

##### 永久生效

```shell
1.修改/etc/fstab文件，加,acl
UUID=910dedc7-2b9e-4e2b-a82e-db2dda090854 /      xfs     defaults,acl       0 0
2.重新挂载mount -o remount /或重启系统
```



#### 设定与查看ACL权限

   ```shell
setfacl 选项 文件名
				-m	设定ACL权限
				-x	删除指定的ACL权限
				-b  删除所有的ACL权限
				-d  设定默认的ACL权限
				-k	删除默认--
				-R  递归设定ACL权限
   ```

   

   假设：

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011093904.png" alt="image-20200925220231761" style="zoom: 50%;" />

   设置下条件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012090401.png" alt="image-20201012090401137" style="zoom: 50%;" />

##### 为用户设定ACL权限		

```
setfacl -m  u:用户名:权限 文件名
```

`setfacl -m u:st:rx project/	`

##### 为组分配ACL权限

```
setfacl -m  g:组名:权限 文件名
```

`setfacl -m g:tgroup2:rwx project/	`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012090729.png" alt="image-20201012090729017" style="zoom:50%;" />

-  最大权限mask

   修改mask权限，不影响所有者权限（user），影响ACL权限(st)和其所属组权限(tgroup,tgroup2)

##### 调整最大用户权限mask 

```
setfacl -m m:权限 目录/文件
```

`setfacl -m m:rx project/`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012091051.png" alt="image-20201012091051325" style="zoom:50%;" />



##### 删除ACL权限

```
setfacl -x u:用户名 文件
        -x g:组名 文件
        -b	文件	删除文件下所有ACL权限
```

` setfacl -x g:tgroup2 project`		删除组tgroup2的ACL权限

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012091550.png" alt="image-20201012091549977" style="zoom:50%;" />

` setfacl -b project/`				删除project下所有ACL权限

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012091733.png" alt="image-20201012091733107" style="zoom:50%;" />

文件夹有ACL权限时，会有一个+

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012091834.png" alt="image-20201012091834906" style="zoom:50%;" />  

##### 递归设定ACL权限

   父目录设定ACL，子目录和子文件也会拥有相同ACL权限

```
setfacl -m u:用户名:权限 -R 文件名/目录
```

`setfacl -m u:st:rx -R project/ `

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012092303.png" alt="image-20201012092302987" style="zoom: 50%;" />

假设在project目录递归创建ACL权限后，该目录下所有子目录文件均受影响但是对于新创建的文件不受影响。

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012093412.png" alt="image-20201012093412373" style="zoom:50%;" />

   ##### 设定默认ACL权限

新建文件/目录遵守父目录ACL权限设定

```
setfacl -m d:u:用户名：权限 文件名		#d:default	新文件遵守父目录权限
```

` setfacl -m d:u:st:rx -R project/`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012093926.png" alt="image-20201012093926601" style="zoom:50%;" />

文件默认没有执行权限，对于目录

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012094533.png" alt="image-20201012094533781" style="zoom: 50%;" />

查看project目录acl权限

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012094157.png" alt="image-20201012094157294" style="zoom: 50%;" />   

   

### 文件特殊权限

查看默认文件权限时显示数字有四位，如下

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012094950.png" alt="image-20201012094950002" style="zoom:67%;" />

后三位与ugo权限有关，反转之后是755(--- -w- -w-到rwx r-x r-x)。首位就是特殊权限代表的数字和(SUID４，SGID2，SBIT 1)

#### SetUID: u+s

执行者执行时暂时获得文件属主身份（类似sudo root可执行命令）

条件：

- 可执行的二进制程序，可设定SUID权限

- 执行者需对程序有x权限

- SUID权限只在执行程序过程中有效

eg. passwd拥有SetUID权限(标志s)，普通用户在执行passwd命令时暂时拥有root权限，将密码写入shadow中

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012095632.png" alt="image-20201012095632654" style="zoom:50%;" />

  cat没有setUID权限，查看shadow文件警告权限不足

##### 设定SUID权限

  ```shell
chmod 4755 文件名	#设定SUID权限
chmod 755 文件名	#取消SUID权限
或
chmod u+s 文件名
chmod u-s 文件名
  ```
![image-20201012102142956](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012102143.png)

##### 注意

1. 关键目录严格控制写权限，eg./,/usr，/bin
2. 白字红底-错误文件，危险文件，权限过高的文件
3. 错误示范：给vim添加SUID权限，使得普通用户可修改任意文件
4. 对系统中默认应具有SUID权限的文件作一列表，定时检查是否有之外的文件被赋予SUID权限



#### SetGID：g+s

执行者执行时组身份暂时升级为文件属组身份，针对对象有二进制文件和目录两类

```
chmod 2755 文件名
chmod 755 文件名
chmod g+s 文件名
chmod g-s 文件名
```

##### 针对二进制文件

可执行的二进制程序，可设定SGID权限

条件：

- 执行者需对程序有x权限
- SGID权限只在执行程序过程中有效

eg. locate命令。普通用户对locate有执行权限，locate具有SGID权限，普通用户执行locate时，所属组变为slocate,对数据库有r权限，而普通用户对数据库权限为0，命令结束后所属组重新变为原来组

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012102632.png" alt="image-20201012102632928" style="zoom:67%;" />



##### 针对目录

在此目录有效组会变为目录所属组

条件：

- 普通用户对SGID目录有rx权限，才能进入
- 普通用户对目录有写权限时，新建文件默认属组为该目录属组

实例：

1. 创建目录test添加SGID权限，给目录添加写权限。
2. 切换至普通用户jen,jen对目录有rxw权限，可进入，且新建的文件默认属组为test的所属组root

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012103442.png" alt="image-20201012103442141" style="zoom:67%;" />

3. 若普通用户对目录不具备rx权限则无法进入目录

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012103934.png" alt="image-20201012103934801" style="zoom: 67%;" />



#### Sticky BIT文件黏着位：o+t（针对目录）

粘着位，限制普通用户（对root无效）。若普通用户对目录有w权限，只能删除自己建立的文件，不能删除其他用户的文件。

条件：

- 只针对目录有效
- 普通用户对该目录有wx权限，可写入
- 粘着位，限制普通用户，对root无效。普通用户有w权限，只能删除自己建立的文件，不能删除其他用户文件

```shell
chmod 1755 目录名
chmod 755  目录名
chmod o+t  目录名
chmod o-t  目录名
```

常见有粘着位的目录-/tmp

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012105847.png" alt="image-20201012104310298" style="zoom: 67%;" />

测试一下：

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012104900.png" alt="image-20201012104900395" style="zoom:50%;" />



#### 注意

特殊权限位 _ugo（第一位）一般不为7，针对对象不同，SUID-二进制文件，SGID-文件/目录，SBIT-针对目录



### 文件系统属性权限chattr

#### 设置文件系统属性chattr（文件锁）

```shell
chattr [+-=][选项] 文件或目录名
+：增加权限
-：删除权限
=：赋予权限
选项：
	+i	针对文件：不允许修改文件(删除，改名，修改数据)，对root有效
		  针对目录：允许 修改目录下文件数据，不允许建立和删除文件
	+a	文件：只能在文件中追加数据(不能使用vi等编辑器，只能使用echo追加)，
					 不能删除修改数据，相当于锁现有数据，可写入
			目录：允许在目录中建立修改文件，不允许删除

```

##### +i 针对文件：

位文件myfile添加文件锁	`chattr +i myfile`。不允许再修改文件(删除，改名，修改数据)，对root有效

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012105636.png" alt="image-20201012105636076" style="zoom:60%;" />,

查看权限变化，ll无效，需使用`lsattr -a 文件名`   

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012105840.png" alt="image-20201012105840916" style="zoom: 60%;" />

尝试再写入，失败。也无法删除，移动/重命名也不可以。

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012110104.png" alt="image-20201012110104175" style="zoom: 50%;" />

##### +i针对目录

对目录project赋予-i权限

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012110456.png" alt="image-20201012110456358" style="zoom:50%;" />

可看到实际上子文件/目录并未获得-i权限，所以可以修改文件内数据，但是无法删除/重命名/移动

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012110901.png" alt="image-20201012110901004" style="zoom:50%;" />

也不可创建文件/目录

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012112018.png" alt="image-20201012112018159" style="zoom:50%;" />

##### +a针对文件

对文件ccc写入内容后，加a权限

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012111308.png" alt="image-20201012111308373" style="zoom: 50%;" />

不可覆盖写入，即不能修改原数据，但可以追加

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012111525.png" alt="image-20201012111525747" style="zoom: 50%;" />

不能使用vim编辑修改，即便是追加

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012111741.png" alt="image-20201012111741503" style="zoom: 50%;" />



#### 查看文件系统属性lsattr

```shell
ls 选项 文件名
    -a 显示所有文件
    -d 所目标是目录，仅列出目录属性而非子文件
```

### sudo

1. sudo操作对象是系统命令,其他-普通文件
2. root将命令权限赋予普通用户，

```shell
visudo			#修改/etc/sudoers文件
```
<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012112459.png" alt="image-20201012112459000" style="zoom: 50%;" />

修改格式：

参照

```shell
root    ALL=(ALL)       ALL
%wheel  ALL=(ALL)       ALL
用户名  被管理主机地址/网段=（转换后可使用身份,默认root）	授权命令(绝对路径)
```

- 此处被管理ip指允许某用户在登录到该ip的主机上使用任意命令，而非允许源ip是该ip的主机登陆任意主机执行任意命令。定义的是目的ip而非来源ip。

实例：

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012114115.png" alt="image-20201012112944810" style="zoom:50%;" />

```
eg.
st ALL=/sbin/shutdown -r now	#授权st用户重启服务器
st ALL=/usr/bin/vim #vim 权限，实际上慎重赋予普通用户vim权限，转换身份后为root
```
<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012114116.png" alt="image-20201012113045012" style="zoom:50%;" />

此时st用户关机不再需要`sudo shutdown -r now`	而是直接使用命令`shutdown -r now`

`sudo -l`命令可查看用户被赋予sudo权限的命令,需要输入用户密码

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012114117.png" alt="image-20201012113445584" style="zoom:50%;" />



