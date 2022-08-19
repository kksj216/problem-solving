"""
기능개발 
https://school.programmers.co.kr/learn/courses/30/lessons/42586#
"""
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int rest[progresses.size()] ;
    int count = 0;
    
    // initialize 
    for (int i = 0; i < progresses.size(); i++) {
        rest[i] = 0;
    }
    
    // count rest day 
    for (int i = 0; i < progresses.size(); i++) {
        while (progresses.at(i) < 100) {
            progresses[i] += speeds[i];
            rest[i] += 1;
        }
    }
    
    answer.push_back(1);
    int max = rest[0];
    for (int i = 1; i < progresses.size(); i++) {
        if (max < rest[i]) {
            max = rest[i] ;
            answer.push_back(1);
            count++;
        } 
        else {
            answer[count] += 1;
        }
    } 
    
    return answer;
}