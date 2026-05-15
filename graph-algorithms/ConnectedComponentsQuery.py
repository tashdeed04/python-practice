import sys
from collections import deque
N, M, Q = map(int, sys.stdin.readline().split())
G = [[] for i in range(N + 1)]

for i in range(M):
    U, V = map(int, sys.stdin.readline().split())
    G[U].append(V)
    G[V].append(U)

x = [0] * (N + 1)
y = 0
for start in range(1, N + 1):
    if x[start] == 0:
        y += 1
        x[start] = y
        queue = deque()
        queue.append(start)
        while queue:
            node = queue.popleft()
            for i in G[node]:
                if x[i] == 0:
                    x[i] = y
                    queue.append(i)
res = []
for i in range(Q):
    X, Y = map(int, sys.stdin.readline().split())
    if x[X] == x[Y]:
        res.append("YES")
    else:
        res.append("NO")

sys.stdout.write("\n".join(res) + "\n")