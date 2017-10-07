#!/usr/env python
# coding=utf-8
#新方法使用游标方法
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 第一种方法时间复杂度为O(n^2)
        # b = {}
        # for x in range(len(s)):
        #     a = ''
        #     for y in range(x, len(s)):
        #         if s[y] not in a:
        #             a += s[y]
        #         else:
        #             break
        #     b[a] = len(a)
        # if b:
        #     return max(b.values())
        # else:
        #     return 0
        res = 0
        left = 0
        d = {}
        for i, ch in enumerate(s):
            if ch in d and d[ch] >= left:
                left = d[ch] + 1
            d[ch] = i
            res = max(res, i - left + 1)
        return res
a = Solution()
print(a.lengthOfLongestSubstring('z'))
