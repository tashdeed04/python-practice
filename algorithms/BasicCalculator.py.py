import sys
T = int(sys.stdin.readline())
for i in range(T):
    N = sys.stdin.readline().strip()
    K = N.split()
    first = float(K[1])
    sign = K[2]
    second = float(K[3])
    if sign == "+":
        res = first + second
    elif sign == "-":
        res = first - second
    elif sign == "*":
        res = first * second
    elif sign == "/":
        res = first / second
    sys.stdout.write(f"{res:.6f}\n")