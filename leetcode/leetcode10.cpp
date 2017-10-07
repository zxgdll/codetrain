/* 解题思路：
需要用递归Recursion来解，大概思路如下：

- 若p为空，若s也为空，返回true，反之返回false

- 若p的长度为1，若s长度也为1，且相同或是p为'.'则返回true，反之返回false

- 若p的第二个字符不为*，若此时s为空返回false，否则判断首字符是否匹配，且从各自的第二个字符开始调用递归函数匹配

- 若p的第二个字符为*，若s不为空且字符匹配，调用递归函数匹配s和去掉前两个字符的p，若匹配返回true，否则s去掉首字母

- 返回调用递归函数匹配s和去掉前两个字符的p的结果
*/
class Solution{
public:
	bool isMatch(string s,string p)
	{
		if (p.empty())
			return s.empty();
		if(p.size()==1){
			return (s.size()==1&&(s[0]==p[0]||p[0]=='.'));
		}
		if (p[1]!='*')
		{
			if(s.empty()) return false;
			return (s[0]==p[0]||p[0]=='.')&&isMatch(s.substr(1),p.substr(1));
		}
		while(!s.empty()&&(s[0]==p[0]||p[0]=='.'))
		{
			if(isMatch(s,p.substr(2))) return true;
			s=s.substr(1);
		}
		return isMatch(s,p.substr(2));
	}
};