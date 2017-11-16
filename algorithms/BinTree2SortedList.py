#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /BinTree2SortedList.py
# Project: algorithms
# Created Date: Thursday, November 16th 2017, 8:48:13 pm
# Author: yanyan.yyy
# -----
# Last Modified: Thu Nov 16 2017
# Modified By: yanyan.yyy
# -----
###

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#         self.prev = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def __init__(self):
        self.head = None
        self.curr = None

    def add_dblist(self, val):
        prev_node = self.curr
        self.curr = ListNode(val)
        if prev_node != None:       # 如果是不是第一个节点，就把前一个节点的next指向他
            prev_node.next = self.curr
        if self.head == None:       # 如果是第一个节点，则把head指向当前节点
            self.head = self.curr
        self.curr.prev = prev_node  # 当前节点的prev等于前一个节点
        

    def BST_to_dblist(self, root):  # 前序遍历
        if root == None:
            return
        self.add_dblist(root.val)
        self.front_read_BST(root.left)
        self.front_read_BST(root.right)