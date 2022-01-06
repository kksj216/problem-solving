#include <iostream>

using namespace std;

int main() {

    int input[10] ;
    int na[10] ;
    int array[42];
    int result = 0;

    int i = 0;
    while (i < 10) {
        cin >> input[i];
        i++;
    }
    i = 0;
    while (i < 42) {
        array[i] = 0;
        i++;
    }

    for (int i = 0; i < 10; i++){
        na[i] = input[i]%42 ;
        for (int j = 0; j < 42; j++) {
            if (j == na[i]) {
                array[j]++;
            }
        }
        // cout << input[i] << "   " << na[i] << endl;
    }

    i = 0;
    while (i < 42) {
        if (array[i] > 0) {
            result++ ;
        }
        i++;
    }

    cout << result << endl;

}