#include <iostream>
using namespace std;

int main() {
    int N; 
    float M = 0;

    cin >> N;

    float numbers[N];
    float newNums[N];
    float avg;
    
    for (int i=0;i<N;i++) {
        cin >> numbers[i];
    }
    // find value of M
    for (int i=0;i<N;i++) {
        if (M < numbers[i]) {
            M = numbers[i];
        }
    }
    // cout << M << endl;
    // compute new value of score
    for (int i=0;i<N;i++) {
        newNums[i] = numbers[i]/M*100;
        //cout << i << " new score: " << newNums[i] << endl;
    }
    // for (int i=0;i<N;i++) {
    //     cout << i << ": " << newNums[i] << endl;
    // }

    for (int i=0;i<N;i++) {
        avg += newNums[i];
    }
    //cout << "avg: " << avg << endl;
    avg = avg/N;

    cout << avg << endl;


}