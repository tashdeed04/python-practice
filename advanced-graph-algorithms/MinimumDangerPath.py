import sys
import heapq

def dijkstra(adj, SRC, N):
    danger = [float('inf')] * (N+1)
    visited = [0] * (N+1)
    danger[SRC] = 0
    Q = [(0, SRC)]

    while Q:
        D, U = heapq.heappop(Q)
        if visited[U] == 1:
            continue
        visited[U] = 1

        for i, j in adj[U]:
            newDanger = max(danger[U], j)
            if danger[i] > newDanger:
                danger[i] = newDanger
                heapq.heappush(Q, (danger[i], i))

    return danger

def taskC():
    N, M = map(int, sys.stdin.readline().split())
    adj = [[] for i in range(N+1)]

    for i in range(M):
        U , V , W = map(int, sys.stdin.readline().split())        
        adj[U].append((V, W))
        adj[V].append((U, W))
    danger = dijkstra(adj, 1, N)
    res = []

    for i in range(1, N+1):
        if danger[i] == float('inf'):
            res.append("-1")
        else:
            res.append(str(danger[i]))

    sys.stdout.write(" ".join(res) + "\n")
taskC()