#!/usr/bin/env bash
###
# File: /WordFrequency.sh
# Project: leetcode
# Created Date: Saturday, August 5th 2017, 10:53:02 pm
# Author: yanyan.yyy
# -----
# Last Modified: Sun Aug 06 2017
# Modified By: yanyan.yyy
# -----
###


# 
cat ./words.txt | tr ' ' '\n' | sort | uniq -c |sort -r | awk '{
    if($2~/[[:alnum:]]/){
        print $2,$1
    }
}'

# TODO: shell命令中使用正则的坑
echo -e 'a  a   b ' | tr ' ' '\n' | sort | uniq -c |sort -r | awk '{
    if($2~/[[:alnum:]]/){
        print $2,$1
    }
}'

