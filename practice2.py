import queue
class Graph:
	def __init__(self,nV):
		self.nV=nV
		self.adjMatrix=[[0 for i in range(nV)] for j in range(nV)]

	def addEdge(self,v1,v2):
		self.adjMatrix[v1][v2]=1
		self.adjMatrix[v2][v1]=1

	def dfsHelper(self,sv,visited):
		print(sv)
		visited[sv]=True
		for i in range(self.nV):
			if (self.adjMatrix[sv][i]>0 and visited[i] is False):
				self.dfsHelper(i,visited)

	def DFS(self):
		visited=[False for i in range(self.nV)]
		self.dfsHelper(0,visited)

	def BFS(self):
		q=queue.Queue()
		q.put(0)
		visited=[False for i in range(self.nV)]
		visited[0]=True
		while not q.empty():
			u=q.get()
			print(u)
			for i in range(self.nV):
				if (self.adjMatrix[u][i]>0 and visited[i] is False):
					q.put(i)
					visited[i]=True
def __IsPresentBFS(self,sv,ev,visited):
	q=queue.Queue()
	d={}
	q.put(sv)
	visited[sv]=True
	while not q.empty():
		u=q.get()
		for i in range(self.nV):
			if(self.adjMatrix[u][i]==1 and visited[i] is False):
				d[i]=u
				q.put(i)
				visited[i]=True
				if i==ev:
					arr=[]
					arr.append(ev)
					val=d[ev]
					while val!=sv:
						arr.append(val)
						val=d[val]
					arr.append(val)
					return arr
def IsPresentBFS(self,sv,ev):
	visited=[False for i in range(self.nV)]
	return self.__IsPresentBFS(sv,ev,visited)

g=Graph(5)
g.addEdge(0,2)
g.addEdge(0,6)
g.addEdge(0,5)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(6,7)
g.BFS()
#print(g.IsPresentBFS(0,4))




































