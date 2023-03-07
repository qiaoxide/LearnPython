# python3
# -*- encoding: utf-8 -*-
'''
@File    :   yield.py
@Time    :   2023/03/08 01:24:53
@Author  :   Qiaoxide
@Version :   1.0
@Contact :   qiaoxide@126.com
@License :   (C)Copyright 2021-2022, ThreeAtom
@Desc    :   带有 yield 的函数在 Python 中被称之为 generator
'''

# here put the import lib


def fab(max):
    '''
    @Desc     :  没有yields的函数
    @Param    :  
    @Returns  :  
    '''
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a+b
        n = n+1
    return L


def fabIterable(max):
    '''
    @Desc     :  迭代器版本
    @Param    :  
    @Returns  :  
    '''
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1


print(fab(5))

f=fabIterable(5)

print(f.__next__(),f.__next__(),f.__next__())

