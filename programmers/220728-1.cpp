"""
전화번호 목록 https://school.programmers.co.kr/learn/courses/30/lessons/42577
"""
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    
    sort(phone_book.begin(), phone_book.end());
    
    int i = 0; 
    while (i != phone_book.size()-1) { 
        if (phone_book[i+1].find(phone_book[i]) == 0) { 
            answer = false;
            break;
        } 
        if (answer == false) break; 
        
        i++;
    }
    
    return answer;
}

"""
// This solution is failed with efficiency test 4. 
bool solution(vector<string> phone_book) {
    bool answer = true;
    vector <pair<int, string> > phoneWithLenOfNum; 
    
    for (int i = 0; i < phone_book.size(); i++) {
        phoneWithLenOfNum.push_back(make_pair(phone_book[i].length(), phone_book[i]));
    }
    sort(phoneWithLenOfNum.begin(), phoneWithLenOfNum.end()); 
    
    int i = 0 ;
    
    while(i != phoneWithLenOfNum.size()) {
        bool flag = false; 
        
        for (int j = phoneWithLenOfNum.size()-1; j > i; j--) {
            if (phoneWithLenOfNum[j].second.find(phoneWithLenOfNum[i].second) == 0) {
                answer = false ; 
                break;
            }
        }
        if (answer == false) break;
        
        for (int k = i; k < phoneWithLenOfNum.size(); k++) {
            if (phoneWithLenOfNum[i].first != phoneWithLenOfNum[k].first) {
                flag = true; 
                break;
            }
        }
        if (flag == false) break;
        // if (flag == true) continue; 
         
        i++;
    }
    
    return answer;
}
"""