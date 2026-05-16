import sys
def main():
    N = int(sys.stdin.readline())
    tasks = []
    for i in range(N):
        s, e = map(int, sys.stdin.readline().split())
        tasks.append((e, s))
    tasks.sort()
    res = []
    lastEnd = -1
    for e, s in tasks:
        if s > lastEnd:
            res.append((s, e))
            lastEnd = e
    sys.stdout.write(str(len(res)) + '\n')
    for s, e in res:
        sys.stdout.write(str(s) + ' ' + str(e) + '\n')

main()