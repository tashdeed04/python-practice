import sys

def fastSeriesDrift(x, w, z):
    if w == 1:
        return (x % z, x % z)
    mid = w // 2
    s, p = fastSeriesDrift(x, mid, z)
    newP = (p * p) % z
    newS = (s * (1 + p)) % z
    if w % 2 == 1:
        newS = (newS + newP * x) % z
        newP = (newP * x) % z
    return newS, newP
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    x, w, z = map(int, input().split())
    ans, _ = fastSeriesDrift(x, w, z)
    sys.stdout.write(str(ans) + "\n")