#include <iostream>

using namespace std;

int main() {

    int result[500] ;
    int A, B, count=0, i = 0 ;

    while (1) {
        cin >> A;
        cin >> B;

        if (A == 0 && B == 0) {
            break ;
        }
        result[count++] = A + B;
    } 

    while (count > 0) {
        cout << result[i++] << endl ; 
        count--;
    }

}