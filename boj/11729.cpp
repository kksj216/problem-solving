#include <iostream>
#include <string>

using namespace std;

int main() {

    string input ;
    int len ;
    cin >> len;
    cin >> input ;

    int sum = 0;

    for (int i=0; i < len; i++) {
        int n = input[i]-48;
        sum += n;
    }
    cout << sum << endl ;

}