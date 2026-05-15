import sys
N = int(sys.stdin.readline())
w = [sys.stdin.readline().strip() for i in range(N)]
adj = [[] for i in range(26)]
inD = [0] * 26
U = [False] * 26
Edg = [[False] * 26 for i in range(26)]
for i in w:
    for j in i:
        U[ord(j) - 97] = True
inValid = False
for i in range(N - 1):
    a = w[i]
    b = w[i + 1]
    m = min(len(a), len(b))
    found = False
    for j in range(m):
        if a[j] != b[j]:
            u = ord(a[j]) - 97
            v = ord(b[j]) - 97
            if not Edg[u][v]:
                Edg[u][v] = True
                adj[u].append(v)
                inD[v] += 1
            found = True
            break
    if not found and len(a) > len(b):
        inValid = True
        break
if inValid:
    sys.stdout.write("-1\n")
else:
    q = []
    for i in range(26):
        if U[i] and inD[i] == 0:
            q.append(i)
    q.sort()
    res = []
    while q:
        u = q.pop(0)
        res.append(chr(u + 97))
        for v in adj[u]:
            inD[v] -= 1
            if inD[v] == 0:
                q.append(v)
        q.sort()
    countUsed = sum(U)
    if len(res) != countUsed:
        sys.stdout.write("-1\n")
    else:        
        final = []
        ri = 0
        for i in range(26):
            if not U[i]:                
                while ri < len(res) and ord(res[ri]) - 97 < i:
                    final.append(res[ri])
                    ri += 1
                final.append(chr(i + 97))        
        while ri < len(res):
            final.append(res[ri])
            ri += 1

        sys.stdout.write("".join(final) + "\n")