#include <iostream>
#include <vector>
using namespace std;
/*
三种思路，
第一：首尾交换 （实例）
第二：倒序输出
第三：回文输出
*/
// class Solution
// {
// public:
// 	string reverseString(string s){
// 		int a=s.size()-1;
// 		int i=0;
// 		while(i<a)
// 		{
// 			swap(s[i],s[a]);
// 			i++;
// 			a--;
// 		}
// 		return s;
// 	}
// };
class Solution
{
public:
	string reverseString(string s){
		string str(s.rbegin(),s.rend());
		return str;
	}
	
};
int main()
{
	Solution a;
	string b;
	b=a.reverseString("hello");
	cout<<b;
	return 0;
}