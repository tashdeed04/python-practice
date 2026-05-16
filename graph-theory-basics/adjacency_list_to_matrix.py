import sys

N = int(sys.stdin.readline())

mtrx = [[0] * N for i in range(N)]

for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    k = line[0]
    neighbors = line[1:]
    for j in neighbors:
        mtrx[i][j] = 1

for row in mtrx:
    sys.stdout.write(" ".join(map(str, row)) + "\n")
