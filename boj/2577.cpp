#include <iostream>
#include <cmath>

using namespace std;

int main() {

    int a, b, c ;
    int mult ;
    int num[10];
    int maxNum ;

    cin >> a ;
    cin >> b;
    cin >> c ;

    mult = a*b*c;

    for (int i = 0; i < 10; i++) {
        num[i] = 0 ;
    }

    for (int i = 9; i > 0; i--) {
        int k = int(mult / pow(10, i));
        if (k != 0) {
            maxNum = i;
            break;
        }
    }
    // cout << "max: " << maxNum << endl << "res: " << mult << endl;

    for (int i = maxNum; i >= 0; i--) {
        int n = int (mult / pow(10, i));
        // cout << " i-> " << n << endl ;
        for (int j = 0; j < 10; j++) {
            if (n == j) {
                num[j]++ ;
            }
        }
        
        int m = int(mult / pow(10,i-1));
        mult -= pow(10, i)*n;

    }

    for (int i = 0; i < 10; i++) {
        cout << num[i] << endl ;
    }

}