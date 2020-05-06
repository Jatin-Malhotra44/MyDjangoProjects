class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def inp():
    li=[int(el) for el in input().split()]
    head=None
    for cd in li:
        if cd==-1:
            break
        else:
            newn=node(cd)
        if head==None:
            head=newn
            tail=newn
        else:
            tail.next=newn
            tail=newn
    return head
def pr(head):
    while head:
        print(head.data,end=" ")
        head=head.next
def len(head):
    c=0
    while head:
        c=c+1
        head=head.next
    return c
def rem(head,m,n):
    c1=0
    c2=0
    prev=None 
    curr1=head
    if(head is None ):
        return head
    while(curr1 is not None and c1<m):
        prev=curr1
        curr1=curr1.next
        c1+=1
    if(curr1 is None ):
        return head
    curr2=curr1
    while(curr2 is not None and c2<n):
        curr2=curr2.next
        c2+=1
    prev.next=rem(curr2,m,n)
    return head
head=inp()
m=int(input())
n=int(input())
head=rem(head,m,n)
pr(head)