count = 0
def merge(a, b):
    global count
    lft, rgt = 0, 0
    lftLen = len(a)
    rgtLen = len(b)
    sorted = [0] * (lftLen + rgtLen)
    i = 0
    while lft < lftLen and rgt < rgtLen:
        if a[lft] <= b[rgt]:
            sorted[i] = a[lft]
            lft += 1
        else:
            sorted[i] = b[rgt]
            count += (lftLen - lft)
            rgt += 1
        i += 1
    while lft < lftLen:
        sorted[i] = a[lft]
        i, lft = i+1, lft+1
    while rgt < rgtLen:
        sorted[i] = b[rgt]
        i, rgt = i+1, rgt+1
    return sorted

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)
input()
arr = input().split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])

ans = mergeSort(arr)
print(count)
for elem in ans:
    print(elem, end=" ")