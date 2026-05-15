import sys
N,M = map(int, sys.stdin.readline().split())
G = [[] for i in range(N+1)]
for i in range(M):
    U,V = map(int, sys.stdin.readline().split())
    G[U].append(V)
    G[V].append(U)

visit = [False] * (N+1)
queue = [1]
visit[1] = True
res = []

while queue:
    node = queue.pop(0)
    res.append(node)

    for j in G[node]:
        if not visit[j]:
            visit[j] = True
            queue.append(j)

sys.stdout.write(" ".join(map(str, res)) + "\n")