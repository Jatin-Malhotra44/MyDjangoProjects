import queue
class Graph:
	def __init__(self,nV):
		self.nV=nV
		self.adjMatrix=[[0 for i in range(nV)] for j in range(nV)]

	def dfsHelper(self,sv,visited):
		print(sv)
		visited[sv]=True
		for i in range(self.nV):
			if (self.adjMatrix[sv][i]>0 and visited[i] is False):
				self.dfsHelper(i,visited)
		print(visited)	

	def DFS(self):
		visited=[False for i in range(self.nV)]
		self.dfsHelper(0,visited)

	def addEdge(self,v1,v2):
		self.adjMatrix[v1][v2]=1
		self.adjMatrix[v2][v1]=1
#####################################################################################################
	def dfs(self,sv,visited):
		visited[sv]=True
		for i in range(self.nV):
			if (self.adjMatrix[sv][i]==1 and visited[i] is False):
				self.dfs(i,visited)
				visited[i]=True
	def connected(self):
		visited=[False for i in range(self.nV)]
		self.dfs(0,visited)
		for boolV in visited:
			if not boolV:
				return False
		return True
######################################################################################################
	def __connectedComponent(self,visited,smallOutput,sv):
		visited[sv]=True
		smallOutput.append(sv)
		for i in range(self.nV):
			if(self.adjMatrix[sv][i]==True and visited[i] is False):
				self.__connectedComponent(visited,smallOutput,i)

	def connectedComponent(self):
		visited=[False for i in range(self.nV)]
		ans=[]
		for i in range(len(visited)):
			if not visited[i]:
				smallOutput=list()
				self.__connectedComponent(visited,smallOutput,i)
				ans.append(smallOutput)
		return ans
g=Graph(4)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
#g.addEdge(3,4)
#g.addEdge(4,2)
print(g.connectedComponent())
