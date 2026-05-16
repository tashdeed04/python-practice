import sys
def main():
    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    res = []
    for i in range(T):
        N = int(data[idx])
        M = int(data[idx + 1])
        idx += 2
        tasks = []
        for i in range(N):
            start = int(data[idx])
            end = int(data[idx + 1])
            idx += 2
            tasks.append((end, start))
        tasks.sort()
        people = []
        count = 0
        for end, start in tasks:
            best = -1
            for i in range(len(people)):
                if people[i] < start:
                    if best == -1 or people[i] > people[best]:
                        best = i
            if best != -1:
                people[best] = end
                count += 1
            elif len(people) < M:
                people.append(end)
                count += 1
        res.append(str(count))
    print('\n'.join(res))
main()