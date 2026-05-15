def sortStudents(ID, marks):
    arr = []
    for i in range(len(ID)):
        arr.append((marks[i], ID[i], i))
    for i in range(len(arr)):
        pos = i
        for j in range(i + 1, len(arr)):
            if (arr[j][0] > arr[pos][0] or
               (arr[j][0] == arr[pos][0] and
                arr[j][1] < arr[pos][1])):
                pos = j
        if pos != i:
            arr[i], arr[pos] = arr[pos], arr[i]
    visited = [False] * len(arr)
    swaps = 0
    for i in range(len(arr)):
        if visited[i] or arr[i][2] == i:
            continue
        size = 0
        k = i
        while not visited[k]:
            visited[k] = True
            k = arr[k][2]
            size += 1
        if size > 1:
            swaps += size - 1
    print(f"Minimum swaps: {swaps}")
    for i in range(len(arr)):
        print(f"ID: {arr[i][1]} Mark: {arr[i][0]}")
testcases = int(input())
for i in range(testcases):
    n = int(input())
    ID = input().split(" ")
    marks = input().split(" ")
    for j in range(n):
        ID[j] = int(ID[j])
        marks[j] = int(marks[j])
    sortStudents(ID, marks)