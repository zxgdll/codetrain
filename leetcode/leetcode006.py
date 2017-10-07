#!/usr/bin/env python
# coding=utf-8
# 我自己的方法就是找到之字形输出的规律
# 更好的方法，是更改index来输入每个字符


class Solution(object):
    """docstring for """
    # def convert(self, s, numRows):
    #     s_num = len(s)
    #     n = 2 * numRows - 2
    #     l = []
    #     if s_num <= numRows or numRows == 1 or numRows == 0:
    #         return s
    #     for x in range(0, numRows - 1):
    #         ss = ''
    #         y = x
    #         mid = 0
    #         while y < s_num or mid < s_num:
    #             if y < s_num:
    #                 ss += s[y]
    #             mid = y + (numRows - 1 - x) * 2
    #             y += n
    #             if mid < s_num and mid != y:
    #                 ss += s[mid]
    #         l.append(ss)
    #     ss = ''
    #     end = numRows - 1
    #     while end < s_num:
    #         ss += s[end]
    #         end += n
    #     l.append(ss)
    #     res = ''
    #     for x in range(numRows):
    #         res += l[x]
    #     return res

    def convert(self, s, numRows):
        if numRows == 1 or len(s) <= numRows:
            return s
        L = [''] * numRows
        index, step = 0, 1
        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(L)

a = Solution()
b = a.convert('abcd', 2)
print(b)
