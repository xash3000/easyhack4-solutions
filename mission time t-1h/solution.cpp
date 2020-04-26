#include <bits/stdc++.h>
using namespace std;
    
int main()
{
    int test;
    scanf("%d", &test);
    assert(test>=1 && test<=20);
    while(test-->0) {
        int N, G;
        cin >> N >> G;
        assert(N >= 1 && N <= 100);
        assert(G >= 0 && G <= 1e6);
        vector <int> tm(N);
        int sum = 0;
        for(int i = 0; i < (int)N; ++i) {
            cin >> tm[i];
            assert(tm[i] >= 0 && tm[i] <= 100);
            sum += tm[i];
        }
        vector <bool> sumPossible((int)1e4+1, false);
        sumPossible[0] = true;
    
        for(auto it = (tm).begin(); it != (tm).end(); ++it) {
            for(int t = (int)1e4; t >= (int)0; --t) {
                if(t - *it >= 0 && sumPossible[t - *it] == true) {
                    sumPossible[t] = true;
                }
            }
        }
        bool flag = false;
        for(int i = 0; i <= (int)sum; ++i) {
            if(sumPossible[i] && i <= G && sum - i <= G) {
                flag = true;
            }
        }
        cout << (flag ? "YES" : "NO") << "\n";
    }
    
    return 0;
}