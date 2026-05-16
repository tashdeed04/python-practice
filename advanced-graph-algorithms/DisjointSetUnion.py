import sys
import heapq
def main(): 
    T = int(sys.stdin.readline())

    for i in range(T):
        N, M, S, D = map(int, sys.stdin.readline().split())
        u = list(map(int, sys.stdin.readline().split()))
        v = list(map(int, sys.stdin.readline().split()))
        w = list(map(int, sys.stdin.readline().split()))
        graph = [[] for i in range(N + 1)]
        for i in range(M):
            graph[u[i]].append((v[i], w[i]))
            graph[v[i]].append((u[i], w[i]))
        best = [-1] * (N + 1)
        best[S] = float('inf')
        pq = [(-best[S], S)]

        while pq:
            value, node = heapq.heappop(pq)
            value = -value
            if value < best[node]:
                continue
            for nxt, weight in graph[node]:
                newValue = min(value, weight)
                if newValue > best[nxt]:
                    best[nxt] = newValue
                    heapq.heappush(pq, (-newValue, nxt))
        if best[D] == -1:
            print(0)
        else:
            print(best[D])
main()