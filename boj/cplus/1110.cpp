#include <iostream>

using namespace std;

int main() {

    int number, newTemp ,newNum = 100;
    int testNum ;
    int count = 0; 
    
    cin >> number;
    testNum = number;

    while (number != newNum) {

        if (testNum < 10) {
            newTemp = testNum ;
            newNum = testNum*10 + newTemp;
        }
        else {
            int ten = testNum / 10 ;
            int one = testNum-(10*ten);
            
            newTemp = ten + one ;
            int newTempOne = newTemp - (10*(newTemp/10)) ;
            newNum = one*10 + newTempOne ;
        }
        testNum = newNum ;

        count++;
        
    }

    cout << count;


}