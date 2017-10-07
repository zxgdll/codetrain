#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
	vector<string> fizzBuzz(int n){
		std::vector<string> v;
		for (int i = 1; i <= n; i++)
		{
			/* code */
			if (i%3==0 && i%5==0)
				v.push_back("FizzBuzz");
			else if (i%3==0)
			{
				v.push_back("Fizz");
			}
				else if (i%5==0)
				{
					/* code */
					v.push_back("Buzz");
				}
					else
						v.push_back(to_string(i));
		}
		return v;
	}
};
int main()
{
	Solution a;
	vector<string> b;
	b=a.fizzBuzz(15);
	for (int i = 0; i < b.size(); ++i)
	{
		/* code */
		cout<<b[i];
	}	
	return 0;
}