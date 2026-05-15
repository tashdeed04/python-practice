import sys
from collections import deque
R, H = map(int, sys.stdin.readline().split())
G = []
for i in range(R):
    G.append(sys.stdin.readline().strip())

visit = [[False] * H for i in range(R)]
top = 0
for i in range(R):
    for j in range(H):
        if G[i][j] != '#' and not visit[i][j]:
            diamond = 0
            queue = deque()
            queue.append((i, j))
            visit[i][j] = True
            while queue:
                x, y = queue.popleft()
                if G[x][y] == 'D':
                    diamond += 1                
                if x-1 >= 0 and G[x-1][y] != '#' and not visit[x-1][y]:
                    visit[x-1][y] = True
                    queue.append((x-1, y))                
                if x+1 < R and G[x+1][y] != '#' and not visit[x+1][y]:
                    visit[x+1][y] = True
                    queue.append((x+1, y))                
                if y-1 >= 0 and G[x][y-1] != '#' and not visit[x][y-1]:
                    visit[x][y-1] = True
                    queue.append((x, y-1))                
                if y+1 < H and G[x][y+1] != '#' and not visit[x][y+1]:
                    visit[x][y+1] = True
                    queue.append((x, y+1))
            if diamond > top:
                top = diamond

sys.stdout.write(str(top) + "\n")