class binaryTree:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
class BST:
	def __init__(self):
		self.root=None
		self.count=0
	
	def pr_helper(self,root):
		if root==None:
			return
		print(root.data)
		self.pr_helper(root.left)
		self.pr_helper(root.right)

	def pr(self):
		self.pr_helper(self.root)
	
	def insert(self,data):
		self.count+=1
		self.root = self.insert_helper(self.root,data)
	
	def insert_helper(self,root,data):
		if root==None:
			newn=binaryTree(data)
			return newn
		elif root.data<data:
			root.right=self.insert_helper(root.right,data)
			return root
		else:
			root.left=self.insert_helper(root.left,data)
			return root

	def is_present_helper(self,root,data):
		if root==None:
			return
		if root.data==data:
			return True
		elif root.data<data:
			return self.is_present_helper(root.right,data)
		elif root.data>data:
			return self.is_present_helper(root.left,data)
		else:
			return False
	
	def is_present(self,data):
		return self.is_present_helper(self.root,data)
	
	def minimum(self,root):
		if root==None:
			return 1000
		if root.left==None:
			return root.data
		return self.minimum(root.left)

	def delete_helper(self,root,data):
		if root==None:
			return False,None
		if root.data<data:
			deleted, newRight=self.delete_helper(root.right,data)
			root.right=newRight
			return deleted,root

		elif root.data>data:
			deleted, newLeft=self.delete_helper(root.left,data)
			root.left=newLeft
			return deleted,root				
		
		elif root.left==None and root.right==None:
			return True,None

		elif root.left==None:
			return True,root.right

		elif root.right==None:
			return True,root.left

		else:
			repl=self.minimum(root.right)
			root.data=repl
			deleted,newRight=self.delete_helper(root.right,repl)
			root.right=newRight
			return True,root	


	def delete(self,data):
		deleted, newroot=self.delete_helper(self.root,data)
		if deleted:
			self.count-=1
		self.root=newroot
		return deleted

	def NumNodes(self):
		return 0
b=BST()
b.insert(4)
b.insert(2)
b.insert(6)
b.insert(1)
b.insert(3)
b.insert(5)
b.insert(7)
print(b.NumNodes(
	))
b.pr()