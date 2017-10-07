#!/usr/bin/env python
# coding=utf-8


class Solution(object):
    """docstring for Solution"""

    def isPalindrome(self, x):
        l = list(str(x))
        return l == l[::-1]
