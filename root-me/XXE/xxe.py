#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /root-me/XXE/xxe.py
# Project: leetcode
# Created Date: Sunday, August 13th 2017, 6:48:00 pm
# Author: yanyan.yyy
# -----
# Last Modified: Sun Aug 13 2017
# Modified By: yanyan.yyy
# -----
###


from lxml import etree


parser = etree.XMLParser(recover=True)     # recovers from bad characters.resolve_entities = False
tree = etree.parse("xxe.rss", parser)


print tree
