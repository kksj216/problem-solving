#include <iostream>
#include <vector> 

using namespace std;

int main() {

    string input;
    int alph[26];
    // vector<int> alph;
    int max = 0, check = 0;
    int result ;

    cin >> input ;

    for (int i = 0; i < 26; i++) {
        alph[i] = 0;
    }

    for (int i = 0; i < input.length(); i++) {
        // cout << input[i]<< endl;

        for (int j = 0; j < 26; j++) {
            if (input[i] == j+65 || input[i] == j+97) {
                alph[j] += 1 ; 
            }
        }
    }

    for (int i = 0; i < 26; i++) {
        // cout << i << ": " << alph[i] << endl ; 
        if (alph[i] > max) {
            max = alph[i];
            result = i;
        }
    }

    for (int i = 0; i < 26; i++) { 
        if (alph[i] == max) {
            check++ ;
        }
    }

    if (check > 1) {
        cout << "?";
    }
    else if (check == 1 ) {
        cout << char(result+65);
    }


}

