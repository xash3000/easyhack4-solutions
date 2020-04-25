#include <iostream>
using namespace std;bool m[100001];
int main() {m[0]=m[1]=1;for(int i=2;i<=100000;i++)if(!m[i])for(int j=2;j*i<100001;j++)m[i*j]=1;int n,c=0;cin>>n;for(int i=1;i<=n;i++){int x;cin >>x;if(!(m[i]||m[x]))c++;}cout<<c;}
