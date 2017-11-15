#!/usr/bin/env bash
###
# File: /NetworkTCP.sh
# Project: leetcode
# Created Date: Saturday, August 5th 2017, 4:48:32 pm
# Author: yanyan.yyy
# -----
# Last Modified: Sat Aug 05 2017
# Modified By: yanyan.yyy
# -----
###

# 查看TCP流量

netstat -n -p TCP
# Active Internet connections
# Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)
# tcp4       0      0  192.168.0.140.53174    139.198.189.246.443    ESTABLISHED
# tcp4       0      0  192.168.0.140.53172    168.63.242.221.443     ESTABLISHED
# tcp4       0      0  192.168.0.140.53171    203.205.158.61.443     ESTABLISHED
# tcp4       0      0  192.168.0.140.53168    74.125.200.94.80       ESTABLISHED
# tcp4       0      0  192.168.0.140.53167    52.206.2.232.443       CLOSE_WAIT
# tcp4       0      0  192.168.0.140.53165    172.217.27.14.443      ESTABLISHED
# tcp4       0      0  192.168.0.140.53157    172.217.27.3.443       ESTABLISHED
# tcp4       0      0  192.168.0.140.53155    74.125.200.94.443      ESTABLISHED
# tcp4       0      0  192.168.0.140.53098    40.114.95.106.80       ESTABLISHED
# tcp4       0      0  192.168.0.140.52901    176.34.125.100.443     ESTABLISHED
# tcp4       0      0  192.168.0.140.50240    54.254.226.83.443      ESTABLISHED
# tcp4       0      0  192.168.0.140.49718    17.188.166.11.5223     ESTABLISHED
# tcp4       0      0  192.168.0.140.49715    74.125.68.188.5228     ESTABLISHED
# tcp4       0      0  192.168.0.140.49684    17.252.156.226.5223    ESTABLISHED
# tcp4       0      0  192.168.0.140.53166    52.206.2.232.443       TIME_WAIT