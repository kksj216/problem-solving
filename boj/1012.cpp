#include <iostream>
#include <vector>
#include <queue> 

using namespace std;

int arrayX[4] = {0, 0, -1, 1};
int arrayY[4] = {1, -1, 0, 0};

void bfs(vector<int> graph[], int garo, int sero) {

    queue <pair<int, int> > que;
    bool check[sero][garo] ;

    // initialize 
    for (int i = 0; i < sero; i++) {
        for (int j = 0; j < garo; j++) {
            check[i][j] = false ;
        }
    }

    // check all cell 
    for (int i = 0; i < sero; i++) {
        for (int j = 0; j < garo; j++) {
            if (check[i][j] == false && graph[i][j] == 1) {
                que.push(make_pair(i, j));
                
                while(!que.empty()) {
                    int first = que.front().first ;
                    int second = que.front().second ;
                    cout << "first: " << first << " / second: " << second << endl ; 
                    que.pop();

                    for (int k = 0; k < 4; k++) {
                        if (check[first+arrayY[k]][second+arrayX[k]] == false && graph[first+arrayY[k]][second+arrayX[k]] == 1) {
                            que.push(make_pair(first+arrayY[k], second+arrayX[k])) ;
                        }
                    }
                }
                
            }
        }
    }

    
    
}

int main() {

    int testCase ;
    int garo, sero, number ;
    int first, second ;

    cin >> testCase ;

    while (testCase--) {
        cin >> garo >> sero >> number ;
        // cout << garo << " " << sero << " " << number << endl;
        vector<int> graph[garo+1];
        // int graph[sero][garo] ;
        bool check[sero+1][garo+1] ;

        for (int i = 0; i < sero; i++) {
            for (int j = 0; j < garo; j++) {
                check[i][j] = false ;
                graph[i][j] = 0 ;
            }
        }
        cout << " / ?";

        while (number--) {
            cin >> first >> second ;
            // graph[first][second] = 1 ;
            graph[first].at(second) = 1;

            // graph[second][first] = 1 ;
            // graph[second][first] = 1 ;
        }
        cout << "  " <<  first << " / " << second << endl;

        bfs(graph, garo, sero) ;

    }

}
