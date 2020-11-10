#16.2.1mymath.py
def square(x):
    '''
计算平方并返回结果
>>> square(2)
4
>>> square(3)
9
'''
    return x * x
if __name__=='__main__':
    import doctest,my_math
    doctest.testmod(my_math)