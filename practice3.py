import queue
class Graph:
	def __init__(self,nVert):
		self.nVert=nVert
		self.adjMatrix=[[0 for i in range(nVert)]for j in range(nVert)]

	def addEdge(self,sv,ev):
		self.adjMatrix[sv][ev]=1
		self.adjMatrix[ev][sv]=1

	def remEdge(self,sv,ev):
		if self.adjMatrix[sv][sv]==0:
			return 
		else:
			self.adjMatrix[sv][ev]=1
			self.adjMatrix[ev][sv]=1

	def ContainsEdge(self,sv,ev):
		if self.adjMatrix[sv][ev]==1:
			return True
		else:
			return False
	def __DFS(self,sv,visited):
		print(sv)
		visited[sv]=True
		for i in range(self.nVert):
			if(self.adjMatrix[sv][i]==1 and visited[i] is False):
				self.__DFS(i,visited)

	def DFS(self,sv):
		visited=[False for i in range(self.nVert)]
		self.__DFS(sv,visited)	

	def BFS(self,sv):
		q=queue.Queue()
		q.put(sv)
		visited=[False for i in range(self.nVert)]
		visited[sv]=True
		while not q.empty():
			u=q.get()
			print(u)
			for i in range(self.nVert):
				if(self.adjMatrix[u][i]==1 and visited[i] is False):
					q.put(i)
					visited[i]=True

	def __Get_Path_DFS(self,sv,ev,visited):
		ans=[]
		if sv==ev:
			ans.append(sv)
			return ans
		visited[sv]=True
		for i in range(self.nVert):
			if(self.adjMatrix[sv][i]==1 and visited[i] is False):
				ans=self.__Get_Path_DFS(i,ev,visited)
				if ans: 
					ans.append(sv)
					return ans
		return None
	def Get_Path_DFS(self,sv,ev):
		visited=[False for i in range(self.nVert)]
		return self.__Get_Path_DFS(sv,ev,visited)

g=Graph(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,4)
print(g.Get_Path_DFS(0,4))