class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

def inp():
	head=None
	li=[int(x) for x in input().split()]
	for val in li:
		if val == -1:
			break
		newnode=Node(val)
		if head is None:
			head=newnode
			tail=head
		else:
			tail.next=newnode
			tail=newnode

	return head
def pr(head):
	while(head is not None):
		print(str(head.data) + "->",end="")
		head=head.next
	print("None")
	return
def eao(head):
	curr=head
	fhead1=None
	ftail1=None
	fhead2=None
	ftail2=None
	while curr:
		if(curr.data%2==0):
			if(fhead1==None):
				fhead1=curr
				ftail1=curr
			else:
				ftail1.next=curr
				ftail1=curr
		#curr=curr.next

		if(curr.data%2!=0):
			if(fhead2==None):
				fhead2=curr
				ftail2=curr
			else:
				ftail2.next=curr
				ftail2=curr
		curr=curr.next

		
	ftail1.next=fhead2
	head=fhead1
	while(head is not None):
		print(str(head.data) + "->",end="")
		head=head.next
	print("None")

head=inp()
eao(head)