import sys
N = int(sys.stdin.readline())
arr1 = sys.stdin.readline().split()
A = []
for i in arr1:
    A.append(int(i))
swap = True
while swap:
    swap = False
    for i in range(N - 1):
        if (A[i] % 2 == A[i + 1] % 2) and (A[i] > A[i + 1]):
            temp = A[i]
            A[i] = A[i + 1]
            A[i + 1] = temp
            swap = True
for i in range(N):
    sys.stdout.write(f"{A[i]}")
    if i < N - 1:
        sys.stdout.write(" ")