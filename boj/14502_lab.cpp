#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int Lmap[9][9] = {0};

int bfs(int N, int M, vector<pair<int, int>> wall) {
    int count=0;
    int new_map[N][M];
    bool visit[N][M];

    int arrayX[4] = {0, 1, 0, -1};
    int arrayY[4] = {1, 0, -1, 0};

    queue<pair<int, int>> que;

    // map을 복사한다. + 2가 있으면 큐에 넣는다.(for BFS)
    for (int i=0;i<N;i++) {
        for (int j=0;j<M;j++) {
            new_map[i][j] = Lmap[i][j];
            visit[i][j] = false;

            if (new_map[i][j] == 2) {
                que.push(make_pair(i, j)); 
                visit[i][j] = true;
            }
        }
    }
    // 벽을 3개 세운다. 
    for (int i=0;i<wall.size();i++) {
        new_map[wall[i].first][wall[i].second] = 1;
    }

    // bfs를 통해 2가 있으면 퍼뜨린다. 
    while (!que.empty()) {

        int x = que.front().first;
        int y = que.front().second;

        for (int i=0;i<4;i++) {
            // 좌표안에 있고, 
            if (x+arrayX[i] >= 0 && x+arrayX[i] < N && y+arrayY[i] >= 0 && y+arrayY[i] < M) {
                // 0이라면, 
                if (new_map[x+arrayX[i]][y+arrayY[i]] == 0 && visit[x+arrayX[i]][y+arrayY[i]] == false) {
                    new_map[x+arrayX[i]][y+arrayY[i]] = 2; // 바이러스를 퍼뜨린다. 
                    que.push(make_pair(x+arrayX[i], y+arrayY[i])); // que에 넣는다.
                    visit[x+arrayX[i]][y+arrayY[i]] = true; // 방문표시한다.
                }

            }

        }
        que.pop();

    }

    // 0이 몇개인지 센다.
    for (int i=0;i<N;i++) {
        for (int j=0;j<M;j++) {
            if (new_map[i][j] == 0) count++;
        }
    }

    return count;

}

int main() {
    int N, M;
    int max = 0, count;

    cin >> N >> M;

    for (int i=0;i<N;i++) {
        for (int j=0;j<M;j++) {
            cin >> Lmap[i][j]; 
        }
    }

    vector<pair<int, int>> zero; // 값이 0인 좌표를 저장한다. 

    for (int i=0;i<N;i++) {
        for (int j=0;j<M;j++) {
            if (Lmap[i][j] == 0) {
                zero.push_back(make_pair(i, j));
            }
        }
    }

    vector<pair<int, int>> wall; // 0인 좌표들 중 벽세울 세개 골라서 넣는다.  

    for (int i=0;i<zero.size();i++) {
        for (int j=i+1;j<zero.size();j++) {
            for (int k=j+1;k<zero.size();k++) {
                wall.push_back(zero[i]);
                wall.push_back(zero[j]);
                wall.push_back(zero[k]);
                
                count = bfs(N, M, wall);
                
                if (max < count) max = count;

                wall.pop_back();
                wall.pop_back();
                wall.pop_back();
            }
        }
    }

    cout << max;

}
