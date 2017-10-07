#!/usr/bin/python
#coding=utf-8
#3Sum
#给定一组数组，找到该整数数组中满足和为0的三个数字组合。
class Solution(object):
	def threeSum(self,nums):
		result=[]
		num1=sorted(nums)
		n=len(num1)
		for x in range(0,n):
			if x==0 or (x>0 and num1[x]!=num1[x-1]):
				target=-num1[x]
				l,r=x+1,n-1
				while l<r:
					if num1[l]+num1[r]==target:
						result.append([num1[x],num1[l],num1[r]])
						while l<r and num1[l]==num1[l+1]: l+=1
						while l<r and num1[r]==num1[r-1]: r-=1
						l+=1
						r-=1
					elif num1[l]+num1[r]<target:
						l+=1
					else:
						r-=1
		return result
a=Solution()
S = [-1, 0, 1, 2, -1, -4]
b=a.threeSum(S)
print b