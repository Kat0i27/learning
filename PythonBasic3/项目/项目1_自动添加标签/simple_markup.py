#simplemarkup.py 一个简单的标记程序
'''
可创建简单的标记脚本。为此，可按如下基本步骤进行。
    (1) 打印一些起始标记。
    (2) 对于每个文本块，在段落标签内打印它。
    (3) 打印一些结束标记。

这里假设要将第一个文本块放在一级标题标签（h1）内，而不是段
落标签内。另外，还需将用星号括起的文本改成突出文本（使用标签em）。这样程序将更有用一些
'''
#python simple_markup.py < test_input.txt >test_output.html
import sys,re
from util import *

print('<html><head><title></title><body>')

title=True
for block in blocks(sys.stdin):
    block=re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title=False
    else:
        print('<p>')
        print(block)
        print('</p>')
print('</body></html>')