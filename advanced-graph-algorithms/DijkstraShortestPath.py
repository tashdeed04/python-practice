import sys
import heapq
def dijkstra(adj, S, N):
    dist = [float('inf')] * (N+1)
    parent = [None] * (N+1)
    visited = [0] * (N+1)

    dist[S] = 0
    Q = [(0 , S)]
    while Q:
        D , U = heapq.heappop(Q)

        if visited[U] == 1:
            continue
        visited[U] = 1

        for i,j in adj[U]:
            if dist[i] > dist[U] + j:
                dist[i] = dist[U] + j
                parent[i] = U
                heapq.heappush(Q, (dist[i], i))
    
    return dist, parent

def taskA():
    
    N, M, S, D = map(int, sys.stdin.readline().split())

    uLst = list(map(int, sys.stdin.readline().split()))
    vLst = list(map(int, sys.stdin.readline().split()))
    wLst = list(map(int, sys.stdin.readline().split()))

    adj = [[] for i in range(N + 1)]
    for i in range(M):
        adj[uLst[i]].append((vLst[i], wLst[i]))
    
    dist, parent = dijkstra(adj, S, N)
    
    if dist[D] == float('inf'):
        sys.stdout.write("-1\n")
        return
    
    p = []
    curr = D
    while curr is not None:
        p.append(curr)
        curr = parent[curr]
    p.reverse()

    sys.stdout.write(str(dist[D]) + "\n")
    sys.stdout.write(" ".join(map(str, p)) + "\n")


taskA()