import sys
import heapq

def shortest(adj, S, N):
    INF = float('inf')
    dist1 = [INF] * (N+1)
    dist2 = [INF] * (N+1)
    dist1[S] = 0
    Q = [(0, S)]

    while Q:
        D, U = heapq.heappop(Q)
        if D > dist2[U]:
            continue

        for i, j in adj[U]:
            x = D + j
            if x < dist1[i]:               
                dist2[i] = dist1[i]
                dist1[i] = x
                heapq.heappush(Q, (x, i))
            elif dist1[i] < x < dist2[i]:                
                dist2[i] = x
                heapq.heappush(Q, (x, i))
    return dist2

def taskF():
    N , M , S , D = map(int, sys.stdin.readline().split())
    adj = [[] for i in range(N+1)]

    for i in range(M):
        U , V , W = map(int, sys.stdin.readline().split())       
        adj[U].append((V, W))
        adj[V].append((U, W))
    dist2 = shortest(adj, S, N)
    if dist2[D] == float('inf'):
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(str(dist2[D]) + "\n")
taskF()