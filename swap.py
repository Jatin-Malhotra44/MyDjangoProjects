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

def swap(head):
	c1=0
	c2=0
	cur1=head
	prev1=None
	
	cur2=head
	prev2=None
	
	n=int(input())
	m=int(input())
	
	while(c1<n):
		prev1=cur1
		cur1=cur1.next
		c1+=1
		
	while(c2<m):
		prev2=cur2
		cur2=cur2.next
		c2+=1
	t=cur2.next		
	if(cur1==prev2 and prev1!=None):
		prev1.next=cur2
		cur2.next=cur1
		cur1.next=t
	
	elif(prev1==None):
		cur2.next=cur1
		cur1.next=t
		head=cur2

	else:
		prev1.next=cur2
		cur2.next=cur1.next
		prev2.next=cur1
		cur1.next=t

	while(head is not None):
		print(str(head.data) + "->",end="")
		head=head.next
	print("None")
	return
	
head=inp()
swap(head)