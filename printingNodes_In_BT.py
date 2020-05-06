class binaryTree:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
def pr(root):
	if root==None:
		return
	print(root.data)
	pr(root.left)
	pr(root.right)
def inp():
	rootData=int(input())
	if rootData==-1:
		return None
	root=binaryTree(rootData)
	leftN=inp()
	rightN=inp()
	root.left=leftN
	root.right=rightN
	return root
def root_to_Node(root,k):
	if root==None:
		return None
	if root.data==k:
		li=list()
		li.append(root.data)
		return li
	leftOutput=root_to_Node(root.left,k)
	if leftOutput!=None:
		leftOutput.append(root.data)
		return leftOutput
	rightOutput=root_to_Node(root.right,k)
	if rightOutput!=None:
		rightOutput.append(root.data)
		return rightOutput
	else:
		return None

root=inp()
print(root_to_Node(root,7))