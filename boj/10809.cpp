#include <iostream>

using namespace std;

int main() {

    int alp[26];
    string input;

    cin >> input; 

    for (int i = 0; i < 26; i++) {
        alp[i] = -1;
    } 

    for (int i = input.length()-1; i >= 0 ; i--) { 
        for (int j = 0; j < 26; j++) {
            if (j == (int)input.at(i)-97) {
                alp[j] = i;
            }
        }
    }

    for (int i = 0 ; i < 26; i++) {
        cout << alp[i] << " ";
    }
    cout << endl;


}