# -*- coding: utf-8 -*-
'''
/*
 * @Author: yanyan.yyy 
 * @Date: 2017-08-04 23:23:07 
 * @Last Modified by: yanyan.yyy
 * @Last Modified time: 2017-08-05 01:08:16
 */
 '''

'''
URL:<https://leetcode.com/problems/reverse-string/description/>
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''
class Solution(object):
    def reverseString_old(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(reversed(s))

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

if __name__ == "__main__":
    print Solution().reverseString('hello')