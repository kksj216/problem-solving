#include <iostream>
#include <queue>
using namespace std;

int bfs(int size, int startX, int startY, int finalX, int finalY) {

    int arrayX[8] = {1, 2, 2, 1, -1, -2, -2, -1};
    int arrayY[8] = {2, 1, -1, -2, -2, -1, 1, 2};
    int visit[size][size]; // 0: 미방문, 1: 방문
    int count[size][size]; // 
    queue <pair<int, int>> que;

    for (int i=0;i<size;i++) {
        for (int j=0;j<size;j++) {
            visit[i][j] = 0;
            count[i][j] =-1;
        }
    }

    que.push(make_pair(startX, startY));
    count[startX][startY] = 0;

    while (!que.empty()) {
        int a = que.front().first;
        int b = que.front().second;
        visit[a][b] = 1;

        que.pop();

        for (int i=0;i<8;i++) {
            if (a+arrayX[i] >= 0 && a+arrayX[i] < size && b+arrayY[i] >= 0 && b+arrayY[i] < size) {
                if (visit[a+arrayX[i]][b+arrayY[i]] == 0) { 
                    
                    que.push(make_pair(a+arrayX[i], b+arrayY[i])); 
                    count[a+arrayX[i]][b+arrayY[i]] = count[a][b] + 1;
                    visit[a+arrayX[i]][b+arrayY[i]] = 1;

                    if (a+arrayX[i] == finalX && b+arrayY[i] == finalY) {
                       return count[a+arrayX[i]][b+arrayY[i]];
                    }
                }
            }
        }

    }
    return 0;
    
}

int main() {

    int NUM, count, i=0;
    int size, startX, startY, finalX, finalY;

    cin >> NUM;
    int answer[NUM];

    while (NUM--) {
        cin >> size >> startX >> startY >> finalX >> finalY;

        count = bfs(size, startX, startY, finalX, finalY);
        
        answer[i++] = count;

    }

    for (int j=0;j<i;j++) {
        cout << answer[j] << endl;
    }

    return 0;
}

