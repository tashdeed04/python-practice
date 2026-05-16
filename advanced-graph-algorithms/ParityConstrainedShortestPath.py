import sys
import heapq

def dijkstra(adj, SRC, N):
    INF = float('inf')   
    dist = [[INF, INF] for i in range(N+1)]    
    dist[SRC][0] = 0
    dist[SRC][1] = 0
    Q = [(0, SRC, 0), (0, SRC, 1)]
    
    while Q:
        D , U , P = heapq.heappop(Q)
        if D > dist[U][P]:
            continue

        for i, j in adj[U]:
            x = j % 2
            if x != P:
                y = D + j
                if y < dist[i][x]:
                    dist[i][x] = y
                    heapq.heappush(Q, (y, i, x))
    return dist

def taskE():
    N , M = map(int, sys.stdin.readline().split())
    uLst = list(map(int, sys.stdin.readline().split()))
    vLst = list(map(int, sys.stdin.readline().split()))
    wLst = list(map(int, sys.stdin.readline().split()))
    adj = [[] for i in range(N+1)]

    for i in range(M):
        adj[uLst[i]].append((vLst[i], wLst[i]))
    dist = dijkstra(adj, 1, N)
    res = min(dist[N][0], dist[N][1])
    if res == float('inf'):
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(str(res) + "\n")
taskE()