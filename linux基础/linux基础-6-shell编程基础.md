---
title: linux基础_6.shell编程基础
date: 2020-10-11 09:22:17
tags: linux
categories: linux基础
---

## shell概述

### 什么是shell

   - 命令解释器，向用户提供向内核发送请求的界面（双向翻译）

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011093928.png" alt="image-20201001183116659" style="zoom:50%;" />

<!--more-->

   - 编程语言，解释执行的脚本语言，可直接调用linux系统命令

### 分类

1. bourne shell(1970,unix)，主文件名sh

   包括sh, ksh, Bash, psh, zsh;

2. C shell，主要用于BSD版unix，语法与C类似
   包括csh, tcsh

   两种语法（B shell&C shell）不兼容。linux主流shell-Bash，与sh兼容。

### linux支持的shell

 `cat  /etc/shells`可查看该文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012192028.png" alt="image-20201012191714842" style="zoom: 67%;" />

**bash切换**输入shell名即可，退出exit

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012192218.png" alt="image-20201012192218608" style="zoom:50%;" />



- /etc/passwd 最后一个字段为用户登录后权限

   ​	root-/bin/bash, 

   ​	命令（伪用户）-/sbin/nologin, 

   ​	shutdown-/sbin/shutdown	表示只能执行该命令（halt同）

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012192538.png" alt="image-20201012192538519" style="zoom:50%;" />



   

## shell脚本执行方式

### echo输出语句

`!`在shell中有特殊作用，不能在`"`中输出，输出需换为`'`, 但在shell脚本中可以使用。

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012192808.png" alt="image-20201012192808428" style="zoom: 67%;" />

#### 一些实例

```shell
echo -e 输出内容			#-e参数支持转义字符

转义字符:
\\:输出\本身
\a:输出警告音	\b：退格键/向左删除	\c：取消输出行末换行符	\e：ESCAPE键	
\f：换页符	   \n：换行					\r：回车					   	
\t：水平制表符，tab	\v：垂直制表符
\0：八进制--	 \x:shi十六进制输出ASCII码
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012193234.png" alt="image-20201012193234062" style="zoom:67%;" />

使用`\`可实现多行输入命令

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012193336.png" alt="image-20201012193336557" style="zoom:67%;" />

"\x61\t\x62\t\x63\n\x64\t\x65\t\x66"是字母的16进制ASCII表示

```shell
echo -e "\e[1;colornum 内容 \e[0m"		固定表达：颜色输出

colornum
30m黑色，31m红色，32m绿色，33m黄色，
34m蓝色，35m洋红，36m青色，37m白色
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012193520.png" alt="image-20201012193520414" style="zoom:67%;" />

   

### 执行脚本

#### 编写脚本hello.sh

实际上linux中文件不需要后缀，这里添加后缀只是为了管理者方便辨认

使用`cat -A hello.sh`查看下脚本内容(-A指包含隐藏字符),这是一个简单的输出语句

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012193931.png" alt="image-20201012193931886" style="zoom:50%;" />

- `#!/bin/bash`标称以下语句时sh脚本,本身可省略。但如果在脚本1中嵌入其他脚本2，且脚本2没有声称#!/bin/Bash,则会出现报错

- $为linux中的回车符

#### 执行脚本

##### 方法1

赋予执行权限`chmod 755 hello.sh`

然后使用`./脚本路径`执行

![image-20201012194315488](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012194315.png)

##### 方法2

 通过bash调用执行，无需赋权755
 `bash hello.sh `	

- 若出现错误 "bash: ./hello.sh: /bin/Bash: bad interpreter: No such file or directory." 可能是文件格式错误，

     可用vim打开输入:set ff查看文件格式，如果为dos，可使用:set ff=unix修改，然后使用:wq保存退出

     或者使用`#dos2unix 文件名`转换(需要安装支持)




## bash的基本功能

### 历史命令与补全

#### history 

```shell
history [选项]	[历史命令保存文件]
				-c 清空历史命令
				-w 把缓存中的历史命令即时写入历史命令保存文件~/.bash_history，默认退出登录后才会写入
				
```

输入`history`可查询历史命令

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012195537.png" alt="image-20201012195537072" style="zoom:50%;" />

`history -c`#清空缓存的历史命令，慎用。不建议清空历史命令。原因：

1. 可回溯；

2. 黑客习惯于清空隐藏，有助于判断攻击情况；

3. 特殊情况下例如为mysql设置密码后记录会存入文件存在安全隐患



历史命令记录在/root/.bash_history下

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012195810.png" alt="image-20201012195810363" style="zoom:67%;" />

命令还停留在第997条，可知新的历史命令未写入文件，关机或重启后才会更新。可使用` history -w`强制写入。

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012200052.png" alt="image-20201012200052704" style="zoom:50%;" />



- 历史命令默认保存1000条，可在环境变量配置文件中修改/etc/profile，修改后生效需重新登录

  若超过1000条会删除第一条，保存1001条

  ![image-20201012200313914](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012200313.png)





#### 历史命令调用tips

- 上下箭头调用之前的命令
- !n    重复执行第n条（history查询命令前有序号）

- !!      重复执行上一条命令
- !字串  重复执行最后一条以该字符串开头的命令

- 命令与文件补全tab

  命令/文件/目录 	Tab补全，没反应说明有多个该字符串开头的文件/命令/目录，再次敲击可查看



### 别名alias与bash快捷键

#### 别名

除非确定，否则定义的别名不应与现有命令重合

```shell
alias 别名='原命令'
eg.alias vi='vim'
```

查看现有命令别名

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012205138.png" alt="image-20201012205137967" style="zoom:67%;" />



**命令执行优先级：**

绝对路径/相对路径执行>执行别名>执行bash内部命令>按照环境变量$PATH定义的目录查找顺序找到的第一个命令

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012205323.png" alt="image-20201012205323770" style="zoom:50%;" />

- 命令执行需用绝对路径，平时使用不用绝对路径是因为已被放入PATH中
- 永久生效-写入配置文件/root/.bashrc

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012205414.png" alt="image-20201012205414406" style="zoom:60%;" />



删除别名

```shell
unalias 别名
```



#### bash常用快捷键

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012205612.png" alt="image-20201012205612565" style="zoom:50%;" />



按ctrl+R后输入ca,搜索到之前使用过含ca的命令

```shell
(reverse-i-search)`ca': cat /etc/profile|grep HISTS
```



### 输入输出重定向

标准输入输出

| 设备   | 设备文件名  | 文件描述符 | 类型         |
| ------ | ----------- | ---------- | ------------ |
| 键盘   | /dev/stdin  | 0          | 标准输入     |
| 显示器 | /dev/stdout | 1          | 标准输出     |
| 显示器 | /dev/sdterr | 2          | 标准错误输出 |

#### 输出重定向

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011093929.png" alt="image-20201002213911045" style="zoom:67%;" />

##### 标准输出重定向

```shell
命令 > 文件		#以覆盖方式将命令输出到文件/指定设备
命令 >> 文件	#以追加方式，将命令输出到指定文件/设备
```

重定向符后的空格可省略，前不可省。

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012205923.png" alt="image-20201012205923435" style="zoom: 50%;" />

再次使用>重定向到文件时，原来的内容会被覆盖

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012210035.png" alt="image-20201012210035266" style="zoom: 67%;" />

使用>>可追加至文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012210137.png" alt="image-20201012210137914" style="zoom: 67%;" />



##### 标准**错误**输出重定向

```shell
错误命令 2> 文件		#以覆盖方式将命令的错误信息输出到文件/指定设备
错误命令 2>> 文件	#以追加方式，将命令的错误信息输出到指定文件/设备
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012210409.png" alt="image-20201012210409854" style="zoom:67%;" />



##### **同时保存**正确和错误输出结果

省去人为查看命令是否正确切换重定向命令

```
命令 > 文件 2>&1		#以覆盖方式将正确和错误输出保存到一个文件中
命令 >> 文件 2>&1		#追加方式.....
命令 &> 文件				#作用同上,覆盖
命令 &>> 文件				#作用同上，追加
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012210631.png" alt="image-20201012210631911" style="zoom:60%;" />

```shell
命令 >> 文件1 2>>文件2        #追加方式，正确输出->文件1，错误输出->文件2

ls >> right 2>>fault			  #分类输出结果信息
```



##### 重定向特殊应用 /dev/null(类似垃圾箱)

 多用于处理shell脚本中的无意义输出, 丢弃一切写入其中的数据（但报告写入操作成功），读取它则会立即得到一个EOF。[详解](https://blog.csdn.net/zqtsx/article/details/41894223)

```shell
ls &> /dev/null
```

- 错误输出2和>之间不能用空格



#### 输入重定向

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011093930.png" alt="image-20201002220921683" style="zoom:67%;" />



##### 统计命令wc，Ctrl+D退出

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012211055.png" alt="image-20201012211055858" style="zoom:67%;" />

结果：6行，6个词，21个字节(包括换行符)

```shell
wc << 字符ch
<输入内容
...
<字符ch
统计ch中间的内容
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012211728.png" alt="image-20201012211728869" style="zoom:60%;" />



##### 使用输入重定向统计文件

```shell
wc [选项] [文件名]
		-c   统计字节数
		-w		统计单词数
		-l		统计行数
```


<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012211359.png" alt="image-20201012211359902" style="zoom:50%;" />




### 多命令顺序执行与管道符

#### 多命令顺序执行

##### ;命令拼接		

命令1`;`命令2`;`命令3.......`;`命令n

n个命令顺序执行，之间没有逻辑关系

eg. ` ls;date;cd /user;pwd`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012212142.png" alt="image-20201012212142389" style="zoom:67%;" />



##### &&逻辑与 

命令1`&&`命令2

命令1正确执行，命令2才会执行

eg. `ls hello.sh && echo yes`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012212228.png" alt="image-20201012212228161" style="zoom:67%;" />



##### ||逻辑或

命令1`||`命令2

“短路执行”：命令1正确，则命令2不执行；命令1错误，命令2 执行

eg.` ls /hhh || echo no`

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012212314.png" alt="image-20201012212314784" style="zoom:67%;" />

eg2.`ls /hhh && echo yes|| echo no`				#命令成功输出yes,失败no

![image-20201012212421968](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012212422.png)



##### 计算命令执行时间

```shell
# date;命令;date
```

##### “升级版”拷贝命令dd:

```shell
dd if=源(输入)文件/设备 of=目标(输出)文件/设备 bs=字节数 count=个数
选项：
bs=字节数			指定单次输入/输出多少字节，将其看做一个数据块
count=个数		 指定输入/输出多少数据块
```

- **dd**可拷贝文件，包括特殊文件（分区，硬盘文件系统），可视为硬盘数据拷贝命令；**cp**仅可拷贝狭义的文件

- /dev/zero是一个特殊的文件，读取它时会提供无限的空字符(NULL, ASCII NUL, 0x00)。[详解](https://blog.csdn.net/zqtsx/article/details/41894223)

  典型用法1：用它提供的字符流来覆盖信息；

  常见用法2：产生一个特定大小的空白文件。

```shell
dd if=/dev/zero of=/dev/sdb bs=4M 来重新给整个U盘清零
date;dd if=/dev/zero of=/root/testfile bs=1k count=100000;date
#计算产生100000k空白文件所需的时间
```

![image-20201012212740222](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012212740.png)

#### 管道符

```shell
命令1 | 命令2			#将命令1的输出作为命令2的输入
```

注意：命令1必须有正确输出，命令2才能执行

```shell
# ll -a /etc/ |more			#翻页查看命令执行结果
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012212934.png" alt="image-20201012212934659" style="zoom: 50%;" />

将使用more查看ll -a查询的结果

```shell
$ netstat -an |grep "ESTA"
tcp        0     96 192.168.52.128:22       192.168.52.1:58323      ESTABLISHED
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012213111.png" alt="image-20201012213100918" style="zoom:67%;" />

- [netstat](https://www.cnblogs.com/peida/archive/2013/03/08/2949194.html)

- grep---类似过滤器

```shell
grep [选项]	“搜索内容”
			-i  忽略大小写
			-n	输出行号
			-v	反向查找即搜索不符合条件的内容
			--color=auto	搜索出的关键字颜色显示
```



### 通配符与其他特殊符号

#### 通配符（完全匹配）

```shell
?		匹配一个任意字符
*		匹配任意多个字符
[]	匹配[]内任意一个字符,eg:[abc]hhh，可匹配ahhh,bhhh,chhh
[-]	匹配[]内任意一个字符，-表范围[0-9]匹配数字0到9，[a-z][A-Z]分别一个匹配小写字母和大写字母
[^]	逻辑非，eg:[^0-9]匹配一个非数字字符
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012213424.png" alt="image-20201012213424424" style="zoom:50%;" />

- 主要区分“一个”？和“多个”*字符



#### 其他Bash中的特殊符号

```shell
'				#单引号，单引号内所有特殊字符(eg.$ `反引号`)都没有特殊含义
"				#双引号，除$,``,\外其余特殊符号没有特殊含义直接显示。
				# 			$-调用变量值，``反引号-引用命令，\-转义
``			#反引号，`系统命令`，在bash中先执行，作用与$(命令)一致，推荐后者，``容易看错
$()			#引用系统命令，区别于``的是，此处调用最后执行，``调用时执行
#				#表注释
\				#转义符，eg:\$,输出$符而不是变量引用

```

- `'`和`"`区别：`'`输出纯字串，不存在特殊字符特殊作用或命令调用

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012213911.png" alt="image-20201012213911455" style="zoom:67%;" />



- ``` `和`$()`的区别

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012214053.png" alt="image-20201012214053115" style="zoom:67%;" />

  虽然执行结果相同，但``先执行命令，将结果赋给abc变量；$()输出时执行命令调用



## bash的变量

### 用户自定义变量

#### 什么是变量

- 变量时计算机内存单元，其中存放的值可以改变。

* 每个变量有一个名字，可以用于引用。

- 变量可用于保存暂时信息。

#### 设置规则

   - 变量名可由**字母，数字，下划线**组成，但只能以字母或下划线开头。eg：2numer（X）

   - bash中 变量默认**字符串类型**，如需运算，需要指定为数值型

   - 变量=值，=左右不能有空格。变量值如果有空格，需用`'`或`"`包含为一个整体。

     eg：abc12="hello world"

   - 变量值可叠加，但需要"$变量名"或${变量名}包含被操作变量。

     eg：PATH="$PATH":/root  或 PATH＝${PATH}:/root相当于在PATG后追加:/root

   - 如将命令结果作为变量值赋予变量需用``` `， 或`$()`包含命令

     eg: aa=\`ls\`  或 aa=$(ls)

   - 环境变量名建议大写，便于区分

#### 变量分类

| 变量           | 作用                       |                                                              |
| -------------- | -------------------------- | ------------------------------------------------------------ |
| 用户自定义变量 | 自定义                     | 变量名可修改，变量作用不定                                   |
| 环境变量       | 保存和系统操作环境相关数据 | 变量名不能自定义，也不可修改，作用固定<br />值可修改，有些环境变量可由用户添加 |
| 位置参数变量   | 向脚本中传递参数或数据     | 变量名不能自定义，作用固定，值不可修改，不可自定义添加       |
| 预定义变量     | bash已经定义好的变量       | 变量名不能自定义，作用固定，值不可修改，不可自定义添加       |

- 位置参数变量是预定义变量的一种，因为类型较多，所以单独列出

#### 本地变量/用户自定义变量

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012214734.png" alt="image-20201012214734552" style="zoom:60%;" />

变量默认时字符串类型，叠加可用`"$变量"`或者`${变量}`

```shell
set | more				#set查看系统中所有变量，more分页显示
```
<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012215000.png" alt="image-20201012215000428" style="zoom:50%;" />

注意：set查看所有变量,包括PATH

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012215213.png" alt="image-20201012215213853" style="zoom:60%;" />

```shell
unset name			#变量删除unname
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012215254.png" alt="image-20201012215254550" style="zoom:67%;" />






### 环境变量

变量名称固定，作用固定，可修改值，部分可添加

#### 用户自定义变量与环境变量区别

作用范围

- 用户自定义变量：当前shell
- 环境变量：当前shell和这个shell的所有子shell。(若写入配置文件，则在所有shell中生效)

#### 设置环境变量

```shell
export 变量名=变量值			#申明变量
env											#查询变量
unset 变量名							#删除变量
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012215522.png" alt="image-20201012215522813" style="zoom:60%;" />

env中的内容

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012215632.png" alt="image-20201012215632888" style="zoom:50%;" />



子shell内：

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012215835.png" alt="image-20201012215835568" style="zoom: 67%;" />

父shell的环境变量在子shell内也起作用

使用pstree可查看进程之间的调用关系树

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012215947.png" alt="image-20201012215947052" style="zoom:50%;" />



#### 系统常见环境变量

##### PATH：系统查找命令的路径

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012220151.png" alt="image-20201012220151533" style="zoom:67%;" />

追加时需注意格式，使用：分隔

ls之类的命令执行不需要绝对路径，是因为在PATH中存有其绝对路径，作用于全局

**Q:可执行文件如何不用./直接执行？**

1. 将文件放入bin下 （不推荐）

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012220545.png" alt="image-20201012220545019" style="zoom:67%;" />

   给文件赋予执行权限后拷贝入bin下

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012220623.png" alt="image-20201012220623060" style="zoom:67%;" />

   文件放入bin下后可直接执行，执行时会在path中列出的绝对路径中查找命令/文件

2. 将当前目录追加在PATH后

   <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012220921.png" alt="image-20201012220921933" style="zoom: 67%;" />

值得注意的是，叠加写入PATH的路径，临时生效，永久需写入配置文件

##### PS1: 定义系统提示符的变量

```shell
\d		显示日期。“星期 月 日”
\t		24h制时间。“HH:MM:SS”
\T		12h制时间。“HH:MM:SS”
\A		24h制时间。“HH:MM”
\@		12h制时间。“HH:MM”
\h		简写主机名。默认“localhost”
\u		显示当前用户名
\w		显示当前目录绝对路径
\W		显示当前所在目录最后一个目录
\#		执行的第几个命令
\$		提示符。普通用户-$,root-#

# echo $PS1				#默认格式
[\u@\h \W]\$
```

修改

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012221415.png" alt="image-20201012221415192" style="zoom:60%;" />

### 位置参数变量

位置参数变量是预定义变量的一种，因为类型较多，所以单独列出

```shell
$n		n-数字，0代表命令本身,$1-9分别表示接收到的第一到九个参数,10以上需按${n}的格式,${10}
$*		代表所有命令，将其看作一个整体
$@		代表所有命令，将每个参数区分对待
$#		参数个数
```

- $*和$@

  假设可执行文件收到参数 11， 22， 33， 44， 55（均为字符串）

  则$*类似'1122334455'，$@类似{11,22,33,44,55}

eg1.

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012221740.png" alt="image-20201012221740590" style="zoom:67%;" />

$0命令本身，$1接收到的第一个命令，以此类推

eg2. 一个运算例子

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012222035.png" alt="image-20201012222000366" style="zoom:67%;" />

```shell
#!/bin/bash
sum=$(($1+$2))                  #数值运算格式$(())
echo $sum
```

eg3. for循环测试$*和$@

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012222408.png" alt="image-20201012222408867" style="zoom:50%;" />

for循环遍历$*,一个整体同时输出
for循环遍历$@，内容单独挨个输出

```shell
#!/bin/bash

echo "parameters numer:$#"
echo "the parameters is:$*"
echo -e "the parameters is:$@\n"			#echo输出特殊字符 -e

for i in "$*"
    do
        echo "the parameters is:$i"
    done

x=1
for j in "$@"
    do
        echo "the parameter$x is:$j"
        x=$(($x+1))
    done
```





### 预定义变量

#### 预定义变量

```shell
$?		最后一次执行命令返回的状态。正确-0，错误-对应错误的数字代码
$$		当前进程进程号PID
$!	后台运行的最后一个进程的进程号PID
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012231527.png" alt="image-20201012222936620" style="zoom: 50%;" />

命令 &表示将命令放在后台执行，由于top是专用于前台与用户交互 查看系统状态的命令，所以一放入后台就停止运行。想要恢复到前台运行可使用`fg 工作号`(工作号就是[]内的数字)，可通过`jobs`查看后台正在运行/中止的命令。

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012224044.png" alt="image-20201012224044036" style="zoom:67%;" />



```shell
#!/bin/bash

echo "the current process is $$"			#当前进程PID
find /root -name hello.sh &			#&表示将进程挂在后台执行
echo "$(jobs)"
echo "the last one Daemon process is $!"		#最后一个后台进程PID
```





##### 主动接收键盘输入read

echo只能被动等待，不能输出提示信息引导用户输入，不够友好

```shell
read [选项] [变量名]
			-p "提示信息"
			-t 秒数  等待用户输入秒数
			-n 			接受参数数量/字符数
      -s			隐藏输入，例如输入密码时可用
```
![image-20201012224603790](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012224603.png)
```shell
readtest.sh 
#!/bin/bash
read -t 30 -p "Please input your name:" name
echo "Name is $name"

read -s  -t 30 -p "Please input your passwd:" password
echo -e "\nPasswd is $password"

read -n 1 -t 30 -p "login?[y/n]:" choice			#-n 1 接受1个参数后立刻执行下一条
echo -e "\n"
```



## bash的运算符

### 数值运算与运算符

#### 声明变量类型 declare

```shell
declare [+-][选项] 变量名
				-：给变量设置属性
				+：给变量取消属性
				-i:将变量声明为整数型
				-x:将变量申明为环境变量
				-p:显示变量被声明的类型
```

变量默认类型为字符型，要想进行**数值运算**，需将变量声明为整型,使用-i参数

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012225128.png" alt="image-20201012225128291" style="zoom:67%;" />



环境变量+x

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012224930.png" alt="image-20201012224930505" style="zoom:67%;" />

```bash
export aa			#将aa声明为环境变量
declare -p aa		#查看aa类型，x--环境变量
declare +x aa			#取消aa的环境变量属性
```

其他数值运算方法

```shell
echo $(($aa+$bb)) 		#$((运算式))，推荐
echo $[$aa+$bb] 			#$[运算式]，不建议容易与$(命令)混
echo $(expr $aa + $bb)		#$(expr 运算式)，注意+左右有空格
```



#### 运算优先级

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011093931.png" alt="image-20201003231448357" style="zoom:67%;" />

优先级数字越大，优先级越高



### 变量测试与内容替换

#### 置换格式

![image-20201003231608574](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011093932.png)

主要用于通过x的值检测y值的状态（未设置，空，有值），多用于脚本中自动判断，类似if-else



一些小规律：（表比较难记，建议作为工具表，随用随查）

- ：与没有：

- +-  结果相反

  =   不仅改变x还改变y

- ?报错



## 环境变量配置文件

### 简介

环境变量配置文件-每次开机生效

#### source

更改环境变量后重新登陆生效，source可省略此过程

```shell
source 配置文件
或
. 配置文件		#.是source的缩写
```



#### 环境变量配置文件

定义对系统os生效的系统默认环境变量，如PATH，HISTSIZE，PS1，HOSTNAME等

```shell
# echo $PATH
/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/jen/.local/bin:/home/jen/bin
```

变量叠加修改：一次性,重启开机后失效，想要永久生效需写入配置文件

**常见配置文件**

`/etc/profile`

``/etc/profile.d/*.sh`

 `/etc/bashrc`

 `~/.bashrc`, 

 `~/.bash_profile`

- /etc...                 所有用户都生效
- ~/.bash...          家目录，当前用户生效，隐藏文件

### 作用

#### 优先级

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011093933.png" alt="image-20201002163004666" style="zoom:67%;" />

#### 访问路径1

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011093934.png" alt="image-20201004104239463" style="zoom:67%;" />

- /etc/profile作用：

  USER变量，LOGINNAME变量，MAIL变量，PATH变量，HOSTNAME变量，HISTSIZE变量

  PATH：

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012225926.png" alt="image-20201012225926614" style="zoom:50%;" />

  USER，LOGINNAME，MAIL

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012230040.png" alt="image-20201012230040443" style="zoom:50%;" />

  HOSTNAME, HISTSIZE .HISTCONTROL

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012230114.png" alt="image-20201012230114836" style="zoom:67%;" />

  umask

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012230201.png" alt="image-20201012230201241" style="zoom:67%;" />

  调用/etc/profile.d/*.sh文件

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012230257.png" alt="image-20201012230257888" style="zoom:50%;" />

  下面的程序段使得管理员才能执行/usr/sbin下的命令

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012230423.png" alt="image-20201012230423363" style="zoom:50%;" />

- /etc/profile.d/*.sh

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012231528.png" alt="image-20201012230636733" style="zoom:67%;" />

- lang.sh-与系统语言有关

  /etc/locale.conf调用+path追加

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012231529.png" alt="image-20201012230911559" style="zoom:50%;" />

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012231530.png" alt="image-20201012231000855" style="zoom: 50%;" />





#### 访问路径2

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011093935.png" alt="image-20201004110954353" style="zoom: 50%;" />

- ~/.bash_profile

  追加PATH.后Path会覆盖原值，但./bash_profile中使用追加

  ![image-20201012231413254](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012231413.png)
  
  
  
- ~/.bashrc

  别名声明,可写在其他文件内，注意作用范围

  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012231518.png" alt="image-20201012231518249" style="zoom:67%;" />
  
- /etc/bashrc

  PS1变量
  
  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012231724.png" alt="image-20201012231724059" style="zoom:50%;" />
  
  umask
  
  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012231945.png" alt="image-20201012231945496" style="zoom:60%;" />
  
  PATH变量
  
  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012231926.png" alt="image-20201012231926225" style="zoom:60%;" />
  
  调用/etc/profile.d/*.sh（仅在免登录shell中调用）
  
  <img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201012232009.png" alt="image-20201012232009695" style="zoom:67%;" />



   

   

### 其他配置文件与登录信息

#### 注销时生效的环境变量配置文件

  `~/.bash_logout`

#### 历史命令记录配置文件

~/bash_history

- 重要排错手段，一般不建议删除
- mysql设置密码时会记录在配置文件中

#### shell中登录信息

##### 本地终端欢迎信息：/etc.issue

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011093936.png" alt="image-20201004111344889" style="zoom: 50%;" />

```shell
#/etc/issue
\S
Kernel \r on an \m
```

修改后只对本地生效

- 终端号

  每个虚拟控制台登录都会产生一个`tty1-7`, 每一个远程连接都会产生一个`pts/0-255`.



##### 远程终端欢迎信息：/etc/issue.net

```shell
$ cat /etc/issue.net
\S
Kernel \r on an \m
```

- 转义符在此文件中不能使用
- 是否显示欢迎信息，由ssh配置文件**/etc/ssh/sshd_config**决定（加入Banner /etc/issue.net行才可显示，需重启ssh服务）。默认不生效

```shell
vim /etc/ssh/sshd_profile
...
# no default banner path
#Banner none
Banner /etc/issue.net
...


service ssh restart			#重启ssh服务

#退出后重新登录可见欢迎信息，由于issue.net中转义符不会生效，故原样输出
\S
Kernel \r on an \m
Last login: Sun Oct  4 19:20:24 2020 from 192.168.52.x
[root@localhost ~]# 
```

- 登陆后欢迎信息：/etc/motd

  本地/远程均显示

  ```shell
  # cat /etc/motd
  Do not operate unauthorized,thanks
  ```

  可自定义，不建议写welcome to ...，国外有个报道黑客入侵了一个服务器，而这个服务器却给出了欢迎登录的信息，因此法院不做任何裁决。

  ```shell
  #重新登陆可见
  \S
  Kernel \r on an \m
  Last login: Sun Oct  4 19:27:18 2020 from 192.168.52.1
  
  Do not operate unauthorized,thanks
  ```

远程登录欢迎信息应尽可能删减敏感信息



