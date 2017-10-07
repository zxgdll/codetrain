#斐波那契数列问题是很经典的一个问题，通常解法是根据f(n)=f(n-1)+f(n-2)，写递归算法，但是如果深度过大，会出现栈溢出

#O(n^2),递归解法
class Solution(object):
	'''
	f(1)=0
	f(2)=1
	f(n)=f(n-1)+f(n-2)
	'''
	def Fib1(self,n):
		if n==1:
			return 0
		if n==2:
			return 1
		return Fib(n-1)+Fib(n-2)


	def Fib2(self,n):
		'''
		循环替代递归
		'''
		if n==1:
			return 0
		if n==2:
			return 1
		a,b=0,1
		for i in range(2,n):
			a,b=b,a+b
		return b


	def Fib3(self,n):