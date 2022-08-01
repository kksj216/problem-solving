/* 
위장 https://school.programmers.co.kr/learn/courses/30/lessons/42578 
*/ 
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1; 
    
    map<string, int> mm;
    
    for (int i = 0 ;i < clothes.size(); i++) {
        mm[clothes[i][1]]++;
    }
    
    for (auto& iter : mm) {
        answer *= (iter.second+1);
    }  
    
    return answer-1;
}

/*
// failed with testcase 16 

bool cmp(vector<string> &v1, vector<string> &v2){
  if(v1[1] == v2[1])
    return v1[0]<v2[0];
  else return v1[1]<v2[1];
}

int solution(vector<vector<string>> clothes) {
    int answer = 1; 
    int count = 0;
    
    sort(clothes.begin(), clothes.end(), cmp); 
    
    for (int i=1; i < clothes.size(); i++) {
        if (clothes[i][1] != clothes[i-1][1]) { 
            count++; 
            answer *= (count+1); 
            count = 0; 
        }
        else {
            count++;
        }
    }
    
    if (clothes[clothes.size()-1][1] != clothes[clothes.size()-2][1]) { 
        count = 1; 
        answer *= (count+1); 
    } else {
        count++;
        answer *= (count+1);
    }
    
    return answer-1;
}
*/