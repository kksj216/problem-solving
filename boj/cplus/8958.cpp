#include <iostream>
#include <string.h>
using namespace std;

/** 
 * 2021.01.09
 * boj 8958 
*/
int main() {
    int N;

    cin >> N;
    char quizs[N][80];
    int score[N][80];
    int total = 0;
    int totalArr[N];

    for (int i=0;i<N;i++) {
        cin >> quizs[i];
    }
    
    for (int i=0;i<N;i++) {
        total = 0;
        // cout << quizs[i] << " " << strlen(quizs[i]) << "  ";
        for (int j=0;j<strlen(quizs[i]);j++) {
            // cout << quizs[i][j] << " ";
            if (quizs[i][j] == 'O') {
                if (j == 0) {
                    score[i][j] = 1;
                }
                else {
                    score[i][j] = score[i][j-1] + 1;
                }
            }
            else if (quizs[i][j] == 'X') {
                score[i][j] = 0;
            }
            total = total + score[i][j];
        }  
        totalArr[i] = total; 
    }
    
    for (int i=0;i<N;i++) {
        cout << totalArr[i] << endl;
    }

}