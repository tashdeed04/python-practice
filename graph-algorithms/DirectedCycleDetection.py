import sys
sys.setrecursionlimit(2*100000+5)
N, M = map(int, sys.stdin.readline().split())
G = [[] for i in range(N+1)]

for i in range(M):
    U,V = map(int, sys.stdin.readline().split())
    G[U].append(V)
clr = [0] * (N+1)
cycle = False

def dfs(node):
    clr[node] = 1
    for i in G[node]:
        if clr[i] == 1:
            cycle[0] = True
            return
        if clr[i] == 0:
            dfs(i)
        if cycle[0]:
            return
    clr[node] = 2

for i in range(1, N+1):
    if clr[i] == 0:
        dfs(i)
    if cycle:
        break

if cycle:
    sys.stdout.write("YES\n")
else:
    sys.stdout.write("NO\n")