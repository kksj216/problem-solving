#include <iostream>
using namespace std;

int main() {

    int a; 

    cin >> a;

    int nums[a] ;
    int min = 1000000;
    int max = -1000000;
    
    for (int i = 0; i < a; i++) {
        cin >> nums[i] ;
    }

    for (int i = 0;i < a; i++) {
        if (min >= nums[i]) {
            min = nums[i] ;
        }
        if (max <= nums[i]) {
            max = nums[i] ;
        }
    }

    cout << min << " " << max << endl;
    
}