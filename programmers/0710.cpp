/**
 *  programmers: skill tree
 *  2021-07-10 
 */
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0, count = 0;
    string check;
    vector<string> skills;

    for (int i = 0;i < skill_trees.size(); i++) {
        for (int j = 0; j < skill_trees.at(i).size(); j++) {

            for (int k = 0; k < skill.size(); k++) {
                if (skill_trees.at(i)[j] == skill[k]) {
                    check += skill[k] ;
                }
            }
        }
        skills.push_back(check);
        check = "" ;
    }

    for (int i = 0; i < skills.size(); i++) {
        // cout << skills.at(i) << endl ;
        for (int j = 0; j < skills.at(i).size(); j++) {
            for (int k = 0; k < skill.size(); k++) {
                if (skills.at(i)[j] == skill[k] && (k<=j)) {
                    count ++;
                    break ;
                }
            }
        }
        if (count == skills.at(i).size()) {
            answer++;
        }
        count = 0;
    }

    cout << answer ;

    return answer;
}