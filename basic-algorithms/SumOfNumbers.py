import sys
T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    res = N*(N+1)//2
    sys.stdout.write(f"{res}\n")