#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /ReverseString.py
# Project: leetcode
# Created Date: Saturday, August 5th 2017, 12:52:55 am
# Author: yanyan.yyy
# -----
# Last Modified: Sat Aug 05 2017
# Modified By: yanyan.yyy
# -----
###


'''
URL:<https://leetcode.com/problems/reverse-string/description/>
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''


class Solution(object):
    def reverseStringOld(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(reversed(s))

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        
        解题思路：
        python字符串切片，str[start:stop:step]
        当step等于-1时，每次步长为-1，相当于逆序。
        """
        return s[::-1]


if __name__ == "__main__":
    print Solution().reverseString('hello')