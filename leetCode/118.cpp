
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> a;
        
        for (int i = 1; i <= numRows; i++) {
            vector<int> b;
            if (i == 1) {
                b.push_back(1);
                a.push_back(b);
            }
            else {
                b.push_back(1);
                if (i >= 3) {
                    for (int k = 1; k < i-1; k++) {
                        // cout << a.at(i-2).at(k-1) << " ::: " << a.at(i-2).at(k) << endl ;
                        int n = a.at(i-2).at(k-1) + a.at(i-2).at(k);
                        b.push_back(n);
                    }
                }
                b.push_back(1);
                a.push_back(b); 
                
            }
            
        }
        
        return a;
    }
};