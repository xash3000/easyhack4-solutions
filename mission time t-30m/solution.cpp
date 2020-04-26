#include <stdio.h>
#define MAX 100000
int is_prime[MAX+1]={0};
int num_primes[MAX+1]={0};
void seive()
{
    for(int i=3;i<=MAX;i+=2)
        is_prime[i]=1;

    for(int i=3;i*i<=MAX;i+=2)
    {
        if(is_prime[i])
        {
            for(int j=i*i;j<MAX;j+=(i<<1))
                is_prime[j]=0;
        }
    }

    is_prime[2]=1;
    num_primes[1]=0;

    for(int i=2;i<=MAX;i++)
    {
        if(is_prime[i])
            num_primes[i] = num_primes[i-1]+1;
        else
            num_primes[i] = num_primes[i-1];
    }
    return;
}
int main()
{
    seive();
    int query;
    scanf("%d",&query);
    while(query--)
    {
        int N;
        scanf("%d",&N);
        if(num_primes[N]%2==1)
            printf("Zolfa\n");
        else
            printf("MJ\n");
    }
    return 0;
}