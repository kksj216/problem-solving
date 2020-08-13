/*
 BOJ 1260 
 DFS, BFS
 */

#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> vec[10001];
int visits[10001] ={0};

void dfs(int start) {
    
    if (!visits[start]) {
        cout << start << " ";
        visits[start] = 1;
    }

    for (int i=0;i<vec[start].size();i++) {
        if (visits[vec[start].at(i)] == 0) {
            dfs(vec[start].at(i));
        }
    }

}

void bfs(int n, int start) {
    bool visit[n+1];
    queue<int> que;

    for (int i=0;i<n+1;i++) {
        visit[i] = false;
    }

    que.push(start);
    
    while (!que.empty()) {
        int a = que.front();
        visit[a] = true;
        cout << a << " ";
        que.pop();

        for (int i=0;i<vec[a].size();i++) {
            if (!visit[vec[a].at(i)]) {
                que.push(vec[a].at(i));
                visit[vec[a].at(i)] = true;
            }
        }
    }
}

int main() {
    int N, M, V, a, b;

    cin >> N >> M >> V;

    while (M--) {
        cin >> a >> b;
        vec[a].push_back(b);
        vec[b].push_back(a);
        
    }
    for (int i=0;i<N;i++) {
        sort(vec[i].begin(), vec[i].end());
    }

    dfs(V);
    cout << endl;
    bfs(N, V);

}
