import sys
T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    if N%2 == 0:
        sys.stdout.write(f"{N} is an Oven number.\n")
    else:
        sys.stdout.write(f"{N} is an Odd number.\n")