a, b = map(int, input().split())

if a % 2 != b % 2:
    print("IMPOSSIBLE")
else:
    print(a + b) // 2
