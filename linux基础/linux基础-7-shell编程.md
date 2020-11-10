---
title: linux基础_7.shell编程
date: 2020-10-11 09:23:01
tags: linux
categories: linux基础
---



## 基础正则表达式

### 正则表达式与通配符区别

| 正则                         | 通配符{*？-[]}                                 |
| ---------------------------- | ---------------------------------------------- |
| 在文件中匹配符合条件的字符串 | 匹配符合条件的文件名                           |
| 包含匹配                     | 完全匹配                                       |
| grep,awk,sed等命令支持正则   | ls，find,cp不支持正则，只能用shell的通配符匹配 |

**完全匹配**

<!--more-->

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013093007.png" alt="image-20201013093007746" style="zoom:67%;" />

**包含匹配**

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011094008.png" alt="image-20201004155335138" style="zoom:67%;" />



### 基础正则

包含匹配，规则越准确，匹配内容越少

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011094012.png" alt="image-20201004193504902" style="zoom: 67%;" />

***和.**

   ```shell
grep "a*" file			a重复0次或一次，其实无意义，无论有无均可匹配
grep "aa*"	file		匹配至少有一个a的行
grep "s..d"	file		匹配含s_ _d的行
grep "s.*d" file			匹s----...-d的所有内容
grep ".*" file			匹配任意字符
   ```

**^和$**

```
grep "^M" file			匹配以M开头的行
grep "n$" file			匹配以n结尾的行
grep "^$" file			匹配空白行\
grep -n "^$" file		-n显示行号
```
**[]**

```
grep -n "s[ao]id" file		匹配含said或soid的行
grep -n "[0-9]" file			匹配任意一个数字
grep -n "^[a-z]" file			匹配任意小写字母开头的行
```
**[^]**

```
grep -n "^[^a-zA-Z]" file			匹配非字母
```
**\\**

```
grep "\.$" file			匹配以.结尾的行
```
**\\{n\\}**

```
grep "a\{3\}"	file	匹配a连续出现3次的行
grep "[0-9]\{3\}"	file	匹配数字连续出现3次的行(超过也会包含)
```
**\\{n,\\}**

```
grep "^[0-9]\{3,\}[a-z]"	file	匹配数字开头连续出现超过3次的行
```
**\\{n,m\\}**

```
grep "sa\{1,3\}i" file		匹配s和i之间a出现至少1此至多3次的行
```

 

   

## 字符截取命令

### cut

cut提取列，grep提取行

```shell
cut [选项] file
		-f 列号			提取第几列
		-d 分隔符		按照指定分隔符分割列
```
读取文件某列(分隔符默认tab)

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013094938.png" alt="image-20201013094938332" style="zoom:67%;" />

指定分隔符读取

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013095042.png" alt="image-20201013095042047" style="zoom:50%;" />

以`:`为分隔符取第一三列即用户名和uid

**cut+grep**

下面是一个获取普通用户用户名的例子，普通用户shell为/bin/bash

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011094005.png" alt="image-20201004150004628" style="zoom:50%;" />



**局限**

分隔符：制表符tab，确切的符号，。：等可很好的匹配

如果是空格，可能有影响

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201011094011.png" alt="image-20201004181605979" style="zoom:67%;" />

awk可以解决这个问题，但使用较为复杂，建议优先cut,不能解决再寻求awk

### printf(严格上说不算截取命令)

#### 格式化打印

awk中最常见的打印输出字符串命令

```shell
printf '输出类型输出格式' 输出内容
				%ns		字符串，n指数量
				%ni		整数
				%m,nf	浮点数/小数，m和n是数字，m=整数位数+小数位数,n=小数位数。
							eg. 8.2f表示共输出8位数，其中2位是小数
				\a		警告音			\b	退格/向左删除
				\f		清除屏幕		\n	换行
				\r		回车				\t	水平制表符/tab
				\v		垂直制表符
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013095652.png" alt="image-20201013095652228" style="zoom:67%;" />

```shell
printf %s 1 2 3 4 5 6			
123456
```

对输出内容使用%s格式化输出,一次处理一个字符

```shell
printf %s %s %s 1 2 3 4 5 6			
%s%s123456
```

多于1个输出格式应使用''或""括起来，否则会识别第一个，并将后续格式当作输出内容处理

```shell
printf '%s %s %s' 1 2 3 4 5 6			
1 2 34 5 6		  									#输出 1 2 3为一组4 5 6为一组
printf '%s %s %s\n' 1 2 3 4 5 6
1 2 3
4 5 6
```

#对输出内容使用%s %s %s格式,一次处理三个字符



#### 命令结果的格式化输出

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013100131.png" alt="image-20201013100131097" style="zoom:67%;" />

printf不能打印文件内容,也不能使用管道符接收输出内容

```shell
printf '%s' stu.txt			#不会直接识别文件
cat stu.txt|printf '%s'		#不能使用管道符接收输出内容
```
需将查看文件命令作为变量传入`$()`,文件内容以字符串形式输出,不包含特殊字符

```shell
printf '%s' $(cat stu.txt)		#将命令结果作为变量$(命令)
IDNamegenderMark1LimingM862ScM903GaoM83
```
```shell
printf '%s\t%s\t%s\t%s\n' $(cat stu.txt)	#调整格式
ID      Name    gender  Mark
1       Liming  M       86
2       Sc      M       90
3       Gao     M       83
```

awk支持print和printf，print默认结尾换行（Linux中默认没有print）

### awk(复杂版列提取）

#### 格式

```shell
awk '条件1 {动作1} 条件2 {动作2} 条件3 {动作3} 条件4 {动作4}'


一般使用关系表达式作为条件,eg:
x>10		x>=10		x<=
```



**动作：**

1. 格式化输出

2. 流程控制语句

感觉像一个一句话版的if-else，（过滤）条件可省略，指所有

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013100801.png" alt="image-20201013100801711" style="zoom:67%;" />

```shell
awk '{printf $2 "\t" $4 "\n"}' stu.txt 
```

- awk支持`''`, 也支持`""`,注意避免同类型重复嵌套造成意外闭合
- 未设定过滤条件，表示对所有数据格式化输出
- 处理数据时读入一行-格式化-读入下一行。。。文件结尾

#### awk & cut

之所以需要awk是因为cut不能很好处理分隔符为空格的内容

```shell
df -h | awk '{print $1 "\t" $5 "\t" $6}'
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013100957.png" alt="image-20201013100957892" style="zoom:67%;" />

- 系统命令中只有printf,没有print。但在awk中都可用

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013101121.png" alt="image-20201013101121875" style="zoom:67%;" />

```shell
df -h |grep sda2|awk '{print $5}'|cut -d "%" -f 1
```

- 首先查询分区状况,找到含sda2的列,取第5 行,以%作为分隔符,取第一部分得到分区使用率

#### BEGIN标记

```shell
awk 'BEGIN{printf"This is a transcript \n"} {print $2 "\t" $6}' stu.txt
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013101502.png" alt="image-20201013101502351" style="zoom:67%;" />

BEGIN表示在读取数据之前先执行BEGIN后{动作}

#### 指定分隔符

```shell
awk '{FS=":"} {print $1 "\t\t\t" $3}' /etc/passwd 
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013101645.png" alt="image-20201013101645334" style="zoom:67%;" />
由于awk先读取数据后执行动作所以在指定分隔符之前数据已经读入，所以未被处理
```shell
awk 'BEGIN{FS=":"} {print $1 "\t\t\t" $3}'  /etc/passwd
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013101853.png" alt="image-20201013101853284" style="zoom:67%;" />

#### END标记

```shell
awk 'BEGIN{FS=":"} {print $1 "\t\t\t" $3} END{print "aaaaaaa"}' /etc/passwd
```

![image-20201013102037884](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013102037.png)

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013102102.png" alt="image-20201013102102768" style="zoom:60%;" />



#### 关系运算符

```shell
cat stu.txt|grep -v Name|awk '$4>85 {print $2}' 
```

如果第4列>85则输出第2列

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013102305.png" alt="image-20201013102305102" style="zoom:67%;" />

#### awk&grep

```shell
nmap -sT 192.168.72.88 |grep tcp |grep ssh|awk '{print $2}'
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013110201.png" alt="image-20201013110201813" style="zoom:67%;" />



### sed

轻量流编辑器，用于将数据选取，替换，删除，新增命令

#### 区别于vi

- vi不能修改命令结果里的内容，除非先将结果保存到文件



- sed可用管道符接受内容进行修改

#### 格式

```shell
sed [选项] '[动作]' file
选项：
		-n:将经sed处理的行输出到屏幕(默认输出所有)
		-e:允许对输入数据应用多条sed命令编辑
		-i:由sed的修改结果直接修改读取数据的文件而不是由屏幕输出
动作：
		a :追加，在当前行后添加一行或多行，添加多行时除最后行每行末尾需用"\"表示数据未完结
		c \:行替换，用c后字符替换原行，多行替换时行末加\表示未完结
		i \:插入当前行前插入，多行插入行末\
		d:	删除指定行
		p:  打印输出指定行
		s:	字串替换，"行范围s/oldstr/newstr/g"	类似vim替换格式
		
```

- 不建议使用-i直接对文件进行修改，sed主要用于处理文件命令输出，修改可用vi(m)



#### 输出实例:

##### **输出p**

```shell
sed '2p' stu.txt 			
```
<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013104559.png" alt="image-20201013103404965" style="zoom:50%;" />

输出第二行,其余行是文件本身输出.要想只输出sed处理的内容,需添加-n参数

```shell
sed -n '2p' stu.txt 				#-n只输出处理内容
```

##### **删除d**

```shell
sed '2,4d' stu.txt 			#删除第2到4行
sed '2,3d' stu.txt  			#不影响源文件，加-i直接作用于文件结果
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013103659.png" alt="image-20201013103659734" style="zoom:67%;" />

注意这里删除只作用于命令结果,不会影响源文件

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013103755.png" alt="image-20201013103755582" style="zoom:50%;" />

##### **行后追加a**

```shell
sed '2a hello' stu.txt 
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013103943.png" alt="image-20201013103943679" style="zoom:67%;" />

##### **行前插入i**

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013104137.png" alt="image-20201013104137089" style="zoom:67%;" />



##### 行替换c

```shell
sed '2c No person' stu.txt 
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013104446.png" alt="image-20201013104446117" style="zoom:67%;" />

同样不影响源文件

##### 行内字符替换s

```shell
sed '4s/83/100/g' stu.txt  		#第4行83改为100
sed -e 's/Liming//g;s/Sc//g' stu.txt     #将Liming和Sc替换为空    
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013104713.png" alt="image-20201013104712938" style="zoom:50%;" />



## 字符处理命令

### 排序sort

```shell
sort [选项] file
			-f		忽略大小写
			-n		数值型排序，默认字符串型
			-r		反向排序
			-t		指定分隔符，默认tab
			-k,n[,m]	按指定字段范围排序，从n到m,默认到行尾
```

一般使用`sort 文件名`或者管道符

```shell
sort /etc/passwd
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013104835.png" alt="image-20201013104835673" style="zoom: 50%;" />

指定分隔符和排序字段

```shell
sort -t ":" -k 3,3 /etc/passwd
```

以:作分隔符,按照第三列排序

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013105053.png" alt="image-20201013105053702" style="zoom:50%;" />

由于默认按照字符型排序所以比较字符串首位ASCII大小,相同则比较第二位,以此类推.1001在2之前

```shell
sort -t ":" -k 3,3 /etc/passwd -n
```

### 统计wc

```shell
wc [选项] file
		-l:只统计行数
		-w:只统计单词数
		-m:只统计字符数
```

```shell
wc /etc/passwd
wc -l /etc/passwd
wc -w /etc/passwd
wc -m /etc/passwd
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013105423.png" alt="image-20201013105423397" style="zoom:67%;" />

可使用管道符统计命令输出



## 条件判断

### 常用判断语句格式

```shell
[ 判断语句 ]&&echo yes||echo no
或
test 判断语句 &&echo yes||echo no
```

`test 判断语句`不常用于脚本，不过看个人使用习惯

一般在脚本中使用格式2`[ xxx -e file ]`， 注意[ ]两侧的空格



```shell
[ -d /root ]&& echo yes ||echo no
yes
```

执行过程：扫描-分区-判断存在



#### 文件类型判断

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013111410.png" alt="image-20201013111410513" style="zoom: 50%;" />

eg:

```shell
test -e /root/initial-setup-ks.cfg 
[ -e /root/initial-setup-ks.cfg ]
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013111622.png" alt="image-20201013111622229" style="zoom:67%;" />

由于测试没有回显,所以使用`$?`查看上条命令执行结果,0代表正确执行,其他数字代表对应的错误代码.



#### 判断文件权限

只能测出大概范围，例如只有ugo中有一人有w权限则判断为真

##### 两个文件之间比较

```shell
file1 -nt file2		判断文件1修改时间是否比文件2新，新则1/真
file1 -ot file2		判断----旧
file1 -ef file2		通过比较inode判断是否为同一文件
```

- 硬链接inode一致，软连接不一致。

  ![image-20201013113327752](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013113327.png)

  一般情况下，文件名和 inode 号是一一对应，但是也有可能多个文件名指向同一个 inode 号，即硬链接。硬链接可以实现用不同的文件名访问同一个文件；对文件内容修改，会影响到所有的文件名；但是，删除一个文件名，不影响其他文件名的访问。
  
  ![image-20201013113239611](https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013113239.png)
  
  
  
  ```shell
  [ hello.sh -ef sh_hardlink.sh ]&&echo yes||echo no     
  ```

##### 整数大小比较

```shell
整数1 -eq 整数2			判断数1=数2?,相等则真
整数1 -ne 整数2			判断数1=数2?,不相等则真

整数1 -gt 整数2			判断数1>数2?,>则真
整数1 -lt 整数2			判断数1<数2?,<则真

整数1 -ge 整数2			判断数1>=数2?,>=则真
整数1 -le 整数2			判断数1<=数2?,<=则真
```

##### 字串比较

```shell
-z str			判断字符串是否为空，空则真
-n str			判断字符串是否非空，非空则真

str1==str2		相等则真
str1!=str2		不等则真
```

判断是否为空十分常用--脚本中检测用户输入

##### 多重条件判断

```shell
判断1 -a 判断2		逻辑与，都成立则真
判断1 -o 判断2		逻辑或，有1个真则真
！判断						 逻辑非，判断结果取反
```



## 流程控制

### if

#### 单分支格式 if-then

```shell
if [ 条件判断式 ];then
	程序
fi

或
if [ 条件判断式 ]
then
	程序
fi
```

这里的[  ]就是test判断格式2

```shell
#!/bin/bash
#统计根分区使用率iftest1.sh

rate=$(df -h | grep "/dev/sda2"|awk ' {print $5}' | cut -d "%" -f 1)

if [ $rate -ge 80 ]
        then
                echo 'Warning!/dev/sda2 is full!!'
fi
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013114143.png" alt="image-20201013114143168" style="zoom: 67%;" />

#### 双分支 if-then-else

**格式**

```shell
if [ 条件判断式 ]
  then
    程序
  else
    程序
fi
```

**实例**

```shell
#!/bin/bash
#备份mysql数据库

ntpdate asia.pool.ntp.org &>/dev/null
#同步系统时间
date=$(date +%y%m%d)    #提取年月日
size=$(du -sh /var/lib/mysql)           #统计数据库大小并记录
if [ -d /tmp/dbbak ]
        then 
                echo "Date:$date!">/tmp/dbbak/dbinfo.txt
                echo "Data size: $size" >> /tmp/dbbak/dbinfo.txt
                cd /tmp/dbbak
                tar -zcf mysql-lib-$date.tar.gz /var/lib/mysql dbinfo &>/dev/null			
                #文件不会覆盖,日期做后缀
                rm -rf /tmp/dbbak/dbinfo.txt
        else
                mkdir /tmp/dbbak
                echo "Date:$date!">/tmp/dbbak/dbinfo.txt
                echo "Data size: $size" >> /tmp/dbbak/dbinfo.txt
                cd /tmp/dbbak
                tar -zcf mysql-lib-$date.tar.gz /var/lib/mysql dbinfo &>/dev/null
                rm -rf /tmp/dbbak/dbinfo.txt
fi
```

```shell
#!/bin/bash
#判断apache是否启动
port=$(nmap -sT 192.168.1.156|grep tcp|grep http|awk ' {print $2}')
#使用nmap扫描服务器，截取apache服务状态，赋予port
if [ $port=="open" ]
	then
			echo "$(date) httpd is OK.">>/tmp/autostart-acc.log
	else
			/etc/rc.d/init.d/httpd restart &> /dev/null
			echo "$(date) restart httpd." >> /tmp/autostart-err.log
fi
```

- 有时用ps判断不准确，可能apache启动但不显示服务，不能确定是否可以正常连接
- netstat同上
- nmap可连接apache证明打开[nmap使用指南](https://crayon-xin.github.io/2018/08/12/nmap%E8%B6%85%E8%AF%A6%E7%BB%86%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97/)





#### 多分支 if-then-elif-then...-else

**格式**

```shell
if [ 条件判断式1 ]
  then		#1成立，执行，不成立执行elif判断2
    程序
elif [ 条件判断式2 ]
	then		#2成立执行，不成立-判断3
		程序
elif [ 条件判断式3 ]
	then
		程序
    ...
  else			#所有条件均不成立，执行此程序
    程序
fi
```

```shell
#!/bin/bash
read -p "Please input a filename: " file
#$file=输入的文件名
if [ -z "$file" ]		#是否空
	then
		echo "Error,Please input a filename: "
		exit 1
elif [ ! -e "$file"]#是否存在
	then 
		echo "Your input is not a file"
		exit 2
elif [ -f "$file" ]
	then
		echo "$file is a regulare file!"
elif [ -d "$file" ]
	then
		echo "$file is a regulare directory!"
else
		echo "$file is an other file!"
fi
```



### case多分支条件判断语句

与if...elif..else区别:if能判断多种条件关系，case语句只能判断一种条件关系

**格式**

```shell
case $变量名 in
	"值1")
			变量==值1则执行程序1
			;;
	"值2")
			如果变量值==值2，执行程序2
			;;
		...
			;;
		*)
			如果变量值都不是以上值，执行此程序
			;;
esac

```

```shell
#!/bin/bash
#判断用户输入
read -p "please choose yes/no:" -t 30 cho
case $cho in
	"yes")
			echo "your choice is yes!"
			;;
	"no")
			echo "your choice is no!"
			;;
	*)
			echo "your choose is error!"
esac


----------------
[root@localhost sh]# bash casetest1.sh
please choose yes/no:yes
your choice is yes!
[root@localhost sh]# bash casetest1.sh 
please choose yes/no:aa
your choose is error!
```



### for循环

#### 不确定循环次数

**格式**

```shell
for 变量 in 值1 值2 值3...
	do
		程序
	done
```

**实例:**

```shell
#!/bin/bash
#打印时间
for time in morning noon afternoon evening
	do
			echo "this time is $time!"
	done
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013114833.png" alt="image-20201013114833901" style="zoom: 67%;" />

不确定循环次数的for循环应用，灵活

```shell
#!/bin/bash
#批量解压缩脚本
cd /lamp
ls *.tar.gz > ls.log
for i in $(cat ls.log)
	do
		tar -zxf $i &>/dev/null
	done
rm -rf /lamp/ls.log
```

#### 指定循环次数

**格式**

```shell
for((初始值;循环控制条件;变量变化))
	do
		程序
	done
```

**实例**

```shell
#!/bin/bash
#从1加到100
s=0
for((i=1;i<100;i=i+1))
	do
		s = $(($s+$i))
	done
echo "the sum of 1+2+3...+100 is : $s"
```

```shell
#!/bin/bash
#批量添加用户
read -p "please input username: " -t 30 name
read -p "please input count: " -t 20 counts
read -p "please input password: " -t 20 pass

if [ ! -z "$name" -a ! -z "$counts" -a ! -z "$pass" ]                      #-z判断是否为空，-a与，3个全不空则为真
        then
                y=$(echo $counts | sed 's/[0-9]//g')                       #判断num是否是数字，将数字替换为空
                if [ -z "$y" ]          #空则证明是数字
                        then
                                for(( i=1;i<=$counts;i=i+1 ))
                                        do
                                                useradd "$name$i" &>/dev/null
                                                echo $pass | passwd --stdin "$nmae$i" &>/dev/null
                                        done
                fi
fi
```

<img src="https://cdn.jsdelivr.net/gh/mij0lb/PictureBed/BlogImg20201013115418.png" alt="image-20201013115418045" style="zoom: 67%;" />



### while循环与until循环

#### while不定/条件循环

循环会一直继续至条件不成立

**格式**

```shell
while [ 条件判断式 ]
	do
		程序
	done
```

**实例**

```shell
#!/bin/bash
#1加到100

i=1
s=0
while [ $i -le 100 ]		#小于等于100
	do
		s=$(($s+$i))
		i=$(($i+1))
	done
echo "the num is :$s"
```



#### until循环

与while相反，表达式不成立执行循环至表达式成立，终止

```shell
#!/bin/bash
#1加到100

i=1
s=0
until [ $i -gt 100 ]		#知道大于100结束
	do
		s=$(($s+$i))
		i=$(($i+1))
	done
echo "the num is :$s"
```



```shell
line=$(wc -l t2.sh|cut -f 1 -d " ") #行数
cow= $(cat t2.sh |awk "END{print NF}")#列数
for((j=0;j<cow;j++))
	do
			for((i=0;i<line;i++))
				do
					echo "$(cut -d " " -f $j t2.sh | sed -n '$i'p)"
					echo " "
				done
				echo -e "\n"
	done
```

