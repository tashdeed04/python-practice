import sys
def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    tasks = []
    for i in range(n):
        a = int(data[idx])
        d = int(data[idx + 1])
        idx += 2
        tasks.append((a, d))
    tasks.sort()
    time = 0
    reward = 0
    for a, d in tasks:
        time += a
        reward += d - time
    print(reward)

main()