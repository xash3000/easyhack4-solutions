#include <bits/stdc++.h>

using namespace std;

int main(){
    long long N, A, B, ans;
    cin >> N >> A >> B;

    if(A % 2 == B % 2){
        ans = (B - A) / 2;
    }else{
        ans = min(A - 1, N - B) + 1 + (B - A - 1) / 2;
    }
    
    cout << ans;
}
