# python3
# -*- encoding: utf-8 -*-
'''
@File    :   heapq.py
@Time    :   2023/03/10 01:39:35
@Author  :   Qiaoxide
@Version :   1.0
@Contact :   qiaoxide@126.com
@License :   (C)Copyright 2021-2022, ThreeAtom
@Desc    :   
'''

# here put the import lib
import heapq

nums = [1, 8, 2, 23, 7, -4, 42, 37, 55]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
heapq.heapify(nums)
print(nums)
