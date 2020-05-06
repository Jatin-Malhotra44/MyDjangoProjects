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

def merge(head1,head2):
	fhead=None
	ftail=None
	if(head1.data<head2.data):
		fhead=head1
		ftail=head1
		head1=head1.next
	else:
		fhead=head2
		ftail=head2
		head2=head2.next
	while (head1 is not None and head2 is not None):
		if(head1.data<head2.data):
			ftail.next=head1
			ftail=ftail.next
			head1=head1.next
		else:
			ftail.next=head2
			ftail=ftail.next
			head2=head2.next
	if(head1 is not None):
		ftail.next=head1
	if(head2 is not None):
		ftail.next=head2
	head=fhead
	while(head is not None):
		print(str(head.data) + "->",end="")
		head=head.next
	print("None")
	return


head1=inp()
head2=inp()
merge(head1,head2)