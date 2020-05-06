import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
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
def build(preorder,inorder):
	if len(preorder)==0:
		return None
	rootD=preorder[0]
	root=BinaryTreeNode(rootD)
	index=0
	for i in range(0,len(inorder)):
		if inorder[i]==rootD:
			index=i
			break
	leftInorder=inorder[0:index]
	rightInorder=inorder[index+1:]

	lenleft=len(leftInorder)
	
	leftPreorder=preorder[1:lenleft+1]
	rightPreorder=preorder[lenleft+1:]

	leftChild=build(leftPreorder,leftInorder)
	rightChild=build(rightPreorder,rightInorder)

	root.left=leftChild
	root.right=rightChild

	return root

def build2(postorder,inorder):
	if len(postorder)==0:
		return None
	rootD=postorder[-1]
	root=BinaryTreeNode(rootD)
	index=0
	for i in range(0,len(inorder)):
		if inorder[i]==rootD:
			index=i
			break
	leftInorder=inorder[0:index]
	rightInorder=inorder[index+1:]

	lenleft=len(rightInorder)
	
	rightpostorder=postorder[-2:-lenleft-2]
	leftpostorder=postorder[-lenleft-2:-1]

	leftChild=build2(postorder,inorder)
	rightChild=build(postorder,inorder)

	root.left=leftChild
	root.right=rightChild

	return root

preorder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
postorder=[int(i) for i in input().strip().split()]
root = build2(postorder, inorder)
printLevelATNewLine(root)
