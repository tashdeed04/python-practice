import sys

def find(x, parent):    
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def main():
    N , K = map(int, sys.stdin.readline().split())
    parent = list(range(N + 1))
    size = [1] * (N + 1)
    res = []
    for i in range(K):
        a, b = map(int, sys.stdin.readline().split())
        X = find(a, parent)
        Y = find(b, parent)

        if X != Y:            
            if size[X] < size[Y]:
                X, Y = Y, X
            parent[Y] = X
            size[X] += size[Y]
        res.append(str(size[X]))
    sys.stdout.write('\n'.join(res))
main()