import sys
sys.setrecursionlimit(200000)

def orderingBinaryTree(arr, lft, rgt, res):
    if lft > rgt:
        return    
    mid = (lft + rgt) // 2
    res.append(arr[mid])
    orderingBinaryTree(arr, lft, mid - 1, res)
    orderingBinaryTree(arr, mid + 1, rgt, res)
input = sys.stdin.readline
len = int(input())
arr = list(map(int, input().split()))
res = []
orderingBinaryTree(arr, 0, len - 1, res)
sys.stdout.write(" ".join(map(str, res)))