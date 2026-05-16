import sys

N, M = map(int, sys.stdin.readline().split())

diff = [0] * (N + 1)

if M > 0:
    u_list = list(map(int, sys.stdin.readline().split()))
    v_list = list(map(int, sys.stdin.readline().split()))

    for i in range(M):
        u = u_list[i]
        v = v_list[i]
        diff[u] -= 1
        diff[v] += 1

sys.stdout.write(" ".join(map(str, diff[1:])) + "\n")
