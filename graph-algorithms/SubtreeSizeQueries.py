import sys
from collections import deque

N,R = map(int, sys.stdin.readline().split())
G = [[] for i in range(N + 1)]

for i in range(N - 1):
    U, V = map(int, sys.stdin.readline().split())
    G[U].append(V)
    G[V].append(U)

p = [-1] * (N + 1)
p[R] = 0
ord = []
visit = [False] * (N + 1)
visit[R] = True
queue = deque()
queue.append(R)
while queue:
    node = queue.popleft()
    ord.append(node)
    for i in G[node]:
        if not visit[i]:
            visit[i] = True
            p[i] = node
            queue.append(i)

size = [1] * (N+1)
for node in reversed(ord):
    if p[node] != 0:
        size[p[node]] += size[node]

Q = int(sys.stdin.readline())
res = []
for i in range(Q):
    X = int(sys.stdin.readline())
    res.append(str(size[X]))

sys.stdout.write("\n".join(res) +"\n")