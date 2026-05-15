import sys
from collections import deque

N = sys.stdin.readline().split()
S = N[0]
C = N[1]
N = int(sys.stdin.readline())
f = set()
for i in range(N):
    f.add(sys.stdin.readline().strip())
if S == C:
    sys.stdout.write("0\n")
elif S in f or C in f:
    sys.stdout.write("-1\n")
else:    
    dst = {}
    dst[S] = 0
    queue = deque()
    queue.append(S)
    res = -1

    while queue:
        curr = queue.popleft()
        d = dst[curr]        
        for i in range(4):
            dgt = int(curr[i])            
            newDgt = (dgt + 1) % 10
            newCombo = curr[:i] + str(newDgt) + curr[i+1:]
            if newCombo not in f and newCombo not in dst:
                dst[newCombo] = d + 1
                if newCombo == C:
                    res = d + 1
                    queue.clear()
                    break
                queue.append(newCombo)            
            newDgt = (dgt - 1) % 10
            newCombo = curr[:i] + str(newDgt) + curr[i+1:]
            if newCombo not in f and newCombo not in dst:
                dst[newCombo] = d + 1
                if newCombo == C:
                    res = d + 1
                    queue.clear()
                    break
                queue.append(newCombo)
        if res != -1:
            break
    sys.stdout.write(str(res) + "\n")