#!/usr/bin/env python
# coding=utf-8

# 常规思维，O(n^2)复杂度，会引起TLE错误。
'''class Solution(object):
    """docstring for Solution"""

    def maxArea(self, height):
        if len(height) < 2:
            return 0
        max = 0
        result = []
        for i in range(len(height) - 1):
            for j in range(i, len(height)):
                maxa = min(height[i], height[j]) * (j - i)
                if maxa > max:
                    max = maxa
        return max'''

# 线性复杂度


class Solution(object):
    """docstring for Solution"""

    def maxArea(self, height):
        if len(height) < 2:
            return 0
        i = 0
        j = len(height) - 1
        max = 0
        while i < j:
            maxa = min(height[i], height[j]) * (j - i)
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
            if max < maxa:
                max = maxa
        return max
a = Solution()
b = a.maxArea([1, 1])
print b
