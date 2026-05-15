import sys

def matrixMultiplication(M1, M2):
    mod = 1000000007
    res = [[0,0],[0,0]]
    res[0][0] = (M1[0][0]*M2[0][0] + M1[0][1]*M2[1][0]) % mod
    res[0][1] = (M1[0][0]*M2[0][1] + M1[0][1]*M2[1][1]) % mod
    res[1][0] = (M1[1][0]*M2[0][0] + M1[1][1]*M2[1][0]) % mod
    res[1][1] = (M1[1][0]*M2[0][1] + M1[1][1]*M2[1][1]) % mod
    return res

def fastMatrixDrift(M, X):
    if X == 1:
        return M
    subMatrix = fastMatrixDrift(M, X//2)
    multiplied = matrixMultiplication(subMatrix, subMatrix)
    if X % 2 == 0:
        return multiplied
    else:
        return matrixMultiplication(multiplied, M)
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M = list(map(int, input().split()))
    X = int(input())
    M = [[M[0],M[1]],[M[2],M[3]]]
    ans = fastMatrixDrift(M, X)
    sys.stdout.write(f"{ans[0][0]} {ans[0][1]}\n")
    sys.stdout.write(f"{ans[1][0]} {ans[1][1]}\n")