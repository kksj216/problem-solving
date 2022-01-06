#include <iostream>

using namespace std;

int main() {

    int num;

    cin >> num ;

    float array[num];
    int max = 0;
    float newArray[num];
    float sum = 0.0;
    float avg ;

    int i = 0; 
    
    while (i < num) {
        cin >> array[i];
        if (max < array[i]) {
            max = array[i] ;
        }
        i++;
    }
    // cout << "max: " << max << endl; 

    for (int i = 0; i < num; i++) {
        newArray[i] = (array[i]/max)*100.0;
        // cout << " " << newArray[i] << endl;

        sum += newArray[i] ;
    }
    avg =float(sum/num);

    cout << avg << endl;

}