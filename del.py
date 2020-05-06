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
def rem(head):
	curr =head    
	while curr:
		for c1 in range(1,2):
			if curr is None:
				return
			curr=curr.next
		if curr is None:
			return
		t=curr.next
		for c2 in range(1,4):
			if t is None:
				break
			t=t.next
		curr.next=t
		curr=t
	while(head is not None):
		print(str(head.data) + "->",end="")
		head=head.next
	print("None")
	return        
        


head=inp()
rem(head)