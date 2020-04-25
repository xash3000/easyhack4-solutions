#include <bits/stdc++.h>

using namespace std;

int main(){
    long long N, A, B, rem, ans;
    cin >> N >> A >> B;
    ans = N / (A+B) * A;
    rem = N % (A + B);
    ans += min(rem, A);
    cout << ans;
}
