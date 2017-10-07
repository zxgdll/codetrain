#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
	int countBattleships(vector<vector<char> >& board){
		if (board.empty())
		{
			return 0;
		}
		int rrize=board.size();
		int csize=board[0].size();
		int count=0;
		for (int i = 0; i < rrize; ++i)
		{
			for (int j = 0; j < csize; ++j)
			{
				/* code */
				if (board[i][j]=='X'&&(i==0||board[i-1][j]=='.')&&(j==0||board[i][j-1]=='.'))
				{


					count++;
				}
			}
			/* code */
		}
		return count;
	}	
};
// int main()
// {
// 	Solution a;
// 	vector<vector<char> > b={
// 		{'X','.','.','X'},
// 		{'.','.','.','X'},
// 		{'.','.','.','X'}
// 	};
// 	int b1;
// 	b1=a.countBattleships(b);
// 	cout<<b1;
// 	return 0;
// }
