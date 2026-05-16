import sys

def find(x, parent):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def main():
    N, M = map(int, sys.stdin.readline().split())
    edges = []
    for i in range(M):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v, i))
    sortedEdges = sorted(edges)
    parent = list(range(N + 1))
    size = [1] * (N + 1)
    mstAdj = [[] for i in range(N + 1)]
    inMst = [False] * M
    mstCost = 0
    used = 0
    for w, u, v, idx in sortedEdges:
        ru = find(u, parent)
        rv = find(v, parent)
        if ru != rv:
            if size[ru] < size[rv]:
                ru, rv = rv, ru
            parent[rv] = ru
            size[ru] += size[rv]
            mstAdj[u].append((v, w))
            mstAdj[v].append((u, w))
            mstCost += w
            inMst[idx] = True
            used += 1
    if used != N - 1:
        print(-1)
        return
    def two_max_on_path(src, dst):
        visited = [False] * (N + 1)
        par = [0] * (N + 1)
        par_w = [0] * (N + 1)
        stack = [src]
        visited[src] = True
        while stack:
            node = stack.pop()
            if node == dst:
                 break

            for nxt, w in mstAdj[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    par[nxt] = node
                    par_w[nxt] = w
                    stack.append(nxt)
        max1 = -1
        max2 = -1
        cur = dst
        while cur != src:
            w = par_w[cur]
            if w > max1:
                max2 = max1
                max1 = w
            elif w > max2 and w != max1:
                max2 = w
            cur = par[cur]
        return max1, max2
    ans = float('inf')
    for w, u, v, idx in sortedEdges:
        if inMst[idx]:
            continue
        max1, max2 = two_max_on_path(u, v)
        if w > max1:
            ans = min(ans, mstCost + w - max1)
        elif w == max1 and max2 != -1:
            ans = min(ans, mstCost + w - max2)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
main()