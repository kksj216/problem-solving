"""
베스트 앨범 
https://school.programmers.co.kr/learn/courses/30/lessons/42579
"""
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    
    map<string, int> bestGenr;
    map<string, map<int, int>> ma;
    
    for (int i = 0; i < genres.size(); i++) {
        // 장르별 총 재생횟수 
        bestGenr[genres[i]] += plays[i];
        // 노래 번호와 재생횟수 추가 
        ma[genres[i]][i] = plays[i]; 
    }
    
    while (bestGenr.size() > 0) {
        string gnr;
        int max = 0; 
        // 재생횟수 가장 높은 장르 찾기 
        for (auto m: bestGenr) {
            if (max < m.second) {
                gnr = m.first; 
                max = m.second; 
            }
        }
        // 해당 장르의 가장 높은 값 두개 찾아서 answer에 넣어주고 
        // map 에서 지워주기 
        for (int i = 0 ; i < 2; i++) {
            int value = 0;
            int index = -1; 
            for (auto m: ma[gnr]) {
                if (value < m.second) {
                    value = m.second ;
                    index = m.first ;
                }
            }
            if (index == -1) break;
            answer.push_back(index);
            ma[gnr].erase(index);
        }
        bestGenr.erase(gnr);
        
    }
    
    return answer;
}