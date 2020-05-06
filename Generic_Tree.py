class TreeNode:
	def __init__(self,data):
		self.data=data
		self.children=list()

def inp():
	rootD=int(input())
	if rootD==-1:
		return None
	root=TreeNode(rootD)
	childCount=int(input("enter no. children"))
	for i in range(childCount):
		child=inp()
		root.children.append(child)
	return root

def pr(root):
	print(root.data)
	for x in root.children:
		pr(x)

def NumNodes(root):
	c=1
	for i in root.children:
		c+=NumNodes(i)
	return c

def add(root):
	sum=0
	sum+=root.data
	for i in root.children:
		sum+=i
	return sum

root=inp()
print(sum(root))
