#include <iostream>

using namespace std;

int main() {
    int N, K, index=2;
    int num = 0; // array[i] = 1인 것의 개수
    int count = 0; // 몇번째로 지우는 것인지 세기

    cin >> N >>  K;
    int array[N];
    int min = N;

    for (int i=0;i<N-1;i++) {
        array[i] = index++;
        if (array[i] != 1) {
            num++;
        }
    }

    // 아직 모든 수를 지우지 않았다면 즉, array[i] = 1인 것의 개수가 > 0 이라면 반복
    while (num >= 1) {
        // 가장 작은 값 P 찾기
        min = N;
        for (int i=0;i<N-1;i++) {
            if (array[i] != 1 && array[i]<min) {
                min = array[i];
            }
        }
        //cout << "min: " << min << endl;

        // min과 min의 배수 지우기(1로 바꾸기)
        for (int i=0;i<N-1;i++) {
            if (array[i] % min == 0) {
                count++;
                //cout << "count: " << count << endl;
                //cout << "array[" << i<<"]: " << array[i] << endl;
                //cout << "K: " << K << endl;
                if (count == K) {
                    cout << array[i];
                    return 0;
                }
                array[i] = 1;
                //cout << "array[" << i<<"]: " << array[i] << endl;
                
            }
        }

        // 아직 지우지 않은 (1로 바꾸지 않은) 것 몇개인지 세기
        num = 0;
        for (int i=0;i<N-1;i++) {
            if (array[i] != 1) num++;
        }

    }



    /*for (int i=0;i<N-1;i++) {
        cout << i << " " << array[i] << " ";
        cout << endl;
    }*/

}
