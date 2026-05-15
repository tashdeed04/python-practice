import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
G = [[] for i in range(N+1)]
for i in range(N-1):
    U, V = map(int, input().split())
    G[U].append(V)
    G[V].append(U)

def bfs(s):
    dst = [-1] * (N+1)
    dst[s] = 0
    queue = deque()
    queue.append(s)
    while queue:
        Node = queue.popleft()
        for j in G[Node]:
            if dst[j] == -1:
                dst[j] = dst[Node] + 1
                queue.append(j)
    farNode = s
    farDst = 0
    for i in range(1, N+1):
        if dst[i] > farDst:
            farDst = dst[i]
            farNode = i
    return farNode, farDst

A, c = bfs(1)
B, d = bfs(A)
sys.stdout.write(str(d) + "\n")
sys.stdout.write(str(A) + " " + str(B) + "\n")