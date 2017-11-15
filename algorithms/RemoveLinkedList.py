#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /RemoveLinkedList.py
# Project: algorithms
# Created Date: Sunday, November 12th 2017, 11:17:09 am
# Author: yanyan.yyy
# -----
# Last Modified: Sun Nov 12 2017
# Modified By: yanyan.yyy
# -----
###


# <https://leetcode.com/problems/remove-linked-list-elements/description/>
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            if curr.val == val:
                if not prev:
                    curr = curr.next
                    head = curr
                else:
                    prev.next = curr.next
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head