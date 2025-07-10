/**
 * 2667번 
 * 단지번호 붙이기
 * Graph - DFS/BFS
 * */
#include <iostream> 
#include <stdio.h>
#include <queue>
#include <algorithm>
#include<string>

using namespace std;

int main() {

    int arrayX[4] = {0, 1, 0, -1};
    int arrayY[4] = {1, 0, -1, 0};
    queue <pair<int, int> > que; 
    // int first, second ;
    int result[100000] = {0};
    int count = 0;

    int size ;

    cin >> size ;

    int arr[size][size] ;
    string input[size] ;
    int visit[size][size]; // 0: 미방문, 1: 방문

    for (int i = 0; i < size; i++) {
        cin >> input[i] ;
    }

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < input[i].size(); j++) {
            arr[i][j] = input[i][j] - '0';
        }
    }

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            visit[i][j] = 0;
        }
    }

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (visit[i][j] == 0 && arr[i][j] == 1) {
                result[count] += 1;
                que.push(make_pair(i, j));

                while (!que.empty()) {
                    int first = que.front().first;
                    int second = que.front().second;
                    visit[first][second] = 1;

                    que.pop() ;

                    for (int k = 0; k < 4; k++) {
                        if (visit[arrayX[k]+first][arrayY[k]+second] == 0 && arr[arrayX[k]+first][arrayY[k]+second] == 1) { 
                            if (arrayX[k]+first >= 0 && arrayY[k]+second >= 0 && arrayX[k]+first < size && arrayY[k]+second < size) { // 범위 설정
                                visit[arrayX[k]+first][arrayY[k]+second] = 1 ;
                                result[count] += 1;
                                que.push(make_pair(arrayX[k]+first, arrayY[k]+second)) ;
                            }
                        }
                    }
                }
                count++;
            }
        }
    }

    cout << count << endl ;
    sort(result, result+count) ;

    for (int i = 0; i < count-1; i++) {
        cout << result[i] << endl ;
    }
    cout << result[count-1] ;

}
