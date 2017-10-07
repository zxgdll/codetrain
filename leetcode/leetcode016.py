#coding=utf-8
#在数组中，任选三个数，使该数的值靠近给定的target
class Solution(object):
	def threeSumCloest(self,nums,target):
		if len(nums)<3: return 0
        nums=sorted(nums)
        res=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            while l<r:
                tmp=nums[i]+nums[l]+nums[r]
                if res==target: return res
                if abs(res-target)>abs(tmp-target):
                    res=tmp
                if tmp<target:
                    l+=1
                else:
                    r-=1
        return res
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
            
        return result