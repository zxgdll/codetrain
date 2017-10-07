# 对排序的nums1和nums2，求中间数
# 该算法：将两个nums变成一个list，排序后求中间数。


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        num = sorted(num)
        if len(num) % 2 == 0:
            return (num[int(len(num) / 2)] + num[int(len(num) / 2 - 1)]) / 2.0
        else:
            return num[int(len(num) / 2)]
a = Solution()
print(a.findMedianSortedArrays([1, 2], [3]))
