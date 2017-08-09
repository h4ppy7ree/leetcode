#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /decorator.py
# Project: leetcode
# Created Date: Monday, August 7th 2017, 7:40:06 pm
# Author: yanyan.yyy
# -----
# Last Modified: Mon Aug 07 2017
# Modified By: yanyan.yyy
# -----
###


# 无参数的修饰符使用
def deco(func):
    print "* before func() called."
    func()
    print "* after func() called."
    return func


# 内嵌包装函数(常用)
def deco_1(func):
    def _deco():
        print("before myfunc() called.")
        func()
        print("  after myfunc() called.")
        # 不需要返回func，实际上应返回原函数的返回值
    return _deco


# 对带参数的函数进行装饰
def deco_2(func):
    def _deco(a, b):
        print("before myfunc() called.")
        func(a, b)
        print("  after myfunc() called.")
    return _deco


# 对参数数量不确定的函数进行装饰
def deco_3(func):
    def _deco(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _deco


@deco_3
def myfunc():
    print "* myfunc() called."


@deco_3
def myfunc_1(a, b):
    print "* myfunc(" + a + ", " + b + ") called."


@deco_3
def myfunc_2(a, b, c):
    print "* myfunc(" + a + ", " + b + ", " + c + ") called."


# <http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html>
myfunc()
myfunc_1("1", "2")
myfunc_2("1", "2", "3")


# 装饰器带类参数
class locker:
    def __init__(self):
        print("locker.__init__() should be not called.")
         
    @staticmethod
    def acquire():
        print("locker.acquire() called.（这是静态方法）")
         
    @staticmethod
    def release():
        print("  locker.release() called.（不需要对象实例）")


def deco_4(cls):
    '''cls 必须实现acquire和release静态方法'''
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, cls))
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()
        return __deco
    return _deco


@deco_4(locker)
def myfunc_3():
    print(" myfunc() called.")


myfunc_3()


class A():
    def __init__(self):
        self.__t = 0
        self.s = 1

    def __a(self):
        print "_a"

    def z(self):
        print "z"


def print_directory_contents(sPath):
    import os
    print os.path
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print sChildPath


print_directory_contents('./')


from os import walk


f = []
mypath = '.'
for (dirpath, dirnames, filenames) in walk(mypath):
    print dirpath, dirnames, filenames
    f.extend(filenames)
    break
print f
