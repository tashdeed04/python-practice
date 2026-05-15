import sys

def postOrder(inOrder, preOrder):
    if inOrder == [] or preOrder == []:
        return []
    idxMap = {}
    for i in range(len(inOrder)):
        idxMap[inOrder[i]] = i

    root = preOrder[0]
    rootIdx = idxMap[root]
    lftIn = inOrder[:rootIdx]
    rgtIn = inOrder[rootIdx+1:]
    lftPre = preOrder[1:1+len(lftIn)]
    rgtPre = preOrder[1+len(lftIn):]
    lftPost = postOrder(lftIn, lftPre)
    rgtPost = postOrder(rgtIn, rgtPre)    
    return lftPost + rgtPost + [root]

input = sys.stdin.readline
n = int(input())
inOrder = list(map(int, input().split()))
preOrder = list(map(int, input().split()))
res = postOrder(inOrder, preOrder)
sys.stdout.write(" ".join(map(str, res)))