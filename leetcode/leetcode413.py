#!/bin/env python
#coding=utf-8
#arithmetic slices
#找等差数列的数目
#[1,2,3,4]
# 数组	等差数列的数目	与上一数组的等差数列数目比较
# 1 2 3	1	1 - 0 = 1
# 1 2 3 4	3	3 - 1 = 2
# 1 2 3 4 5	6	6 - 3 = 3
# 1 2 3 4 5 6	10	10 - 6 = 4
# 1 2 3 4 5 6 7	15	15 - 10 = 5
# 观察就能发现两个等差数列数目之差（表格第三列）就是[1,2, 3, 4, 5……]这个序列，因此每次增加一个等差数列的元素，总的等差数列的数目就会增加[1,2, 3, 4, 5……]中对应的数值。

# 按照这一点，在代码实现时就设置一个变量dem，表示增加的数目，它对应着[1,2, 3, 4, 5……]这个序列，如果下一个数组元素能够加入到等差数列中，addend就自增1，然后总的数目就增加addend。如果下一个数组元素不能加入到等差数列中，addend就重置为0。这样通过一个循环就能获得结果。
class Solution(object):
    def numberOfArithmeticSlices(self, A):
    	count=0;
    	dem=0;
    	if len(A)<3:
    		return count
    	for x in range(1,len(A)-1):
    		if (A[x]-A[x-1])==(A[x+1]-A[x]):
    			dem+=1
    			count+=dem
    		else:
    			dem=0;
    	return count
# a=Solution()
# b=[1,2,3,4,5,6,9,10,11]
# print(a.numberOfArithmeticSlices(b))
