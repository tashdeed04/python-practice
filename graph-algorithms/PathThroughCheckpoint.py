import sys
from collections import deque

def bfs(start, end, G, N):
    p = [-1] * (N + 1)
    p[start] = 0
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        for i in G[node]:
            if p[i] == -1:
                p[i] = node
                queue.append(i)

    if p[end] == -1 and start != end:
        return None    
    path = []
    curr = end
    while curr != 0:
        path.append(curr)
        curr = p[curr]
    path.reverse()
    return path

l1 = sys.stdin.readline().split()
N = int(l1[0])
M = int(l1[1])
S = int(l1[2])
D = int(l1[3])
K = int(l1[4])

G = [[] for i in range(N + 1)]
for i in range(M):
    parts = sys.stdin.readline().split()
    U = int(parts[0])
    V = int(parts[1])
    G[U].append(V)

path1 = bfs(S, K, G, N)
path2 = bfs(K, D, G, N)
if path1 is None or path2 is None:
    sys.stdout.write("-1\n")
else:   
    totalPath = path1 + path2[1:]
    dist = len(totalPath) - 1

    sys.stdout.write(str(dist) + "\n")
    sys.stdout.write(" ".join(map(str, totalPath)) + "\n")