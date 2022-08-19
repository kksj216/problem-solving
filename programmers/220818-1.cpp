"""
같은 숫자는 싫어 
https://school.programmers.co.kr/learn/courses/30/lessons/12906
"""
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    int size = arr.size();
    int i = 1; 
    
    answer.push_back(arr[0]);
    
    while (i < size) {
        if (answer.back() != arr[i]) {
            answer.push_back(arr[i]) ;
        }
        i++;
    }

    return answer;
}