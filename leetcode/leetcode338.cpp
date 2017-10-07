#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
	vector<int> countBits(int num)
	{
		std::vector<int> v;
		int num1=0;
		for (int i = 0; i < num+1; i++)
		{
			v.push_back(countsinglebits(i));
		}
		return v;
	}
private:
	int countsinglebits(int i)
	{
		int count=0;
		while(i)
		{
			count++;
			i&=(i-1);
		}
	return count;
	}
};
int main()
{
	Solution a;
	vector<int> b;
	b=a.countBits(5);
	for (int i = 0; i < b.size(); ++i)
	{
		/* code */
		cout<<b[i];
	}	
	return 0;
}