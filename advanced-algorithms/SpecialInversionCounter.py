count = 0
def merge(a, b):
    global count
    lft, rgt = 0, 0
    lftLen = len(a)
    rgtLen = len(b)
    sorted_arr = [0] * (lftLen + rgtLen)
    i = 0
    while lft < lftLen and rgt < rgtLen:
        if a[lft] <= b[rgt]:
            sorted_arr[i] = a[lft]
            lft += 1
        else:
            sorted_arr[i] = b[rgt]
            target = b[rgt] ** 2
            L, R = lft, lftLen
            while L < R:
                mid = (L + R) // 2
                if a[mid] > target:
                    R = mid
                else:
                    L = mid + 1
            count += (lftLen - L)
            rgt += 1        
        i += 1
    while lft < lftLen:
        sorted_arr[i] = a[lft]
        i, lft = i+1, lft+1    
    while rgt < rgtLen:
        sorted_arr[i] = b[rgt]
        i, rgt = i+1, rgt+1    
    return sorted_arr

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
mergeSort(arr)
print(count)

