def magicSquare(n):
    data = [[0] * n for i in range(n)]
    i = 0
    j = n // 2
    for k in range(1, n * n + 1):
        data[i][j] = k
        if k % n == 0:
            i += 1
        else:
            i -= 1
            if i < 0:
                i = n - 1
            j += 1
            if j == n:
                j = 0
    for i in range(n):
        for j in range(n):
            print("{0:3d} ".format(data[i][j]), end = "")
        print()

if __name__ == "__main__":
    n = int(input("숫자 : "));
    magicSquare(n)
