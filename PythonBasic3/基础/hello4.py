#hello4.py
def hello():
	print('Hello,world!')
def test():
	hello()

if __name__=='__main__':#作为程序运行，执行函数hello,否则行为像普通模块，单独写hello(),则导入时会调用
	test()
