import sys

def preOrder(inOrder, postOrder):
    if inOrder == [] or postOrder == []:
        return []    
    idxMap = {}
    for i in range(len(inOrder)):
        idxMap[inOrder[i]] = i

    root = postOrder[-1]
    rootIdx = idxMap[root]
    lftIn = inOrder[:rootIdx]
    rgtIn = inOrder[rootIdx+1:]
    lftPost = postOrder[:len(lftIn)]
    rgtPost = postOrder[len(lftIn):-1]
    lftPre = preOrder(lftIn, lftPost)
    rgtPre = preOrder(rgtIn, rgtPost)
    return [root] + lftPre + rgtPre

input = sys.stdin.readline
n = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))
res = preOrder(inOrder, postOrder)
sys.stdout.write(" ".join(map(str, res)))