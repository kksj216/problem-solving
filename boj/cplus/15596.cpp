#include <iostream>
#include <vector>

using namespace std;

long long sum(vector<int> &a);

int main() {

    vector<int> a ;

    for (int i = 0; i < 10 ;i++ ) {
        a.push_back(i+1); 
    }

    sum(a);



}

// 이 함수부분 
long long sum(std::vector<int> &a) {

    long long sum = 0;

    for (int i = 0; i < a.size(); i++) {
        sum += a.at(i);
        // cout << sum << endl;
    }
    // cout << "sum: " << sum << endl;

    return sum;

}