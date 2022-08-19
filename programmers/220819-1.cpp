"""
올바른 괄호 
https://school.programmers.co.kr/learn/courses/30/lessons/12909
"""

#include<string>
#include <iostream>
#include <vector>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    vector<char> vec;

    if (s.at(0) == ')') return false; 
    
    for (int i = 0; i < s.length(); i++) {
        if (s.at(i) == '(') vec.push_back('(');
        else {
            if (!vec.empty()) vec.pop_back();  
            else if (vec.empty()) return false;
        }   
    }
    
    if (!vec.empty()) answer = false; 

    return answer;
}