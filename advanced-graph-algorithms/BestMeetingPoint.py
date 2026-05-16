import sys
import heapq

def dijkstra(adj, SRC, N):
    dist = [float('inf')] * (N + 1)
    visited = [0] * (N + 1)

    dist[SRC] = 0
    Q = [(0, SRC)]

    while Q:
        D, U = heapq.heappop(Q)

        if visited[U] == 1:
            continue
        visited[U] = 1

        for i, j in adj[U]:
            if dist[i] > dist[U] + j:
                dist[i] = dist[U] + j
                heapq.heappush(Q, (dist[i], i))

    return dist

def taskB():
    N, M, S, T = map(int, sys.stdin.readline().split())
    adj = [[] for i in range(N + 1)]
    for i in range(M):
        U , V, W = map(int, sys.stdin.readline().split())
        adj[U].append((V, W))

    distS = dijkstra(adj, S, N)
    distT = dijkstra(adj, T, N)
    bestTime = float('inf')
    bestNode = -1

    for i in range(1, N + 1):
        if distS[i] != float('inf') and distT[i] != float('inf'):
            meetTime = max(distS[i], distT[i])
            if meetTime < bestTime:
                bestTime = meetTime
                bestNode = i

    if bestNode == -1:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(str(bestTime) + " " + str(bestNode) + "\n")

taskB()