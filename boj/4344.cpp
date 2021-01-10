#include <iostream>
using namespace std;

/** 
 * 2021.01.10
 * boj 4344
*/
int main() {
    int C;

    cin >> C;
    int studentsN[C];
    int scores[C][1000];
    float avgs[C];
    int overAvgNum[C];
    float result[C];
    
    for (int i=0;i<C;i++) {
        cin >> studentsN[i];
        
        for (int j=0;j<studentsN[i];j++) {  
            cin >> scores[i][j];
            avgs[i] = avgs[i] + scores[i][j];
        }
        avgs[i] = avgs[i]/studentsN[i];
    }

    for (int i=0;i<C;i++) { 
        overAvgNum[i] = 0;
        for (int j=0;j<studentsN[i];j++) {  
            if (scores[i][j] > avgs[i]) {
                overAvgNum[i] += 1;
            }
        }
        result[i] = (float)overAvgNum[i]/studentsN[i]*100;

    }
    for (int i=0;i<C;i++) {
        cout.setf(ios::fixed);
        cout.precision(3);
        cout << result[i] << "%" << endl;
    }

}