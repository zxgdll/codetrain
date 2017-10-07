class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> dic(256,-1);
        int res=0,left=0;
        for (int i = 0; i!=s.length(); ++i)
        {
        	/* code */
        	if (d[s[i]]>=left)
        	{
        		left=d[s[i]]+1;
        	}
        	d[s[i]]=i;
        	res=max(res,i-left+1);
        }
        return res;
    }
};