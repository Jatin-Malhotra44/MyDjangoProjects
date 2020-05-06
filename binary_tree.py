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
def count(root):
	if root ==None:
		return 0

	lN=count(root.left)
	rN=count(root.right)
	return 1+lN+rN
def sum(root):
	if root==None:
		return 0
	result=root.data
	result+=sum(root.left)
	result+=sum(root.right)
	return result
def largest(root):
	if root==None:
		return -1
	ll=largest(root.left)
	rl=largest(root.right)
	return max(ll,rl,root.data)
def largCount(root):
	if root==None:
		return 0
	result=0
	if root.data>2:
		result+=1
	result+=largCount(root.left)
	result+=largCount(root.right)
	return result 
def height(root):
	if root==None:
		return 0
	lh=1
	rh=1
	lh+=height(root.left)
	rh+=height(root.right)
	return max(lh,rh)
def depth(root,k):
	if root==None:
		return
	if k==0:
		print(root.data)
		return
	depth(root.left,k-1)
	depth(root.right,k-1)
def repDepth(root,level=0):
	if root==None:
		return
	root.data=level
	repDepth(root.left,level+1)
	repDepth(root.right,level+1)
def search(root):
	if root==None:
		return False
	if root.data==2:
		return True
	l=search(root.left)
	s=search(root.right)
	return l or s
def sibling(root):
	if root==None:
		return None
	if (root.left==None and root.right!=None):
		print(root.right.data)
	elif(root.right==None and root.left!=None):
		print(root.left.data)
	sibling(root.left)
	sibling(root.right)
def removeLeaf(root):
	if root==None:
		return None
	if (root.left==None and root.right==None):	
		root.data=-1
	removeLeaf(root.left)
	removeLeaf(root.right)
def mirror(root):
	if root==None:
		return 
#	if root.left==None and root.right==None:
#		return root
	t=root.left
	root.left=root.right
	root.right=t
	mirror(root.left)
	mirror(root.right)
	return root
def balanced(root):
	if root==None:
		return 0
	lh=1
	rh=1
	lh+=balanced(root.left)
	rh+=balanced(root.right)
	if lh==rh:
		return True
	else:
		return False
def diameter(root):
	if root==None:
		return 0
	lh=height(root.left)
	rh=height(root.right)
	c=lh+rh+1
	ld=diameter(root.left)
	rd=diameter(root.right)
	return max(c,max(ld,rd))

INT_MAX=1000
def findMax(root): 
      
    # Base case  
    if (root == None):  
        return -999999999999
  
    res = root.data 
    lres = findMax(root.left)  
    rres = findMax(root.right)  
    if (lres > res): 
        res = lres  
    if (rres > res):  
        res = rres  
    return res 

def path_sum_to_root(root,sum_so_far,sum,path):
	if root==None:
		return
	sum_so_far+=root.data
	path.append(root.data)
	if(sum_so_far==sum):
		for i in range(len(path)):
			print(path[i],end=" ")
		print()
	if root.left!=None:
		path_sum_to_root(root.left,sum_so_far,sum,path)
	if root.right!=None:
		path_sum_to_root(root.right,sum_so_far,sum,path)

	path.pop()
def printPaths(root, sum): 
  
    path = [] 
    path_sum_to_root(root, sum, 0, path)  

def printkDistanceNodeDown(root, k): 
      
    # Base Case 
    if root is None or k< 0 : 
        return 
      
    # If we reach a k distant node, print it 
    if k == 0 : 
        print(root.data)  
        return 
      
    # Recur for left and right subtee 
    printkDistanceNodeDown(root.left, k-1) 
    printkDistanceNodeDown(root.right, k-1)
     
root=inp()
(removeLeaf(root))