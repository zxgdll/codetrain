#!/usr/bin/python
# coding=utf-8
# 原始的解法是通过遍历两次循环求解。
# 较快的解法则是构建dict，dict搜索属于hash


class Solution(object):
    def twoSum(self, nums, target):
        # result = []
        # for x in range(len(nums) - 1):
        #     for y in range(x + 1, len(nums)):
        #         if nums[x] + nums[y] == target:
        #             result.append(x)
        #             result.append(y)
        # return result
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return d[target - num], i
            d[num] = i
a = Solution()
b = a.twoSum([1, 0, 4, 3, 5, 0, 6], 0)
print b
