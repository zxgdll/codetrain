#!/bin/env python
#coding=utf-8
#nim game 
#共有n个石头，两人进行游戏，每次可以移走1-3个石头，移走最后一个石头的人为胜者。
#遇到4的倍数，先手的人必输。
class Solution(object):
	"""docstring for Solution"""
	def canWinNim(self,n):
		if n%4==0:
			return False
		else:
			return True
a=Solution()
print(a.canWinNim(5))