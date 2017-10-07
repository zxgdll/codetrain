#!/usr/bin/env python
# coding=utf-8


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            s = str(x)
            s = s[::-1]
            return [0, int(s)][int(s) <= (2**31 - 1)]
        else:
            s = str(x)
            s = s[:0:-1]
            return [0, -int(s)][int(s) <= 2**31]
