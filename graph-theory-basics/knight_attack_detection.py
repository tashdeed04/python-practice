import sys

N, M, K = map(int, sys.stdin.readline().split())

pos = set()
knights = []

for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    pos.add((x, y))
    knights.append((x, y))

kmoves = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2),  (1, 2),  (2, -1),  (2, 1)
]

found = False
for x, y in knights:
    for dx, dy in kmoves:
        nx, ny = x + dx, y + dy
        if (nx, ny) in pos:
            found = True
            break
    if found:
        break

sys.stdout.write("YES\n" if found else "NO\n")
