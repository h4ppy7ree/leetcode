#!/usr/bin/env bash
###
# File: /TenthLine.sh
# Project: leetcode
# Created Date: Saturday, August 5th 2017, 1:01:17 pm
# Author: yanyan.yyy
# -----
# Last Modified: Sat Aug 05 2017
# Modified By: yanyan.yyy
# -----
###

# How would you print just the 10th line of a file?

# For example, assume that file.txt has the following content:

# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10
# Your script should output the tenth line, which is:
# Line 10


# Read from the file file.txt and output the tenth line to stdout.
# example: bash ./TenthLine.sh 10 1
# one line solusion
LINE_NUM=$1; LINES=$2; tail -n+$LINE_NUM ./file_TenthLine.txt | head -n $LINES
LINE_NUM=$1; LINES=$2; sed -n "${LINE_NUM},$((${LINES}-1))p" < ./file_TenthLine.txt

# awk文本处理
awk -v LINE_NUM=$1 -v LINES=$2 '{
    if(LINE_NUM <= NR && NR-LINE_NUM<LINES){
        print $0  
    }
}' ./file_TenthLine.txt