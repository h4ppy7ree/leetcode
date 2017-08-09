#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /FizzBuzz.py
# Project: leetcode
# Created Date: Sunday, August 6th 2017, 6:15:29 pm
# Author: yanyan.yyy
# -----
# Last Modified: Sun Aug 06 2017
# Modified By: yanyan.yyy
# -----
###


# <https://leetcode.com/problems/fizz-buzz/description/>
'''
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number 
and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.
Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = [""] * n
        for i in range(1, n+1):
            if not i % 3:
                output[i-1] += "Fizz"
            if not i % 5:
                output[i-1] += "Buzz"
            if 0 != i % 3 and 0 != i % 5:
                output[i-1] = str(i)
        return output


print Solution().fizzBuzz(15)