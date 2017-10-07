#coding=utf-8
class Solution(object):
	"""仿照手机里的数字面板，给定一个数字字符串，返回数字可能表示的所有可能的字母组合
	"""
	def letterCombinations(self, digits):
		dic={"1":"*","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz","0":" "}
		res=[]
		if len(digits)<1:
			return res
		res.append("")
		for i in digits:
			tmp=[]
			for j in range(len(dic[i])):
				for k in range(len(res)):
					tmp.append(res[k]+dic[i][j])
			res=tmp
		return res
a=Solution()
b='10'
print a.letterCombinations(b)