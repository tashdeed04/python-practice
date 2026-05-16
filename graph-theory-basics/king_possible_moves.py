import sys

N = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().split())

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

moves = []
for dx, dy in directions:
    nx = x + dx
    ny = y + dy
    if 1 <= nx <= N and 1 <= ny <= N:
        moves.append((nx, ny))

moves.sort()

sys.stdout.write(str(len(moves)) + "\n")
for a, b in moves:
    sys.stdout.write(f"{a} {b}\n")
