#
'''
问题描述
你要给纯文本文件添加格式。假设你要将一个文件用作网页，而给你文件的人嫌麻烦，没有以HTML格式编写它。你不想手工添加需要的所有标签，想编写一个程序来自动完成这项工作。

功能分析
输入无需包含人工编码或标签。
程序需要能够处理不同的文本块（如标题、段落和列表项）以及内嵌文本（如突出的文本和URL）。
虽然这个实现添加的是HTML标签，但应该很容易对其进行扩展，以支持其他标记语言。
工具分析
肯定需要读写文件（参见第11章），至少要从标准输入（sys.stdin）读取以及使用print进行输出。
可能需要迭代输入行（参见第11章）
需要使用一些字符串方法（参见第3章）。
可能用到一两个生成器（参见第9章）。
可能需要模块re（参见第10章）。  如果你不熟悉上述任何概念，请花点时间复习一下。


 解析器：添加一个读取文本并管理其他类的对象。
 规则：对于每种文本块，都制定一条相应的规则。这些规则能够检测不同类型的文本块
并相应地设置其格式。
 过滤器：使用正则表达式来处理内嵌元素。
 处理程序：供解析器用来生成输出。每个处理程序都生成不同的标记。


这个程序存在如下潜在的扩展空间。
 增加对表格的支持。为此，只需找出左对齐内容的边界，并将文本块分成多列。
 突出全部大写的单词。为此，需要考虑缩略语、标点、姓名和其他首字母大写的单词。
 支持LATEX格式的输出。
 编写一个执行其他处理（而不是添加标记）的处理程序，如以某种方式对文档进行分析。
 创建一个脚本，将特定目录中的所有文本文件都自动转换为HTML文件。
 了解其他纯文本格式，如Markdown、reStructuredText或维基百科使用的格式。

'''

#处理程序的超类
class Handler:
    '''
    方法callback负责根据指定的前缀（如'start_'）和名称（如'paragraph'）查找相应的方
    法。这是通过使用getattr并将默认值设置为None实现的。
    如果getattr返回的对象是可调用的，就使用额外提供的参数调用它。
    例如，调用handler.callback('start_', 'paragraph')时，将调用方法handler.start_paragraph且不提供任何参数——如果start_paragraph存在的话
    '''
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method): return method(*args)

    def start(self, name):self.callback('start_', name)

    def end(self, name):self.callback('end_', name)

    def sub(self, name):#eg.name:emphasis
        def substitution(match):
            result = self.callback('sub_', name, match)#调用函数sub_emphasis(match)
            if result is None: match.group(0)
            return result
        return substitution#返回一个函数，调用函数将调用函数sub_emphasis

#处理程序
class HTMLRenderer:
    #段落处理方法
    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('/p')

    #正则表达式替换函数
    def sub_emphasis(self,match):
        return '<em>{}</em>'.format(match.group(1))
    #向处理程序提供实际文本
    def feed(self,data):
        print(data)

#规则：
    '''
    规则是供主程序（解析器）使用的。主程序必须根据给定的文本块选择合适的规则来对其进
    行必要的转换。换而言之，规则必须具备如下功能。
     知道自己适用于那种文本块（条件）。
     对文本块进行转换（操作）。
    因此每个规则对象都必须包含两个方法：condition和action。
    方法condition只需要一个参数：待处理的文本块。它返回一个布尔值，指出当前规则是否适用于处理指定的文本块。
    方法action也将当前文本块作为参数，但为了影响输出，它还必须能够访问处理器对象。
    有些情况下，应用一个规则后还可应用其他规则。需要给方法action再添加一项功能：让它返回一个布尔值，指出是否就此结束对当前文本块的处理
    '''
class HeadlineRule:#标题规则伪代码
    def condition(self, block):
        pass
        #如果文本块符合标题的定义，就返回True；
        #否则返回False。
    def action(self, block, handler):
        #调用诸如handler.start('headline')、handler.feed(block）和handler.end('headline')等方法。
        #我们不想尝试其他规则，因此返回True，以结束对当前文本块的处理。


#规则超类：
    '''多个规则可能执行相同的操作：调用处理程序的方法
    start、feed和end，并将相应的类型字符串作为参数，再返回True'''
class Rule:
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True

#过滤器
#handler类包含方法sub

#解析器
    '''parser类它使用一个处理程序以及一系列规则和过滤器
    将纯文本文件转换为带标记的文件（这里是HTML文件）'''
class Parser：
    def __init__ (self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []
    def addRule(self, rule):
        self.rules.append(rule)
    def addFilter(self, pattern, name):
        def filter(block, handler):#创建过滤器
            return re.sub(pattern, handler.sub(name), block)#规则，替换类型，文字块
        self.filters.append(filter)#在过滤器列表中添加过滤器
    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
        for rule in self.rules:
            if rule.condition(block):
                last = rule.action(block, self.handler)
                if last: break
        self.handler.end('document')


#规则和过滤器
'''
    标题是只包含一行的文本块，长度最多为70个字符。以冒号结束的文本块不属于标题。
    题目是文档中的第一个文本块，前提条件是它属于标题。
    列表项是以连字符（-）打头的文本块。
    列表以紧跟在非列表项文本块后面的列表项开头，以后面紧跟着非列表项文本块的列表项结束。
'''
class HeadingRule(Rule):
"""
标题只包含一行，不超过70个字符且不以冒号结尾
"""
    type = 'heading'
    def condition(self, block):
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'

class TitleRule(HeadingRule):
"""
题目是文档中的第一个文本块，前提条件是它属于标题
"""
    type = 'title'
    first = True
    def condition(self, block):
        if not self.first: return False
        self.first = False
        return HeadingRule.condition(self, block)

class ListItemRule(Rule):
"""
列表项是以连字符打头的段落。在设置格式的过程中，将把连字符删除
"""
    type = 'listitem'
    def condition(self, block):
        return block[0] == '-'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())#它删除了文本块中的第一个字符（连字符），并删除了余下文本中多余的空白
        handler.end(self.type)
        return True

class ListRule(ListItemRule):
"""
列表以紧跟在非列表项文本块后面的
列表项开头，以相连的最后一个列表
项结束
"""
    type = 'list'
    inside = False
    def condition(self, block):#检查所有文本块
        return True
    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)#刚进入列表
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)#刚离开列表
            self.inside = False
        return False

class ParagraphRule(Rule):
"""
段落是不符合其他规则的文本块
"""
    type = 'paragraph'
    def condition(self, block):
        return True

#过滤器-正则表达式
r'\*(.+?)\*'#突出内容
r'(http://[\.a-zA-Z/]+)'#url
r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)'#email