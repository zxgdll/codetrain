#!/usr/env/python
#coding=utf-8
#Fizz Buzz 题意：字符串输出1 到 n，如果这个数是3的倍数则输出‘Fizz’，如果是5
#的倍数则是Buzz，如果是3 和 5共同的倍数则输出'Fizzbuzz'
class Solution(object):
	"""docstring for """
	def fizzBuzz(self,n):
		cout=[]
		for x in xrange(1,n+1):
			if x%3==0 and x%5==0:
				cout.append('Fizzbuzz')
			elif x%3==0:
				cout.append('Fizz')
			elif x%5==0:
				cout.append('Buzz')
			else:
				cout.append(str(x))
		return cout
# a=Solution()
# print(a.fizzBuzz(15))				