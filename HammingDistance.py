# -*- coding: utf-8 -*-
'''
/*
 * @Author: yanyan.yyy 
 * @Date: 2017-08-04 23:23:07 
 * @Last Modified by: yanyan.yyy
 * @Last Modified time: 2017-08-05 00:35:07
 */
 '''

'''
URL:<https://leetcode.com/problems/hamming-distance/description/>
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 2^31

Example:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ?   ?
The above arrows point to positions where the corresponding bits are different.
'''

class Solution(object):
    def hammingDistance_old(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        BinX = bin(x)[2:]
        BinY = bin(y)[2:]
        count = 0
        if len(BinX) >= len(BinY):
            BinY = '0'*(len(BinX)-len(BinY)) + BinY
        else:
            BinX = '0'*(len(BinY)-len(BinX)) + BinX
        for i in range(0, len(BinX)):
            if BinX[i] != BinY[i]:
                count+=1
        return count

    def hammingDistance(self, x, y):
        '''
        解题思路：位运算
            按位与：a & b。两个位都是1时，得1
            按位或：a | b。其中一个位有1时，得1
            异或：a ^ b。两个位相同则为0，不同则为1
            取反：~a
            左移：a<<b
            右移：a>>b
        '''
        return bin(x ^ y).count('1')

if __name__ == "__main__":
    print Solution().hammingDistance(1,4)