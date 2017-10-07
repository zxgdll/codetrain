class solution(object):
	"""docstring for solution"""
	#方法1
	def countBits(self,num):
		cout=[0]
		for x in range(num+1):
			cout.append(bin(x).count('1'))
		return cout
	#方法2,x&(x-1)计算1的个数
	def countBits(self,num):
		cout=[]
		num1=0;
		for x in range(num+1):
			while x:
				x=x&(x-1)
				num1+=1
			cout.append(num1)
			num1=0
		return cout
# a=solution()
# print(a.countBits(5))
 			
# a=bin(5)
# print(type(a))
# print(a.count('1'))