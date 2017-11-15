#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /sepString.py
# Project: leetcode
# Created Date: Wednesday, August 9th 2017, 9:16:49 pm
# Author: yanyan.yyy
# -----
# Last Modified: Wed Nov 01 2017
# Modified By: yanyan.yyy
# -----
###


# 开发题：一串数字，转换为逗号分隔3位的字符串。
def reStr(a):
    str_a = str(a)
    len_a = len(str_a)
    output = str_a[-3:]
    if len_a > 3:
        for i in range(2, len_a / 3 + 1):
            output = str_a[-3*i:-3*i+3] + "," + output
        if len_a % 3 != 0:
            output = str_a[:len_a % 3] + "," + output
    return output


print reStr(1265.1212)

print("{:,}".format(1265.1212));
