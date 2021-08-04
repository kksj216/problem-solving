#include <iostream>

using namespace std;

int main() {

    int N;
    cin >> N;

    int A[N], B[N];

    for (int i = 0; i < N;i++) {
        cin >> A[i] >>B[i];

    }

    for (int i = 0; i < N; i++) {
        cout << "Case #" << i+1 << ": " << A[i] << " + " << B[i] << " = " << A[i]+B[i] << "\n";
    }

}