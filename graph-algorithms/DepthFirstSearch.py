import sys
sys.setrecursionlimit(2*100000 + 5)
N,M = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))
y = list(map(int, sys.stdin.readline().split()))

G = [[0] for i in range(N+1)]
for i in range(M):
    U = x[i]
    V = y[i]
    G[U].append(V)
    G[V].append(U)

visit = [False] * (N+1)

def dfs(node):
    visit[node] = True
    sys.stdout.write(str(node) + " ")

    for j in G[node]:
        if not visit[j]:
            dfs(j)

dfs(1)
sys.stdout.write("\n")