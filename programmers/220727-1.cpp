#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    vector<int> n;
    n.insert(n.begin(), nums.begin(), nums.end());
    
    unique(n.begin(),n.end()); 
    sort(n.begin(), n.end()); 
    n.erase(unique(n.begin(),n.end()),n.end()); 
    
    // for(int i=0;i<n.size();i++)
		// cout<<n[i]<<endl;
    
    if ((nums.size() / 2) <= n.size()) {
        answer = nums.size() / 2 ;
    }
    else {
        answer = n.size() ;
    }
    
    return answer;
}