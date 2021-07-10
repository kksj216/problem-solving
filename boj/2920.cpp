#include <iostream>
using namespace std;

int main() {

    int num[8] ; 
    int count1 = 0, count2 = 0 ; 

    for (int i = 0; i < 8; i++) {
        cin >> num[i] ;
    }

    for (int i = 0; i < 8; i++) {
        if (num[i] == (i+1)) {
            count1++ ;
            continue ;
        }
        else if (num[i] == (8-i)) {
            count2++ ;
            continue ;
        }
        else {
            break ; 
        }
    }

    if (count1 == 8) {
        cout << "ascending\n";
    }
    else if (count2 == 8) {
        cout << "descending\n";
    }
    else {
        cout << "mixed\n" ;
    }

}
