#include <iostream>
#include <queue>
#include <vector>
using namespace std;

string bfs(int a, int b);

int main() {
    int T, i=0;
    int start, finish;

    cin >> T;
    vector<string> results;

    while (T>0) {
        cin >> start >> finish;

        results.push_back(bfs(start, finish));

        T--;
    }

    for (int j=0;j<results.size();j++) {
        cout << results[j] << endl;
    }

}

string bfs(int a, int b) {
    queue<int> que;
    string A[10000];
    int visit[10000];
    int D=0, S=0, L=0, R=0;
    int tho, hun, ten, one;
    string answer;

    for (int z=0;z<10000;z++) {
        visit[z] = 0;
    }

    //A[a] = "";
    que.push(a);
    visit[a] = 1;
    
    while(!que.empty()) {
        int out = que.front();

        /* if (out == 1) {
            out = 0001;
        }*/
        
        if (out == b) {
            answer = A[out];
            //cout << "answer " << answer << ": " << out; 
            break;
        }

        que.pop();

        // compute D
        D = out *2;
        if (D>9999) {
            D = D % 10000;
        }

        // compute S
        S = out - 1;
        if (out == 0) {
            S = 9999;
        }

        tho = out/1000;
        hun = (out-tho*1000)/100;
        ten = (out-tho*1000-hun*100)/10;
        one = (out-tho*1000-hun*100-ten*10);
        
        // comput L
        L = hun*1000 + ten*100 + one*10 + tho;

        // compute R
        R = one*1000 + tho*100 + hun*10 + ten;

        if (visit[D] == 0)  {
            A[D] = A[out] + "D"; 
            que.push(D);
            visit[D] = 1;
            //cout << "D: " << D << endl;
        }
        
        if (visit[S] == 0) {    
            A[S] = A[out] + "S";
            que.push(S);
            visit[S] = 1;
            //cout << "S: " << S << endl;
        }

        if (visit[L] == 0) {
            A[L] = A[out] + "L";
            que.push(L);
            visit[L] = 1;
            //cout << "L: " << L << endl;
        }

        if (visit[R] == 0) {
            A[R] = A[out] + "R";
            que.push(R);
            visit[R] = 1;
            //cout << "R: " << R << endl;
        }
        
    }
    
    return answer;


}
