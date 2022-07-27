"""
완주하지 못한 선수 https://school.programmers.co.kr/learn/courses/30/lessons/42576
"""
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    
    sort(completion.begin(), completion.end());
    sort(participant.begin(), participant.end());
    
    for (int i = 0 ; i < participant.size(); i++) {
        if (participant[i] != completion[i]) {
            answer = participant[i] ;
            break;
        }
    }
    
    
    return answer;
}