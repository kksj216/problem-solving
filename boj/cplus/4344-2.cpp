#include <iostream>

using namespace std;

int main() {

    int n ;
    cin >> n;

    int std[n] ; 
    int result[n];
    float avg[n];
    float re[n];


    for (int j = 0; j < n; j++) {
        avg[j] = 0.0;
        cin >> std[j] ;
        
        float temp[std[j]];
        float totalNum = std[j];
        float overNum=0;

        for (int i = 0; i < std[j]; i++) {
            cin >> temp[i];
            avg[j] += temp[i];
        }
        avg[j] = avg[j]/std[j];

        for (int i = 0; i < std[j]; i++) {
            if (avg[j] < temp[i]) {
                overNum++;
            }
        }
        
        re[j] = float(overNum / totalNum) * 100.0;
        
    }

    for (int i = 0; i < n ;i++) {
        cout << fixed ;
        cout.precision(3);
        cout << re[i] << "%" << endl;
    }

}