# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l_1 = 0
        l_2 = 0
        if not l1:
            return l2
        if not l2:
            return l1
        for x in range(len(l1)):
            l_1 += l1[x] * pow(10, x)
        for x in range(len(l2)):
            l_2 += l2[x] * pow(10, x)
        res = l_1 + l_2
        return list(str(res))[::-1]

    def pow(x, n):
        s = 1
        while n > 1:
            n -= 1
            s *= x
        return s
a = Solution()
b = a.addTwoNumbers([2, 4, 3], [5, 6, 4])
print(b)
