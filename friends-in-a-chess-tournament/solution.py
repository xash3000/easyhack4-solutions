N, A, B = map(int, input().split())

if A % 2 == B % 2:
    print((B - A) // 2)
else:
    print(min(A - 1, N - B) + 1 + (B - A - 1)//2)
