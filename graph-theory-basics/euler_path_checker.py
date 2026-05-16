import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

deg = [0] * (N + 1)
adj = [[] for i in range(N + 1)]

if M > 0:
    u_list = list(map(int, sys.stdin.readline().split()))
    v_list = list(map(int, sys.stdin.readline().split()))

    for i in range(M):
        u = u_list[i]
        v = v_list[i]
        deg[u] += 1
        deg[v] += 1
        adj[u].append(v)
        adj[v].append(u)
else:
    sys.stdin.readline()
    sys.stdin.readline()

odd_count = 0
for i in range(1, N + 1):
    if deg[i] % 2 == 1:
        odd_count += 1

start = -1
for i in range(1, N + 1):
    if deg[i] > 0:
        start = i
        break

if start == -1:
    sys.stdout.write("YES\n")
else:
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for nb in adj[node]:
            if not visited[nb]:
                visited[nb] = True
                queue.append(nb)

    connected = True
    for i in range(1, N + 1):
        if deg[i] > 0 and not visited[i]:
            connected = False
            break

    if connected and (odd_count == 0 or odd_count == 2):
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")
