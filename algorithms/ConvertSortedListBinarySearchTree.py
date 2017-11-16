#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /ConvertSortedListBinarySearchTree.py
# Project: algorithms
# Created Date: Thursday, November 16th 2017, 8:36:33 pm
# Author: yanyan.yyy
# -----
# Last Modified: Thu Nov 16 2017
# Modified By: yanyan.yyy
# -----
###


# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        