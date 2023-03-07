# python3
# -*- encoding: utf-8 -*-
'''
@File    :   deque.py
@Time    :   2023/03/08 01:57:24
@Author  :   Qiaoxide
@Version :   1.0
@Contact :   qiaoxide@126.com
@License :   (C)Copyright 2021-2022, ThreeAtom
@Desc    :   None
'''

# here put the import lib
from collections import deque


def simple():
    q = deque(maxlen=3)
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)
    q.append(4)
    print(q)

simple()