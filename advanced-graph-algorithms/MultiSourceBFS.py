import sys
from collections import deque
N , M , S , Q = map(int, sys.stdin.readline().split())
G = [[] for i in range(N+1)]

for i in range(M):
    U , V = map(int, sys.stdin.readline().split())
    G[U].append(V)
    G[V].append(U)

s = list(map(int, sys.stdin.readline().split()))
d = list(map(int, sys.stdin.readline().split()))
dst = [-1] * (N+1)
queue = deque()

for i in s:
    dst[i] = 0
    queue.append(i)
while queue:
    Node = queue.popleft()
    for j in G[Node]:
        if dst[j] == -1:
            dst[j] = dst[Node] + 1
            queue.append(j)
res = []
for i in d:
    res.append(str(dst[i]))
sys.stdout.write(" ".join(res) + "\n")