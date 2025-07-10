#include <iostream>

using namespace std;

int main() {

    int arr[9] ;
    int max = 0 ;
    int maxIdx = 0 ;

    for (int i = 0; i < 9; i++) {
        cin >> arr[i] ;
    }

    for (int i = 0; i < 9; i++) {
        if (max < arr[i]) {
            max = arr[i] ;
            maxIdx = i + 1;
        }
    }

    cout << max << endl << maxIdx << endl; 

}