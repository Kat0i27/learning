# python基础教程3

## 第一章 基础知识

math.floor(32.9)	取整

复数 cmath

绘图-海龟绘图turtle[官方文档](https://docs.python.org/zh-cn/3/library/turtle.html?highlight=tur#module-turtle)， 结束后done(),否则绘图窗口未响应

拼接字符串 +

python表达式与字符串转换repr()&str()

多行字符串''' '''

忽略特殊字符，除‘’

字符串unicode编码，码点

bytes和bytearray，编码/解码将文件存储到磁盘

## 第二章 列表和元组

数据结构：序列，索引/偏移量	0	-1

列表可修改，元组不可以

操作：索引，切片，相加，相乘，成员检查

索引相加

空列表

成员资格：序列，字符串	in

最大值，最小值，长度函数

list替换可以长度不同

插入新元素，与删除替换

列表方法：append(),clear(),=和.copy(),extend()

extend()修改的序列是调用序列，常规+拼接产生新序列

index(),insert(),pop(),

**pop()唯一修改列表但返回非None的方法**，作用于append相反

remove()删除第一个值为指定值的元素

reserse()反序，但直接作用于调用序列，要想得到反序后的值可调用reversed(a)，返回一个迭代器，可使用list将其变为列表（强制迭代完成）

sort()返回None直接修改调用序列，sorted可作用与任一序列，总返回一个列表

sort可选参数，key,reverse



元组，序列，不可修改

一个值的元组（value,)

元组可作为映射中的键，列表不行



## 字符串

字符串不可变，不可赋值

三种格式化方式，format多用与简写{存放变量}，format指定变量或格式，要包含{}，可用双重

格式化：字段名{}，转换标志r/a/s，格式说明符`:f，b...`

未命名参数和命名参数

字段中可使用索引和点句表示法

基本转换,格式说明符，宽度精度千位分隔符，对齐方式

补零，左对齐，右对齐，居中^

{}和{{}}	`'{{:{}}}{{:>{}}}'.format(item_width,price_width)`

center

find,指定起点终点（一般包含起点，不包含终点，python惯常做法)

join,需要都是字符串

lower()

split()

strip()去首尾空白，指定删除

replace()

translate(参1，参2，参3-可选)单字符替换，参2替换参1，删除参3

字符串满足条件？

isalnum,isalpha,isdecimal,isdigit数字,islower,isnumberic,isprintable,isspace空白,istitle,isupper大写,isdentifier





## 字典

键唯一，值不唯一

dict从其他类型映射为字典

字典操作：len(d),d[k],d[k]=v,del d[k],k in d

字典与列表的区别：

1. 键的类型可以是任何不变的类型，浮点数，整数，字符串，元组
2. 自动添加，即便字典中没有该键，也可赋值添加
3. 成员资格：k in d查找的是键

字符串格式设置功能用于字典" {key} ".format_map(dic)

字典方法

clear()删除所有字典项，返回None.

赋值，指向同一数据；copy,副本，浅复制(复制的新字典中值本身是原件)，深复制（连同值一起复制）

fromkeys创建含指定键的空值字典`{'name': None, 'age': None}`

访问字典get,不存在None,使用键索引不存在报错

items返回含所有字典项的列表[(k,v),(k,v),...],返回值是“字典视图”，不复制，是底层字典的反应。

dic.items()可复制

keys()返回键的字典视图

dic.pop('key')删除键值对

dic.popietm()随机删除，快，无需先获取键列表。字典无序，从最后删除的方法无意义。

setdefault,不存在添加，存在则不变，与get对应

update使用一个字典更新另一个，将参数添加入字典，若键存在，则进行值替换。

dic.values()可能包含重复值