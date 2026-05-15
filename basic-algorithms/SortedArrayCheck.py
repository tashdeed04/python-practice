import sys
T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    arr = sys.stdin.readline().split()
    for i in range(N-1):
        if int(arr[i]) > int(arr[i+1]):
            sys.stdout.write("NO\n")
            break
    else:
        sys.stdout.write("YES\n")