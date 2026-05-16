import sys
import heapq

def dijkstra(adj, SRC, weight, N):
    dist = [float('inf')] * (N+1)
    visited = [0] * (N+1)
    dist[SRC] = weight[SRC]
    Q = [(weight[SRC], SRC)]

    while Q:
        D, U = heapq.heappop(Q)

        if visited[U] == 1:
            continue
        visited[U] = 1

        for i in adj[U]:
            newCost = dist[U] + weight[i]
            if dist[i] > newCost:
                dist[i] = newCost
                heapq.heappush(Q, (dist[i], i))
    return dist

def taskD():
    N , M , S , D = map(int, sys.stdin.readline().split())
    weight = [0] + list(map(int, sys.stdin.readline().split()))
    adj = [[] for i in range(N+1)]

    for i in range(M):
        U, V = map(int, sys.stdin.readline().split())
        adj[U].append(V)

    dist = dijkstra(adj, S, weight, N)
    if dist[D] == float('inf'):
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(str(dist[D]) + "\n")
taskD()