# python3
# -*- encoding: utf-8 -*-
'''
@File    :   assign.py
@Time    :   2023/03/07 22:22:40
@Author  :   Qiaoxide
@Version :   1.0
@Contact :   qiaoxide@126.com
@License :   (C)Copyright 2021-2022, ThreeAtom
@Desc    :   None
'''

# python 语法学习，数据结构和算法

#


def printAssignMulVal():
    '''
    @Desc     :  解压序列赋值多个变量
    @Param    :  
    @Returns  :  
    '''
    p = (4, 5)
    x, y = p
    print('p=>', x, y)
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    print('Data=>', name, shares, price, date)
    name, shares, price, (year, mon, day) = data
    print('DataInfo=>', name, shares, price, year, mon, day)
    # 使用占位变量去丢掉
    _, shares, price, _ = data
    print('SimpleData=>', shares, price)


def avg(el):
    return(sum(el)/(len(el)))


def drop_first_last(grades):
    '''
    @Desc     :  解压可迭代对象赋值给多个变量
    @Param    :  
    @Returns  :  
    '''
    first, *middle, last = grades
    return avg(middle)


print(drop_first_last([1, 60, 60, 60, 100]))


printAssignMulVal()
