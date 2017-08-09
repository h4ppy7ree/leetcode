#!/usr/bin/env bash
###
# File: /TransposeFile.sh
# Project: leetcode
# Created Date: Sunday, August 6th 2017, 10:11:22 am
# Author: yanyan.yyy
# -----
# Last Modified: Sun Aug 06 2017
# Modified By: yanyan.yyy
# -----
###


# <https://leetcode.com/problems/transpose-file/description/>
# 
filename='./file.txt'

awk '{
    for(i=1; i<=NF; i=i+1){
        if(FNR==1){
            s[i-1]=$i;
        }
        else{
            s[i-1]=s[i-1]" "$i
        }
    }
}END{
    for(i=0; i<length(s); i=i+1){
        print s[i];
    }
}' $filename


# 这个方法打开文件太多次了，很耗内存
for (( i=1 ; i<=`awk 'END{print NF}' $filename` ; i=(($i+1)) ))
do
    awk -v i=$i '{print $i}' $filename | xargs
done


# 计算文件列数，非awk的方法
a=(`cat ./file.txt`) && echo ${#a[@]}

# shell 二维数组
# shell本身不支持二维数组，只支持一维数组。
# 一、定义数组
# 1、赋值
# array=(value1 value2 ...... valueN)             #从下标0开始依次赋值
# array=([1]=value1 [2]=value2 [0]=value0)        #指定下标赋值
# declare -a array=(value1 value2 ...... valueN)  #声明+赋值，也可以只声明
# unixtype=('Debian' 'Red Hat' 'Fedora')          #如果元素有空格，就要用引号
# read -a array                  #-a表示从标准输入读入数组，遇到换行为止
# 2、查看值
# set | grep unixtype                                 #利用set查看数组赋值情况
# echo "${array[@]}"              #显示数组的值
# 3、清除数据
# unset array                     #清除数组
# unset array[1]                 #清除数组的指定元素
 
# 二、数组变量
# # 取得数组元素的个数
# length=${#array_name[@]}
# # 或者
# length=${#array_name[*]}
# # 取得数组单个元素的长度
# lengthn=${#array_name[n]}
# #取得数组下标的值
# ${!array[@]}
# #从数组的n位置开始取m个元素
# ${array[@]:n:m}

# 三、数组的常用操作
# 1、命令执行结果放入数组
# $ array=($(ls | grep '.sh'))
# 或
# $ array=(`ls | grep '.sh'`)
# 2、判断某值是否在数组里面？
# $ echo ${unixtype[@]} | grep -q 'a'
# $ echo $?
# 0
# $ echo ${unixtype[@]} | grep -wq 'abc'
# $ echo $?
# 1
# 或
# for i in ${array[@]};do
#    if [ "$i" = "${member}" ];then
#    ....
#    fi
# done

# 5、构建二维数组
# a=('1 2 3' '4 5 6' '7 8 9')             #赋值，每个元素中都有空格
# for i in ${a[@]} ; do
#    b=($i)                                    #赋值给b，这样b也是一个数组
#    for j in ${b[@]};do                  #相当于对二元数组操作
#    ......
#    done
# done

# 6、文件内容读入数组
# cat /etc/shells | tr "\n" " " >/tmp/tmp.file                      #回车变空格
# read -a array < /tmp/tmp.file                                       #读入数组
# set | grep array
# # array=([0]="/bin/sh" [1]="/bin/bash" [2]="/sbin/nologin" [3]="/bin/tcsh" [4]="/bin/csh" [5]="/bin/dash")