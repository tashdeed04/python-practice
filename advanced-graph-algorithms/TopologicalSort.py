import sys
from collections import deque
T = int(sys.stdin.readline())
for i in range(T):
    x = sys.stdin.readline().strip()
    while x == "":
        x = sys.stdin.readline().strip()
    N, M = map(int, x.split())    
    G = [[] for i in range(N+1)]
    inD = [0] * (N+1)
    
    for i in range(M):
        A, B = map(int, sys.stdin.readline().split())
        G[A].append(B)
        inD[B] += 1    
    queue = deque()

    for i in range(1, N+1):
        if inD[i] == 0:
            queue.append(i)
    Ord = []

    while queue:
        Node = queue.popleft()
        Ord.append(Node)
        for i in G[Node]:
            inD[i] -= 1
            if inD[i] == 0:
                queue.append(i)

    if len(Ord) == N:
        sys.stdout.write(" ".join(map(str, Ord)) + "\n")
    else:
        sys.stdout.write("-1\n")