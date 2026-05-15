import sys
from collections import deque
N,M,S,D = map(int, sys.stdin.readline().split())

if M==0:
    x = []
    y = []

else:
    x = list(map(int, sys.stdin.readline().split()))
    y = list(map(int, sys.stdin.readline().split()))

G = [[] for i in range(N+1)]

for i in range(M):
    U = x[i]
    V = y[i]
    G[U].append(V)
    G[V].append(U)

for i in range(N+1):
    G[i].sort()

d = [-1] * (N+1)
p = [-1] * (N+1)
d[S] = 0
queue = deque()
queue.append(S)

while queue:
    node = queue.popleft()

    for j in G[node]:
        if d[j] == -1:
            d[j] = d[node] + 1
            p[j] = node
            queue.append(j)
            
if d[D] == -1:
    sys.stdout.write("-1\n")

else:
    path = []
    curr = D
    while curr != -1:
        path.append(curr)
        curr = p[curr]

    path.reverse()

    sys.stdout.write(str(d[D]) + "\n")
    sys.stdout.write(" ".join(map(str, path)) + "\n")