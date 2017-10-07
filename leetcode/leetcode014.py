#coding=utf-8
#寻找列表中最长的字符串前缀
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str=''
        if ''in strs or not strs:
            return str
        strs=sorted(strs,cmp=lambda x,y:cmp(len(x),len(y)))
        tmp=strs[0]
        flag=1
        for i in range(len(tmp)):
            for k in range(1,len(strs)):
                if tmp[i] != strs[k][i]:
                    flag=0
                    break
            if flag:
                str+=tmp[i]
        return str
class Solution(object):
    def longestCommonPrefix(self,strs):
        if '' in strs or not strs:
            return ''
        shortest=min(strs,key=len)
        for tmp in strs:
            while tmp.find(shortest)!=0:
                shortest=shortest[:-1]
        return shortest