#util.py 一个文本块生成器
'''
一种简单的方法是，收集空行前的所有行并将它们返回，然后重复这样的操作。不需要收集空行，因此不需要返回空文本块（即多个空行）。另外，必须确保文件的最
后一行为空行，否则无法确定最后一个文本块到哪里结束。（当然，有其他确定这一点的方法。）
'''
def lines(file):#在文件末尾添加一个空行
    for line in file:yield line
    yield '\n'

def blocks(file):
    '''
    生成文本块时，将其包含的所有行合并，并将两端多余的空白（如列表项缩进和换行符）
删除，得到一个表示文本块的字符串
    '''
    block=[]
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:#对于空行
            yield ''.join(block).strip()#将上述所得行合并为一个字串，作为一个块
            block=[]