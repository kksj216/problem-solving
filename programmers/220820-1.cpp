"""
프린터 
https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=cpp#
"""
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    vector<pair<int, int>> prioritiesIdx;
    
    for (int i = 0 ; i < priorities.size(); i++) {
        prioritiesIdx.push_back(make_pair(i, priorities[i]));
    }
    
    int count = 0;
    int i = 0;
    while (1) { 
        count = 0;
        int ts = prioritiesIdx.size() ;
        for (int j = i+1; j < ts; j++) {
            if (prioritiesIdx[i].second < prioritiesIdx[j].second) {
                int temp1 = prioritiesIdx[i].first;
                int temp2 = prioritiesIdx[i].second;
                prioritiesIdx.erase(prioritiesIdx.begin());
                prioritiesIdx.push_back(make_pair(temp1, temp2));
                
                break;   
            }
            else count++;
        }
        if (count == ts-1) {
            if (prioritiesIdx[i].first == location) {
                answer += 1;
                break;
            }
            prioritiesIdx.erase(prioritiesIdx.begin() );
            answer += 1;
        }
    } 
    
    return answer;
}
