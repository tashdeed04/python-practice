import sys

N, M = map(int, sys.stdin.readline().split())

mtrx = [[0] * N for i in range(N)]

for i in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    mtrx[u - 1][v - 1] = w

for row in mtrx:
    sys.stdout.write(" ".join(map(str, row)) + "\n")
