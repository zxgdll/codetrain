#!!/usr/bin/env python
# coding=utf-8


class Solution(object):
    """docstring for ClassName"""

    def romanToInt(self, s):
        d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
             'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        num = 0
        i = 0
        if len(s) < 2:
            return d[s]
        while i < len(s) - 1:
            if d[s[i]] >= d[s[i + 1]]:
                num += d[s[i]]
                if i + 1 == len(s) - 1:
                    num += d[s[i + 1]]
            else:
                num += d[s[i] + s[i + 1]]
                i = i + 1
                if i + 1 == len(s) - 1:
                    num += d[s[i + 1]]
            i += 1
        return num
a = Solution()
print a.romanToInt("DCXXI")
