# Two Sum
Given nums = [2, 7, 11, 15], target = 9
return [1, 2]

```python
class Solution:
    """
    @param: nums: an array of Integer
    @param: target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        res={}
        for i,num in enumerate(nums):
            if target-num in res:
                return res[target-num],i+1
            res[num]=i+1
```

```c++
class Solution {
public:
    /*
     * @param nums: an array of Integer
     * @param target: target = nums[index1] + nums[index2]
     * @return: [index1 + 1, index2 + 1] (index1 < index2)
     */
    vector<int> twoSum(vector<int> &nums, int target) {
        // write your code here
        map<int,int> hmap;
        for(int i=0;i<nums.size();++i)
        {
            if(hmap.count(target-nums[i]))
                return {hmap[target-nums[i]],i+1};
            hmap[nums[i]]=i+1;
        }
    }
};
```