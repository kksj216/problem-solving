#include <iostream>
#include <queue>
#include <vector> 

using namespace std ;

int main() {

    int computerNum = 0, connectNum = 0;
    int first, second, result = 0;
    queue<int> que;
    vector<int> vec[101];
    
    cin >> computerNum ;
    cin >> connectNum ; 

    int visitedCom[computerNum] ;

    for (int i=0;i<computerNum;i++) {
        visitedCom[i] = 0 ;
    }
    
    for (int i = 1; i <= connectNum; i++) {
        cin >> first >> second ;
        vec[first].push_back(second) ; 
        vec[second].push_back(first) ; 
    } 

    que.push(1);
    visitedCom[1] = 1;
    while (!que.empty()) {
        int num = que.front();

        for (int i = 0; i < vec[num].size(); i++) {
            if (visitedCom[vec[num].at(i)] != 1) { // if not visited 
                que.push(vec[num].at(i));
                result++;
                visitedCom[vec[num].at(i)] = 1;
            }
        }
        que.pop() ;
    }

    cout << result ;

}