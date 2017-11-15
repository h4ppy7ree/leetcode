#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /RemoveDuplicatesSortedList.py
# Project: algorithms
# Created Date: Sunday, November 12th 2017, 12:01:53 pm
# Author: yanyan.yyy
# -----
# Last Modified: Sun Nov 12 2017
# Modified By: yanyan.yyy
# -----
###


# <https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/>
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr and curr.next:
            next = curr.next
            if curr.val == next.val:
                curr.next = next.next
            else:
                curr = curr.next
        return head