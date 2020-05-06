import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def const(li):
	if len(li)==0:
		return None

	mid=len(li)//2
	root=BinaryTreeNode(li[mid])
	
	
	root.left=const(li[0:mid])
	root.right=const(li[mid+1:])	

	return root
def pr(root):
	if root==None:
		return
	print(root.data)
	pr(root.left)
	pr(root.right)
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

li=[int(i) for i in input().strip().split()]
#li2=[1,2,3,4,5,6,7]
root=const(li)
pr(root)