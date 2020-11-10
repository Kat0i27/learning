#模板系统
'''
假设要把所有的'[something]'（字段）都替换为将something
作为Python表达式计算得到的结果。因此，下面的字符串：
'The sum of 7 and 9 is [7 + 9].'
应转换为：
'The sum of 7 and 9 is 16.'
另外，你还希望能够在字段中进行赋值，使得下面的字符串：
'[name="Mr. Gumby"]Hello, [name]'
转换成：
'Hello, Mr. Gumby'
'''
import fileinput,re

field_pat=re.compile(r'\[(.+?)\]')#变量获取

scope={}#变量收集

#re.sub:
def replacement(match):
    code=match.group(1)
    # print(match.group(1))
    try:
        #表达式
        return str(eval(code,scope))
    except SyntaxError:
        exec(code,scope)
        #执行该赋值语句,并返回空字串
        return ''

#获取所有文本整合为一个字符串
lines=[]
for line in fileinput.input():
    lines.append(line)
text=''.join(lines)


#替换
print(field_pat.sub(replacement,text))#替换函数替换'模式'.sub('函数返回替换值'，代替换文本)