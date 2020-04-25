#include <bits/stdc++.h>

using namespace std;

int main(){

    int n;
    cin >> n;

    int mat[101][101];

    for(int i=0; i < n; i++){
        for(int j=0; j < n; j++){
            cin >> mat[i][j];
        }
    }

    int i = 0, j = n - 1;

    while(j >= 0){
        int ci = i, cj = j;

        int summ = 0;

        while(cj <= n - 1){
            summ += mat[ci][cj];
            ci += 1;
            cj += 1;
        }

        cout << summ << endl;
        j -= 1;
    }

    i = 1, j = 0;

    while(i <= n - 1){
        int ci = i, cj = j;

        int summ = 0;
        while(ci <= n - 1){
            summ += mat[ci][cj];
            ci += 1;
            cj += 1;
        }

        cout << summ << endl;
        i += 1;
    }
}
