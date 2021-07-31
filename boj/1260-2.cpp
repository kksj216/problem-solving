/*
 BOJ 1260 
 DFS, BFS
 */

#include <iostream>
#include <queue>
#include <algorithm>
#include <stack>
#include <vector>
using namespace std;


void dfs(int start, vector<int> graph[], bool check[]) {

    stack <int> stk;

    stk.push(start) ; 
    check[start] = true ; 
    cout << start << " ";

    while (!stk.empty()) {

        int a = stk.top();
        stk.pop();

        for (int i = 0 ; i < graph[a].size(); i++) {
            if (check[graph[a].at(i)] == false) {
                cout << graph[a].at(i) << " ";
                check[graph[a].at(i)] = true;
                stk.push(a) ; // push current 
                stk.push(graph[a].at(i)) ;
                break;
            }
        }
    }


}

void bfs(int start, vector<int> graph[], bool check[]) {

    queue <int> que ; 

    que.push(start) ;
    check[start] = true ; 

    while (!que.empty()) {

        int a = que.front() ;
        que.pop(); 
        cout << a << " ";

        for (int i = 0; i < graph[a].size(); i++) {
            if (check[graph[a].at(i)] == false) { 
                check[graph[a].at(i)] = true ; 
                que.push(graph[a].at(i)) ;
            }
        }
    }


}

int main() {

    int N, M, start ; 
    int first, second; 

    cin >> N >> M >> start ;

    vector<int> graph[N+1] ;
    bool check[N+1] ;

    fill(check, check+N+1, false) ;
    
    for (int i = 0; i < M ;i++) {
        cin >> first >> second ;
        graph[first].push_back(second);
        graph[second].push_back(first);
    }

    for (int i = 0; i <= N; i++) {
        sort(graph[i].begin(), graph[i].end()) ;
    }

    dfs(start, graph, check) ; 
    cout << endl ;

    fill(check, check+N+1, false) ;

    bfs(start, graph, check) ;

}
