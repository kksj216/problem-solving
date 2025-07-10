#include <iostream>

using namespace std;

int main() {
    int n, A, B ;

    cin >> n ;

    int result[n];

    for (int i = 0; i < n; i++) {
        cin >> A >> B; 

        result[i] = A + B ;
    }

    for (int i = 0; i < n; i++) {
        cout << result[i] << endl;
    }


}