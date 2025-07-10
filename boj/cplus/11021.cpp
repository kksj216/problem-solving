#include <iostream>

using namespace std;

int main() {

    int N, A, B;
    cin >> N;

    int re[N];

    for (int i = 0; i < N;i++) {
        cin >> A >>B;

        re[i] = A+B;
    }

    for (int i = 0; i < N; i++) {
        cout << "Case #" << i+1 << ": " << re[i] << "\n";
    }

}