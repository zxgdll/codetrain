# sliding window unique elements sum

```python
'''
时间复杂度过高
'''
class Solution:
    """
    @param: : the given array
    @param: : the window size
    @return: the sum of the count of unique elements in each window
    """

    def slidingWindowUniqueElementsSum(self, nums, k):
        # write your code here
        res=0
        if k>len(nums):
            tmp=set(nums)
            for item in tmp:
                if nums.count(item)==1:
                    res+=1
            return res
        for i in range(len(nums)-k+1):
            tmp=set(nums[i:i+k])
            if len(tmp)!=k:
                for item in tmp:
                    if nums[i:i+k].count(item)==1:
                        res+=1
            else:
                res+=k
        return res
```