#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /数据结构_综合.py
# Project: algorithms
# Created Date: Sunday, November 12th 2017, 3:46:57 pm
# Author: yanyan.yyy
# -----
# Last Modified: Sun Nov 12 2017
# Modified By: yanyan.yyy
# -----
###


# 一个二叉树，转化成双向链表

class MySort(object):
    def __init__(self):
        self.numbers = [10, 7, 2, 5, 3, 11, 4]

    def insert_sort(self):
        '''插入排序'''
        new_nums = [10, 7, 2, 5, 3, 11, 4]
        l_num = len(new_nums)
        for i in range(1, l_num):
            R0 = new_nums[i]
            range_j = range(0, i)
            range_j.reverse()
            for j in range_j:
                if new_nums[j] > R0:
                    new_nums[j+1] = new_nums[j]
                    if j == 0:
                        new_nums[j] = R0 
                else:
                    new_nums[j+1] = R0
                    break
            print new_nums
        return new_nums

    def bubble_sort(self):
        '''冒泡排序'''
        new_nums = [5, 9, 3, 4, 7, 5, 8]
        count = len(new_nums)
        for i in range(0, count):
            for j in range(i + 1, count):
                if new_nums[j] < new_nums[i]:
                    new_nums[i], new_nums[j] = new_nums[j], new_nums[i]
        return new_nums

    def quick_sort(self, numb, i, j):
        '''快速排序'''
        new_nums = numb
        pivot = new_nums[-1]
        while True:
            print i, j
            if new_nums[i] < pivot:
                i += 1
            if new_nums[j] > pivot:
                j -= 1
            if new_nums[i] > pivot and new_nums[j] < pivot:
                new_nums[i], new_nums[j] = new_nums[j], new_nums[i]
                i += 1
                j -= 1
            if i >= j:
                pivot, new_nums[i] = new_nums[i], pivot
                break
        self.quick_sort(new_nums, 0, i-1)
        self.quick_sort(new_nums, j, len(new_nums)-1)
        return new_nums

# print MySort().insert_sort()
# print MySort().bubble_sort()


bumb = [51, 34, 78, 60, 12, 43, 89, 13, 74]
print MySort().quick_sort(bumb, 0, len(bumb) - 2)
