def f(n , x):
    i = 0
    while(n % x == 0):
        i += 1
        n  =n / x
    return n,i
        
  
lm  =  {2:0 , 3:0 , 5:0}
ln  =  {2:0 , 3:0 , 5:0}
n,m = [int(x) for x in raw_input().split()]

n,ln[2] = f(n,2)
#print(ln[2])
n,ln[3] = f(n,3)
n,ln[5] = f(n,5)

m,lm[2] = f(m,2)
m,lm[3] = f(m,3)
m,lm[5] = f(m,5)

if(m != n):
    print(-1)
else:
    print(abs(ln[2] - lm[2]) + abs(ln[3] - lm[3]) + abs(ln[5] - lm[5]))
