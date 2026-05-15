import sys
from collections import deque

X = sys.stdin.readline().split()
N = int(X[0])
A = X[1]
B = X[2]
words = []
for i in range(N):
    words.append(sys.stdin.readline().strip())
G = [[] for i in range(N)]
for i in range(N):
    for j in range(N):
        if i != j:
            if words[i][-1] == words[j][0]:
                G[i].append(j)
sIdx = -1
endIdx = -1
for i in range(N):
    if words[i] == A:
        sIdx = i
    if words[i] == B:
        endIdx = i
visite = [False] * N
visite[sIdx] = True
queue = deque()
queue.append(sIdx)
found = False
while queue:
    Node = queue.popleft()
    if Node == endIdx:
        found = True
        break
    for i in G[Node]:
        if not visite[i]:
            visite[i] = True
            queue.append(i)
if found:
    sys.stdout.write("YES\n")
else:
    sys.stdout.write("NO\n")