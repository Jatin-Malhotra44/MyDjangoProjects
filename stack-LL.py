class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class StackLL:
	def __init__(self):
		self.head=None
		self.count=0

	def push(self,data):
		newn=Node(data)
		if self.head==None:
			self.head=newn
			self.count+=1
		else:
			newn.next=self.head
			self.head=newn
			self.count+=1
	def pop(self):
		if self.head==None:
			return 0
		ans=self.head.data
		self.head=self.head.next
		self.count-=1
		print(ans)
	def top(self):
		if self.head==None:
			return 0
		print(self.head.data)
	def is_empty(self):
		if self.head==None:
			print(True)
		print(False)
	def size(self):
		print(self.count)
s=StackLL()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.size()