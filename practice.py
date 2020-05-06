import queue
class BinaryTreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def inp():
	rootD=int(input())
	if rootD== -1:
		return None
	root=BinaryTreeNode(rootD)
	leftN=inp()
	rightN=inp()
	root.left=leftN
	root.right=rightN
	return root

def pr(root):
	if root==None:
		return None
	print(root.data)
	pr(root.left)
	pr(root.right)
	return

def count(root):
	if root==None:
		return 0
	c=1
	c+=count(root.left)
	c+=count(root.right)
	return c

def sum(root):
	if root==None:
		return 0
	res=root.data
	res+=sum(root.left)
	res+=sum(root.right)
	return res

def maximum(root):
	if root==None:
		return -1000
	leftM=maximum(root.left)
	rightM=maximum(root.right)
	return max(leftM,root.data,rightM)

def minimum(root):
	if root==None:
		return 1000
	leftM=minimum(root.left)
	rightM=minimum(root.right)
	return min(leftM,root.data,rightM)
def largeCount(root,x):
	if root==None:
		return 0
	c=0
	if root.data>=x:
		c=c+1
	c+=largeCount(root.left,x)
	c+=largeCount(root.right,x)
	return c

def height(root):
	if root==None:
		return 0
	leftH=1
	rightH=1
	leftH+=height(root.left)
	rightH+=height(root.right)
	return max(leftH,rightH)

def diameter(root):
	if root==None:
		return 0
	lh=height(root.left)
	rh=height(root.right)
	c=lh+rh+1
	ld=diameter(root.left)
	rd=diameter(root.right)
	return max(c,max(ld,rd))

def depth(root,k):
	if root==None:
		return
	if k==0:
		print(root.data)
	depth(root.left,k-1)
	depth(root.right,k-1)
def search(root,x):
	if root==None:
		return False
	if root.data==x:
		return True
	l= search(root.left,x)
	r= search(root.right,x)
	return l or r
def sibling(root):
	if root==None:
		return
	if (root.left!=None and root.right==None):
		print(root.left.data)
	elif (root.left==None and root.right!=None):
		print(root.right.data)
	sibling(root.left)
	sibling(root.right)

def rep_with_Depth(root,level=0):
	if root==None:
		return 
	root.data=level
	rep_with_Depth(root.left,level+1)
	rep_with_Depth(root.right,level+1)
	return root

def removeLeaf(root):
	if root==None:
		return
	if (root.right==None and root.left==None):
		return None
	root.left=removeLeaf(root.left)
	root.right=removeLeaf(root.right)
	return root

def PrRev(root):
	if root==None:
		return None
	temp=root.left
	root.left=root.right
	root.right=temp
	PrRev(root.left)
	PrRev(root.right)
	return root

def is_balanced(root):
	if root==None:
		return False
	leftH=height(root.left)
	rightH=height(root.right)
	if (leftH-rightH==0):
		return True
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

def Create_duplicate(root):
	if root==None:
		return None
	leftN=BinaryTreeNode(root.data)
	leftN.left=root.left
	root.left=leftN
	Create_duplicate(leftN.left)
	Create_duplicate(leftN.right)
	return root

def path_sum_to_root(root,sum,sumSoFar,path):
	if root==None:
		return
	sumSoFar+=root.data
	path.append(root.data)
	if sumSoFar==sum:
		for i in range(len(path)):
			print(path[i],end=' ')
		print()
	if root.left!=None:
		path_sum_to_root(root.left,sum,sumSoFar,path)
	if root.left!=None:
		path_sum_to_root(root.right,sum,sumSoFar,path)
	path.pop()

def root_to_node(root,path):
	if root==None:
		return
	path.append(root.data)
	if(root.left==None and root.right==None):
		for i in range(len(path)):
			print(path[i],end=' ')
		print()
	if root.left!=None:
		root_to_node(root.left,path)
	if root.right!=None:
		root_to_node(root.right,path)
	path.pop()

###########################################################################################################
##############BSTBSTBSTBSTBSTBSTBSTBST#####################################################################
def search_BST(root,k):
	if root==None:
		return False
	if root.data==k:
		return True
	if root.data>k:
		return search_BST(root.left,k)
	if root.data<k:
		return search_BST(root.right,k)

def ranges(root,k1,k2):
	if root==None:
		return  
	if (root.data>k1 and root.data<k2):
		print(root.data)
	
	ranges(root.left,k1,k2)
	ranges(root.right,k1,k2)

def constr(li):
	if len(li)==0:
		return None
	
	mid=len(li)//2
	root=BinaryTreeNode(li[mid])
	
	leftSubTree=constr(li[0:mid])
	rightSubTree=constr(li[mid+1:])
	root.left=leftSubTree
	root.right=rightSubTree
	return root

def isBst(root):
	if root==None:
		return False
	leftM=maximum(root.left)
	rightM=minimum(root.right)
	if (root.data>leftM and root.data<rightM):
		return True
	lc= isBst(root.left)
	rc= isBst(root.right)
	return lc and rc

###########################################################################################################
##############GENERICGENERICGENERIC##########################TREESTREESTREESS##############################

class GenericTrees:
	def __init__(self,data):
		self.data=data
		self.children=list()

def inp_Generic():
	rootD=int(input("value:"))
	if rootD==-1:
		return None
	root=GenericTrees(rootD)
	n=int(input("how many children:"))
	for x in range(n):
		child=inp_Generic()
		root.children.append(child)
	return root
def pr_Generic(root):
	print(root.data)
	for x in root.children:
		pr_Generic(x)

def counter(root):
	if root==None:
		return 0
	c=1
	for i in root.children:
		c+=counter(i)
	return c

def add(root):
	sum=0
	sum+=root.data
	for i in root.children:
		sum+=add(i)
	return sum

def largest(root):
	large=-1000
	if large<root.data:
		large=root.data
	for i in root.children:
		t=largest(i)
		if large<t:
			large=t
	return large

def heightt(root):
	ans=1
	for i in root.children:
		res=1+height(i)
		ans=max(ans,res)
	return ans

def find(root,x):
	if root==None:
		return False
	if root.data==x:
		return True
	for i in root.children:
		if find(i,x):
			return True	

def leaf(root):
	c=0
	if not root.children:
		c=1
	for i in root.children:
		if leaf(i):
			c+=leaf(i)
	return c
root=inp_Generic()
print(leaf(root))



















