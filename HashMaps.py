class MapNode:
	def __init__(self,key,value):
		self.key=key
		self.value=value
		self.next=None

class Map:
	def __init__(self):
		self.BucketSize=5
		self.Buckets=[None for i in range(self.BucketSize)]
		self.count=0

	def Size_of_map(self):
		return self.count

	def GetBucketIndex(self,hc):
		return (abs(hc)%(self.BucketSize))

	def GetValue(self,key):
		hc=hash(key)
		index=self.GetBucketIndex(hc)
		head=self.Buckets[index]
		while head is not None:
			if head.key==key:
				return head.value
			head=head.next
		return None

	def loadFactor(self):
		return self.count/self.BucketSize

	def rehash(self):
		temp=self.Buckets
		self.Buckets=[None for i in range(2*self.BucketSize)]
		self.BucketSize=2*self.BucketSize
		self.count=0
		for head in temp:
			while head is not None:
				self.insert(head.key,head.value)
				head=head.next
	def insert(self,key,value):
		hc=hash(key)
		index=self.GetBucketIndex(hc)
		head=self.Buckets[index]
		while head is not None:
			if head.key==key:
				head.value=value
				return
			head=head.next
		head=self.Buckets[index]
		newn=MapNode(key,value)
		newn.next=head
		self.Buckets[index]=newn
		self.count+=1
		loadFactor=self.count/self.BucketSize
		if loadFactor>=0.7:
			self.rehash()

	def delete(self,key):
		hc=hash(key)
		index=self.GetBucketIndex(hc)
		head=self.Buckets[index]
		prev=None
		while head is not None:
			if head.key==key:
				if prev==None:
					self.Buckets[index]=head.next
				else:
					prev.next=head.next
				self.count-=1	
				return head.value
			prev=head
			head=head.next
		return None

m=Map()
for i in range(10):
	m.insert('abc'+str(i),i+1)
	print(m.loadFactor())