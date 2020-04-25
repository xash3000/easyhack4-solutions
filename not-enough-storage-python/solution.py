p,n,a=lambda n: n > 1 and all(n%i for i in range(2, int(n**0.5)+1)),int(input()),list(map(int, input().split()))
print(sum((1 if(p(i+1) and p(a[i])) else 0) for i in range(n)))
