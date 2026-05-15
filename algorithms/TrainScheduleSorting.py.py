def nameCheck(a, b):
    serial = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x = 0
    while x < len(a) and x < len(b):
        if a[x] != b[x]:
            return serial.index(a[x]) < serial.index(b[x])
        x += 1
    return len(a) < len(b)
def sortTrains(details):
    keys = []
    for key in details:
        keys.append(key)

    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            if not nameCheck(keys[i], keys[j]):
                keys[i], keys[j] = keys[j], keys[i]
    for key in keys:
        for i in range(len(details[key])):
            for j in range(i + 1, len(details[key])):
                if (details[key][i][1] < details[key][j][1] or
                   (details[key][i][1] == details[key][j][1] and
                    details[key][i][2] > details[key][j][2])):
                    details[key][i], details[key][j] = details[key][j], details[key][i]
        for i in range(len(details[key])):
            print(f"{key} will depart for {details[key][i][0]} at {details[key][i][1]}")
testcases = int(input())
details = {}
counter = 0
for i in range(testcases):
    data = input().split(" ")
    train = data[0]
    destination = data[4]
    time = data[6]
    if train in details:
        details[train].append((destination, time, counter))
    else:
        details[train] = [(destination, time, counter)]
    counter += 1
sortTrains(details)