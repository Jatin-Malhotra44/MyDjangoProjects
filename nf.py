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

def counter(head):
	n=int(input())
	c=0
	while(c<n):
		head=head.next
		c=c+1	
	print(head.data)

def ins(head):
	prev=None
	curr=head
	ele=input("new element")
	newn=Node(ele)
	pos=int(input("enter pos"))
	c=0
	while(c<pos):
		prev=curr
		curr=curr.next
		c=c+1
	prev.next=newn
	newn.next=curr

def dele(head):
	prev=None
	curr=head
	ele=input("new element")
	newn=Node(ele)
	pos=int(input("enter pos"))
	c=0
	while(c<pos):
		prev=curr
		curr=curr.next
		c=c+1
	prev.next=curr.next

def search(head):
	c=0
	elem=int(input("enter value to be searched: "))
	f=True
	while(head is not None):
		if (head.data==elem):
			f=False
			break
		head=head.next
		c=c+1
	if(f==True):
		print(-1)
	else:
		print(c)
	
def append(head):
	prev=None
	curr=head
	pos=int(input("enter pos"))
	c=0
	while(c<pos):
		prev=curr
		curr=curr.next
		c=c+1
	head2=curr
	h3=head
	head=curr
	while(head2.next is not None):
		head2=head2.next
	print(head.data)
	print(prev.data)
	print(curr.data)
	print(head2.data)
	print(h3.data)
	prev.next=None
	head2.next=h3
	
	print(head2.next.data)
	while(head is not None):
		print(str(head.data) + "->",end="")
		head=head.next
	print("None")

def dup(head):
	prev=None
	curr=head
	duplicate=dict()
	while curr:
		if curr.data in duplicate:
			prev.next=curr.next
		else:
			duplicate[curr.data]=1
			prev=curr
		curr=curr.next

	while(head is not None):
		print(str(head.data) + "->",end="")
		head=head.next
	print("None")

def rev(head):
	prev=None
	curr=head
	while(curr is not None):
		n=curr.next
		curr.next=prev
		prev=curr
		curr=n
	head=prev
	while(head is not None):
		print(str(head.data) + "->",end="")
		head=head.next
	print("None")	

def palindrome(head):
	s=""
	p=head
	while p:
		s+=str(p.data)
		p=p.next
	if(s==s[::-1]):
		print("true")
	else:
		print("false")

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
		curr=curr.next

		if(curr.data%2!=0):
			if(fhead2==None):
				fhead2=curr
				ftail2=curr
			else:
				ftail2.next=curr
				ftail2=curr
		curr=curr.next

		
	#ftail2.next=fhead1
	head=fhead2
	while(head is not None):
		print(str(head.data) + "->",end="")
		head=head.next
	print("None")
head=inp()
eao(head)