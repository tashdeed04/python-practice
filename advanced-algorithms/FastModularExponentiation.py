def fastPowerDrift(a, b):
    if b == 0:
        return 1
    halfPower = fastPowerDrift(a, b // 2)
    com = (halfPower * halfPower) % 107
    if b % 2 != 0:
        com = (com * a) % 107
    return com
arr = input().split()
a = int(arr[0])
b = int(arr[1])
print(fastPowerDrift(a, b))