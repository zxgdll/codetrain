#!/usr/env python
# coding=utf-8
# 队列重建，
# 思想是先对list进行排序，按照h降序,k升序,然后根据k插入。


class Solution:
    def reconstructQueue(self, people):
        p = sorted(people, key=lambda x: x[1])  # k正序
        # h逆序 也可以写成sorted(people,key=lambda x:(-x[0],x[1]))
        p1 = sorted(p, key=lambda x: -x[0])
        re = []
        for item in p1:
            re.insert(item[1], item)
        return re
a1 = [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7],
      [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]
b = Solution()
print(b.reconstructQueue(a1))
