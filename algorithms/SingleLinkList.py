#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /SingleLinkList.py
# Project: algorithms
# Created Date: Sunday, November 12th 2017, 10:33:49 am
# Author: yanyan.yyy
# -----
# Last Modified: Sun Nov 12 2017
# Modified By: yanyan.yyy
# -----
###


# <https://leetcode.com/problems/reverse-linked-list/>
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next            
        return prev
