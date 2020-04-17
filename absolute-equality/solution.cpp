#include <bits/stdc++.h>

using namespace std;

int main(){
    long long a, b;
    cin >> a >> b;

    if(a % 2 != b % 2){
        cout << "IMPOSSIBLE";
    }else{
        cout << int((a + b) / 2);
    }
}
