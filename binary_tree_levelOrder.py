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
import queue
def inp():
	q=queue.Queue()
	print("enter root")
	rootD=int(input())
	if rootD!=-1:
		root=binaryTree(rootD)
	q.put(root)
	while(not(q.empty())):
		curr=q.get()
		
		print("enter left child of",curr.data)
		leftData=int(input())
		if leftData!=-1:
			leftN=binaryTree(leftData)
			curr.left=leftN
			q.put(leftN)

		print("enter right child of",curr.data)
		rightData=int(input())
		if rightData!=-1:
			rightN=binaryTree(rightData)
			curr.right=rightN
			q.put(rightN)
	return root
def pr2(root):
	q=queue.Queue()
	q.put(root)
	while(not(q.empty())):
		curr=q.get()
		print(curr.data)
		if curr.left is not None:
			print(curr.left.data)
			q.put(curr.left)
		if curr.right is not None:
			print(curr.right.data)
			q.put(curr.right)
		print()
	
				



root=inp()
pr2(root)