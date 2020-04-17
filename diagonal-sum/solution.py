def solve(mat, n):
    sols = []

    i, j = 0, n - 1

    while j >= 0:
        ci, cj = i, j

        summ = 0
        while cj <= n - 1:
            summ += mat[ci][cj]
            ci += 1
            cj += 1

        sols.append(summ)
        j -= 1


    i, j = 1, 0

    while i <= n - 1:
        ci, cj = i, j

        summ = 0
        while ci <= n - 1:
            summ += mat[ci][cj]
            ci += 1
            cj += 1

        sols.append(summ)
        i += 1
    return sols

if __name__ == "__main__":
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    print(solve(mat, n))


