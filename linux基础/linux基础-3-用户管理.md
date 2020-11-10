---
title: linux基础_3.用户管理与用户组管理
date: 2020-10-11 09:21:44
tags: linux
categories: linux基础
---


### 用户配置文件

用户配置文件：查看和修改用户信息

####  **passwd**(7个参数)

   `man 5 passwd `查看配置文件格式

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011221712.png" alt="image-20201011221712295" style="zoom:67%;" />

<!--more-->

   - UID（用户ID）

     <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011205156.png" alt="image-20201011205149896" style="zoom:50%;" />

   centos7普通用户从1000开始

   - GID（组ID）

     初始组：用户同名组，只能有一个，可修改

     附加组：可加入其他用户组，拥有其权限，多个

   - GECOS（用户说明）

   - Directory（家目录）

     /home/用户名/和/root/

     初始登录目录，目录权限普通用户700，root 500（ll 目录 -d）

   - shell（命令解释器）

     /bin/bash/

     /sbin/nologin/		伪用户

####  **shadow**(9个参数)

   用户名：加密密码：密码最后修改日期：修改间隔：有效期：密码到期警告时间（前）：过期宽限时间（后）：账号失效时间：保留

`cat /etc/shadow`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011222247.png" alt="image-20201011222247865" style="zoom: 50%;" />

   - 加密密码：sha512，!!或*表示无密码。可能被爆破但密码加盐撞库成功可能性不大

   - 日期均为时间戳（1970-01-01到当天的天数）

     ```sh
     date -d "1970-01-01 16066 days"		#时间戳-日期
     echo $(($(date--date="2014/01/06"+%s)/86400+1))		#日期-时间戳
     ```

#### /etc/**group**

   组名：组密码：GID：组中附加用户

`cat /etc/group`	

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011222437.png" alt="image-20201011222437758" style="zoom: 50%;" />



#### /etc/gshadow

   组名：组密码：组管理管名：组中附加用户

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011222606.png" alt="image-20201011222606938" style="zoom:50%;" />

- 密码为空可用!或不填
- 密码修改可用gpasswd group名，类似passwd
- 组切换可使用newgrp 组名，类似su

##### 例子

```
beinan:!::linuxsir
linuxsir:oUS/q7NH75RhQ::linuxsir
```

第一字段：这个例子中，有两个用户组beinan用linuxsir
第二字段：用户组的密码，beinan用户组无密码；linuxsir用户组有已经，已经加密；
第三字段：用户组管理者，两者都为空；
第四字段：beinan用户组所拥有的成员是linuxsir ，然后还要对照一下/etc/group和/etc/passwd 查看是否还有其它用户，一般默认添加的用户，有时同时也会创建用户组和用户名同名称； linuxsir 用户组有成员linuxisir ；



### 用户管理相关文件

#### 用户家目录

   初始登录位置

   普通用户：/home/用户，所属者和所属组均为此用户，权限700

   超级用户：/root/，----，权限550

   注意：普通用户变为超级用户只需在/etc/passwd将uid变为0,重新登录家目录不变，权限升级

#### 用户邮箱   
/var/spool/mail/用户名

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011223754.png" alt="image-20201011223754631" style="zoom:60%;" />



#### 用户模板文件 /etc/skel/

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011224150.png" alt="image-20201011224150918" style="zoom: 50%;" />

​      

### 用户管理命令

#### 添加用户useradd

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011224451.png" alt="image-20201011224451524" style="zoom:60%;" />

添加用户涉及的文件

手动创建: 指定uid（-u), 用户组(-g初始组gid,-G附加组），备注(-c)，家目录(-d)，shell(-s)

 <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011225017.png" alt="image-20201011225017066" style="zoom: 50%;" />

  缺省选项/默认

   /etc/default/useradd

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011225354.png" alt="image-20201011225354582" style="zoom: 60%;" />

   /etc/login.defs

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011225720.png" alt="image-20201011225720071" style="zoom: 60%;" />



#### 修改密码passwd

   普通用户修改自己密码：passwd

   管理员修改他人：passwd user

   管理员修改密码可无视密码复杂度要求，但普通用户必须遵循

##### 查看密码状态

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011225823.png" alt="image-20201011225823636" style="zoom:67%;" />

  用户名 密码设定时间 修改间隔 密码有效期 警告时间 密码不失效



##### 锁定用户&解锁

`passwd -l user2`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011230035.png" alt="image-20201011230035392" style="zoom:67%;" />

密码前加入!!使密码失效，无法登陆

`passwd -u user2`	解锁

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011230157.png" alt="image-20201011230156958" style="zoom:67%;" />

shell编程批量添加密码的一点启发

`echo "123"|passwd --stdin user1`		使用前者输出作为后者输入代替标准输入

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011230614.png" alt="image-20201011230614044" style="zoom:67%;" />



##### 锁定用户的一些方法小结

      1. passwd文件shell 改为/sbin/nologin
      2. shadow密码前加! 换算失效
      3. 注释用户



#### 修改用户信息usermod

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011230817.png" alt="image-20201011230817906" style="zoom: 50%;" />

   ```shell
usermod -c "tede" user1
usermod -G root user1
usermod -L user1
usermod -U user1 
   ```



#### 修改密码信息chage

 ` chage -l jen`		#查看密码状态

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011231207.png" alt="image-20201011231207328" style="zoom:60%;" />

`chage -d 0 user`	#要求用户一登录就修改密码

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011231449.png" alt="image-20201011231449077" style="zoom:50%;" />

#### 删除用户userdel

`userdel -r username`	-r彻底删除

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011231610.png" alt="image-20201011231610779" style="zoom: 60%;" />

   验证完全删除的方法：再次添加不报错

#### 查询id

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011231744.png" alt="image-20201011231744228" style="zoom:65%;" />

#### 切换用户su

   ```shell
su - root											#- 连带env切换
su - root -c "useradd user3"	#-c 不切换用户身份，执行一次命令
   ```

   

### 用户组管理命令

#### 添加用户组groupadd

`groupadd tg`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011231952.png" alt="image-20201011231952262" style="zoom:65%;" />

帮助文档

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011232100.png" alt="image-20201011232100246" style="zoom:50%;" />

#### groupmod

`groupmod -n lamp tg`		修改组名，一般不用

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011232223.png" alt="image-20201011232222988" style="zoom:67%;" />



#### groupdel

   ```shell
groupdel 组名
   ```

   组内有初始用户，不可删除，附加用户不影响

`useradd tt -g lamp`		`useradd tt1 -G lamp`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011232547.png" alt="image-20201011232547136" style="zoom:60%;" />

此时tt1的初始组是tt1,附加组是lamp。

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011232746.png" alt="image-20201011232746661" style="zoom: 67%;" />

如果像删除组lamp,会报错lamp是tt用户的初始组无法删除

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011232851.png" alt="image-20201011232851481" style="zoom: 67%;" />

使用`userdel -r tt`删除用户tt后，再次删除组lamp即可，此时组lamp不受tt1的限制

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011233116.png" alt="image-20201011233116879" style="zoom:67%;" />



#### 修改已存在用户附加组gpasswd

除了创建用户时指定用户的附加组，使用usermod指定用户附加组，可使用gpasswd将已有用户加入附加组

`gpasswd -a user1 lamp`		#参数-a   user1加入附加组lamp

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011233523.png" alt="image-20201011233523504" style="zoom:67%;" />

`gpasswd -d user1 lamp`			#将用户从附加组中移除

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011233716.png" alt="image-20201011233716097" style="zoom:67%;" />



   

   

