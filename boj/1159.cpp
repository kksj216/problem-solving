#include <iostream>
#include <string>
using namespace std;

int main() {
    int N=0 ;
    int alpa[26] ;
    int alpaResult[26] ;
    char result[26] ;
    int check = 0;

    cin >> N ;

    string names[N];
    int sungs[N];

    for (int j = 0; j < 26; j++) { 
        alpa[j] = j+97;
        alpaResult[j] = 0;
    } 

    for (int i = 0; i < N; i++) {
        cin >> names[i] ; 
        sungs[i] = names[i][0] ;
    }

    for (int i = 0; i < N; i++) {
        for (int k = 0; k < 26; k++) { 
            if (sungs[i] == alpa[k]) {
                alpaResult[k] += 1;
            }
        }
    }

    for (int k = 0; k < 26; k++) {
        if (alpaResult[k] >= 5) {
            check += 1;
        }
    }

    if (check <= 0) {
        cout << "PREDAJA" ;
        return 0 ;
    }
    else {
        for (int k = 0; k < 26; k++) {
            if (alpaResult[k] >= 5) {
                cout << char(k+97) ;
            }
        }
    }
    


}
