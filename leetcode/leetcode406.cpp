#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<pair<int, int> > reconstructQueue(vector<pair<int, int> >& people) {
        sort(people.begin(), people.end(),[](pair<int,int> p1,pair<int ,int> p2){
        	return p1.first>p2.first||(p1.first==p2.first&& p1.second<p2.second);
        });
        vector<pair<int,int> > v;
        for (auto person : people)
        {
        	v.insert(v.begin()+person.second,person);
        }
    return v;
    }
};
// int main()
// {
// 	Solution a;
// 	vector<pair<int,int> > v,b;
// 	v=[[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]];
// 	b=a.reconstructQueue(v);
// 	for (int i = 0; i < v.size(); ++i)
// 	{
// 		cout<<b[i].first<<b[i].second<<endl;
// 	}
// }