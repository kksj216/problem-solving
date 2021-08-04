#include <iostream>

using namespace std;

int main() {

    int N, X, num, count = 0;

    cin >> N>> X;
    int re[N];

    for (int i = 0; i< N; i++) {
        cin >> num ;
        if (num < X) {
            re[count++] = num;
        }
    }

    for (int i = 0 ; i < count ; i++) {
        cout << re[i] << " ";
    }

}