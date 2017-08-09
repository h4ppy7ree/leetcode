#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /singleNumber.py
# Project: leetcode
# Created Date: Sunday, August 6th 2017, 6:46:58 pm
# Author: yanyan.yyy
# -----
# Last Modified: Sun Aug 06 2017
# Modified By: yanyan.yyy
# -----
###


# <https://leetcode.com/problems/single-number/description/>
'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''


class Solution(object):
    def singleNumber_old(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c = Counter(nums)
        for x in nums:
            if 1 == c[x]:
                return x
               
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for x in nums[1:]:
            result = result ^ x
        return result 


print Solution().singleNumber([2, 1, 3, 1, 2, 5, 5])