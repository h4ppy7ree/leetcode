#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /maxDepth.py
# Project: leetcode
# Created Date: Sunday, August 6th 2017, 9:11:13 pm
# Author: yanyan.yyy
# -----
# Last Modified: Sun Aug 06 2017
# Modified By: yanyan.yyy
# -----
###


# <https://leetcode.com/problems/maximum-depth-of-binary-tree/description/>
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))