#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /数据结构_单链表.py
# Project: algorithms
# Created Date: Sunday, November 12th 2017, 3:37:39 pm
# Author: yanyan.yyy
# -----
# Last Modified: Sun Nov 12 2017
# Modified By: yanyan.yyy
# -----
###


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Soluction(object):
    def __init__(self):
        numbers = [1, 1, 1, 2, 6, 3, 0]
        linkList = None
        for x in numbers:
            linkList = self.addNode(linkList, x)
        self.linkList = linkList
        self.displayList(self.linkList)
        
    def addNode(self, head, x):
        new_node = ListNode(x)
        curr = head
        if not curr:
            return new_node
        while curr:
            if not curr.next:
                curr.next = new_node
            else:
                curr = curr.next
        return head

    def deleteNode(self, head, x):
        curr = head
        prev = None
        while curr:
            if curr.val == x:
                if not prev:
                    curr = curr.next
                else:
                    prev.next = curr.next
            else:
                prev = curr
                curr = curr.next
        return head
    
    def queueNode(self, head, x):
        curr = head
        while curr:
            if curr.val == x:
                return curr
            else:
                return None
            curr = curr.next

    def changeNode(self, head, x, y):
        if not head:
            return None
        node = self.queueNode(head, x)
        node.val = y
        return y

    def insertNode(self, head, x, y):
        new_node = ListNode(y)
        if not head:
            return new_node
        node = self.queueNode(head, x)
        new_node.next = node.next
        node.next = new_node

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

    def displayList(self, linkList):
        curr = linkList
        while curr:
            print curr.val
            curr = curr.next

    def insert_sort(self, linkList):
        # 
        
