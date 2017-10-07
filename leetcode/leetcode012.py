#!/usr/bin/env python
# coding=utf-8
# 方法一：减法原则，num从大数开始减，直到差小于减数，更换减数。


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1 or num > 3999:
            return ''
        d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
             'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        d_s = sorted(d.items(), key=lambda item: -item[1])
        result = ''
        for item in d_s:
            while num >= item[1]:
                result += item[0]
                num -= item[1]
        return result
a = Solution()
print(a.intToRoman(3999))
