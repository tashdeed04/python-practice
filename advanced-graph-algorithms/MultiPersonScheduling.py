import sys
def find(x, parent):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def main():
    N , M = map(int, sys.stdin.readline().split())
    edge = []
    for i in range(M):
        u, v, w = map(int, sys.stdin.readline().split())
        edge.append((w, u, v))    
    edge.sort()
    parent = list(range(N + 1))
    size = [1] * (N + 1)
    totalCost = 0
    edgesUsed = 0

    for w, u, v in edge:
        ru = find(u, parent)
        rv = find(v, parent)

        if ru != rv:            
            if size[ru] < size[rv]:
                ru, rv = rv, ru
            parent[rv] = ru
            size[ru] += size[rv]
            totalCost += w
            edgesUsed += 1            
            if edgesUsed == N - 1:
                break
    sys.stdout.write(str(totalCost))
main()