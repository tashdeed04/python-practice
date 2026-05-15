import sys
from collections import deque
n = int(sys.stdin.readline())
x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
if x1 == x2 and y1 == y2:
    sys.stdout.write("0\n")
    sys.exit()
X = [1, 1, -1, -1, 2, 2, -2, -2]
Y = [2, -2, 2, -2, 1, -1, 1, -1]
visite = [[False] * (n+1) for i in range(n+1)]
q = deque()
q.append((x1, y1, 0))
visite[x1][y1] = True

while q:
    x, y, d = q.popleft()
    for i in range(8):
        j = x + X[i]
        k = y + Y[i]
        if 1 <= j <= n and 1 <= k <= n and not visite[j][k]:
            if j == x2 and k == y2:
                sys.stdout.write(str(d + 1) + "\n")
                sys.exit()
            visite[j][k] = True
            q.append((j, k, d + 1))
sys.stdout.write("-1\n")