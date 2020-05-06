import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inp():
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    leftN=inp()
    rightN=inp()
    root.left=leftN
    root.right=rightN
    return root
def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ
def duplicate(root):
    if root==None:
        return
    temp=BinaryTreeNode(root.data)
    l=root.left
    root.left=temp
    temp.left=l
    duplicate(temp.left)
    duplicate(root.right)
root=inp()
duplicate(root)
printLevelATNewLine(root)