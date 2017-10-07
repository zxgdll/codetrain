#!/usr/bin/env python
# coding=utf-8


class Solution(object):
    """docstring for myAtoi"""

    def myAtoi(self, str):
        INT_M = 2**31
        if len(str) == 0:
            return 0
        l = list(str.strip())
        flag = -1 if l[0] == '-' else 1
        if l[0] in ['+', '-']:
            del l[0]
        reg, i = 0, 0
        while i < len(l) and l[i].isdigit():
            reg = reg * 10 + int(l[i])
            i += 1
        return max(-INT_M, min(reg * flag, INT_M - 1))
