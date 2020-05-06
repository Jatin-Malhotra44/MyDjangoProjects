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

def Search(root,x):
	if root==None:
		return False
	if root.data==x:
		return True
	if root.data>x and root.left!=None:
		return Search(root.left,x)
	elif root.data<x and root.right!=None:
		return Search(root.right,x)

def range(root,k1,k2):
	if root==None:
		return None
	if root.data<k1:
		range(root.right,k1,k2)
	elif root.data>k2:
		range(root.left,k1,k2)
	else:
		print(root.data)
		range(root.left,k1,k2)
		range(root.right,k1,k2)

def Min(root):
	if root==None:
		return 1000
	leftMin=Min(root.left)
	rightMin=Min(root.right)
	return min(leftMin,rightMin,root.data)
def Max(root):
	if root==None:
		return -1000
	leftMax=Max(root.left)
	rightMax=Max(root.right)
	return max(leftMax,rightMax,root.data)

def check(root):
	if root==None:
		return True
	leftMax=Max(root.left)
	rightMin=Min(root.right)
	if(root.data<leftMax or root.data>rightMin):
		return False
	checkL=check(root.left)
	checkR=check(root.right)
	return checkL and checkR
root=inp()
print(check(root))