import sys

N, M = map(int, sys.stdin.readline().split())

u_list = list(map(int, sys.stdin.readline().split()))
v_list = list(map(int, sys.stdin.readline().split()))
w_list = list(map(int, sys.stdin.readline().split()))

adj = {}
for i in range(1, N + 1):
    adj[i] = []

for i in range(M):
    u = u_list[i]
    v = v_list[i]
    w = w_list[i]
    adj[u].append((v, w))

for i in range(1, N + 1):
    adj[i].sort()
    if adj[i]:
        neighbors = " ".join(f"({v},{w})" for v, w in adj[i])
        sys.stdout.write(f"{i}: {neighbors}\n")
    else:
        sys.stdout.write(f"{i}:\n")
