#include <iostream>

using namespace std;


int main() {

    string input;
    int result = 0;

    cin >> input ;

    for (int i = 0; i < input.length(); i++) {
        if (input[i] >= 65 && input[i] <= 67) {
            result += 3 ;
        } else if (input[i] >= 68 && input[i] <= 70) {
            result += 4 ;
        } else if (input[i] >= 71 && input[i] <= 73) {
            result += 5 ;
        } else if (input[i] >= 74 && input[i] <= 76) {
            result += 6 ;
        } else if (input[i] >= 77 && input[i] <= 79) {
            result += 7 ;
        } else if (input[i] >= 80 && input[i] <= 83) {
            result += 8 ;
        } else if (input[i] >= 84 && input[i] <= 86) {
            result += 9 ;
        } else if (input[i] >= 87 && input[i] <= 90) {
            result += 10 ;
        } 
    }

    cout << result ;



}
