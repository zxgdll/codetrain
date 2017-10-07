#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
	int numberOfArithmeticSlices(vector <int>& A){
		int count=0;
		int dem=0;
		if (A.size()<3)
			return count;
		for (int i = 1; i < A.size()-1; i++)
		{
			if ((A[i]-A[i-1])==(A[i+1]-A[i]))
			{
				dem++;
				count+=dem;
			}
			else
				dem=0;
		}
		return count;
	}
	
};
// int main()
// {

// 	vector<int> v{1,2,3,4,5};
// 	Solution a;
// 	cout<<a.numberOfArithmeticSlices(v)<<endl;
// 	return 0;
// }