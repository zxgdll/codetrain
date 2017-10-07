//O(n^2)复杂度，在一个数组中，找到所有满足三个数和为0的组合。
#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
	vector<vector<int>> threeSum(vector<int>& nums){
		vector<vector<int>> result;
		int i,l,r,n=nums.size();
		int s;
		sort(nums.begin(),nums.end());
		for(i=0;i<n-2;i++){
			if (i>0 && nums[i]==nums[i-1])
			{
				continue;
			}
			l=i+1;
			r=n-1;
			while(r<l){
			s=nums[i]+nums[l]+nums[r];
			if(s<0) l++;
			else if(s>0) r--;
			else{
				vector<int> tmp;
				tmp.push_back(nums[i]);
				tmp.push_back(nums[l]);
				tmp.push_back(nums[r]);
				result.push_back(tmp);
				while(l<r && nums[l]==nums[l+1]) l++;
				while(l<r && nums[r]==nums[r-1]) r--;
				l++;r--;
			}
		}
	}
		return result;
	}
};