import sys
from collections import deque
N , M = map(int, sys.stdin.readline().split())
G = [[] for i in range(N+1)]
for i in range(M):
    U , V = map(int, sys.stdin.readline().split())
    G[U].append(V)
    G[V].append(U)

clr = [-1] * (N+1)
res = 0
for i in range(1, N+1):
    if clr[i] != -1:
        continue
    queue = deque()
    queue.append(i)
    clr[i] = 0
    count = [0,0]
    count[0] = 1
    is_bipartite = True

    while queue:
        Node = queue.popleft()
        for i in G[Node]:
            if clr[i] == -1:
                clr[i] = 1 - clr[Node]
                count[clr[i]] += 1
                queue.append(i)
            elif clr[i] == clr[Node]:
                is_bipartite = False

    if is_bipartite:
        res += max(count[0], count[1])
    else:
        res += count[0] + count[1]

sys.stdout.write(str(res) + "\n")
