#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /removeList.py
# Project: leetcode
# Created Date: Wednesday, August 9th 2017, 9:04:15 pm
# Author: yanyan.yyy
# -----
# Last Modified: Wed Aug 09 2017
# Modified By: yanyan.yyy
# -----
###


import unittest
# 如果列表b的数字在列表a里面，就把这个数字从列表a去掉，返回a列表。


def removeList(a, b):
    if not a or not b:
        return a
    for i in b:
        for j in range(0, a.count(i)):
            a.remove(i)
    return a


a = [1, 2, 3, 4, 5, 1]
b = [1, 2, 3]
print removeList(a, b)


class TestRemoveList(unittest.TestCase):

    def test_null(self):
        self.assertEqual([], removeList([], [1, 2]))
        self.assertEqual([1, 2], removeList([1, 2], []))

    def test_empty(self):
        self.assertEqual(None, removeList(None, [1]))
        self.assertEqual([1], removeList([1], None))


unittest.main()
