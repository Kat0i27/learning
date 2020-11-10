---
title: linux基础_2.vim
date: 2020-10-11 09:21:24
tags: linux
categories: linux基础
---

### vim

#### 位置

```
:set nu/nonu
gg/G	#到首行/末行
nG/:n   #到第n行
0/$		#移至行首/尾
```

<!--more-->

#### 插入

| a              | A    | i          | I    | o          | O          |
| -------------- | ---- | ---------- | ---- | ---------- | ---------- |
| 光标所在字符后 | 行尾 | ----字符前 | 行首 | 下插入新行 | 上插入新行 |

#### 删除/拷贝/剪切

```
删除：
dG	删除光标所在行到文末内容
D	删除----------行尾内容
:2,5d	删除第2到5行
x	删除光标所在处字符
nx	删除光标所在后n个字符

复制：
yy	复制当前行
nyy	复制当前行以下n行
dd+p剪切
dd ndd
p,P	粘贴在当前光标所在行下或行上
替换:R	从光标所在处开始替换，按esc结束
复原:u
```

#### 搜索

```
:/abc	文件中搜索abc	
n		出现的下一个位置
:%s/old/new/g	全文替换指定字符串
:n1,n2s/old/new/g	在一定范围内替换
```

#### 注释

```
:n1,n2s/^/#/g		#区块注释
:n1,n2s/#/ /g		#取消注释
:n1,n2s/^/\/\//g
```

#### 替换ab

```
ab mymail samlee@lampbrother.nat
```

#### 导入命令执行

```
r 文件路径	#导入文件
r !命令	 #导入命令执行结果
```

#### 定义快捷键

```
:map 快捷键 命令
:map ^P(ctrl+^+v) I#<ESC>	#注释快捷键
:map ^B x	删除行末
```

#### 默认配置文件

```
.vimrc->/home/user/.vimrc
	  ->/root/.vimrc
```

eg.
```
set nu
map ^p I#<ESC>
ab mymail  xxxx@xxx.com
```

#### 编码转换

```
iconv -f 原本编码 -t 新编码 filename [-o newfile]
-o保留原本的编码副本

iconv -f utf8 -t big5 vi.utf8 -o 
```



