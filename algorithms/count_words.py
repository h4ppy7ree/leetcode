#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /count_words.py
# Project: leetcode
# Created Date: Tuesday, August 22nd 2017, 1:31:28 pm
# Author: yanyan.yyy
# -----
# Last Modified: Tue Aug 22 2017
# Modified By: yanyan.yyy
# -----
###


"""Count words."""
def my_cmp(x, y):
    v = x[1] - y[1]
    if v == 0:
        return cmp(y[0], x[0])
    else:
        return v

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    
    # TODO: Return the top n most frequent words. 
    from collections import Counter
    top_n = dict(Counter(s.split(' ')))
    top_n = sorted(top_n.iteritems(), cmp=lambda a, b: my_cmp(a, b), reverse=True)
    if len(top_n) >= n:
        return top_n[0:n]
    else:
        return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
