import sys
from math import gcd

data = sys.stdin.buffer.read().split()
idx = 0

N = int(data[idx]); idx += 1
Q = int(data[idx]); idx += 1

nb = [[] for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if gcd(i, j) == 1:
            nb[i].append(j)
            nb[j].append(i)

for i in range(1, N + 1):
    nb[i].sort()

out = []
for i in range(Q):
    X = int(data[idx]); idx += 1
    K = int(data[idx]); idx += 1

    if K > len(nb[X]):
        out.append("-1")
    else:
        out.append(str(nb[X][K - 1]))

sys.stdout.write("\n".join(out) + "\n")
