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
	
	def Get_path_dfs_helper(self,visited,v1,v2):
		if v1==v2:
			return [v2]
		
		visited[v1]=True

		for i in range(self.nV):
			if (self.adjMatrix[v1][i]>0 and visited[i] is False):
				ans=self.Get_path_dfs_helper(visited,i,v2)
				if ans is not None:
					ans.append(v1)
					return ans
		return None

	def Get_path_dfs(self,v1,v2):
		visited=[False for i in range(self.nV)]
		return self.Get_path_dfs_helper(visited,v1,v2)

	def __IsConnected(self,sv,visited):
		q=queue.Queue()
		q.put(sv)
		c=2
		c2=self.nV
		visited[sv]=True
		while not q.empty():
			u=q.get()
			for i in range(self.nV):
				if (self.adjMatrix[u][i]==1 and visited[i] is False):
					q.put(i)
					visited[i]=True
					c=c+1
		
		for boolV in visited:
			print(visited[boolV])
			#if not boolV:
			#	return False
			#return True
		#if c==c2:
		#	return True

	def IsConnected(self,sv):
		visited=[False for i in range(self.nV)]
		return self.__IsConnected(sv,visited)

	def __Has_path_bfs(self,v1,v2,visited):
		if v1==v2:
			return True
		q=queue.Queue()
		q.put(v1)
		visited[v1]=True
		while not q.empty():
			u=q.get()
			for i in range(self.nV):
				if (self.adjMatrix[u][i]==1 and visited[i] is False):
					if i==v2:
						return True
					q.put(i)
					visited[i]=True
		return False

	def Has_path_bfs(self,v1,v2):
		visited=[False for i in range(self.nV)]
		return self.__Has_path_bfs(v1,v2,visited)

	def __getPath_bfs(self,sv,ev,visited):
		q=queue.Queue()
		mapp={}
		q.put(sv)
		visited[sv]=True
		while not q.empty():
			u=q.get()
			for i in range(self.nV):
				if (self.adjMatrix[u][i]==1 and visited[i] is False):
					mapp[i]=u
					q.put(i)
					visited[i]=True
					if i==ev:
						ans=[]
						ans.append(ev)
						value=mapp[ev]
						while value !=sv:
							ans.append(value)
							value=mapp[value]
						ans.append(value)
						return ans
	def getpath_bfs(self,sv,ev):
		visited=[False for i in range(self.nV)]
		return self.__getPath_bfs(sv,ev,visited)

	def connected(self):
		visited=[False for i in range(self.nV)]
		self.DFS()
		for boolv in visited:
			print(visited[boolv])
			#if not boolv:
			#	return False
			#return True

	def addEdge(self,v1,v2):
		self.adjMatrix[v1][v2]=1
		self.adjMatrix[v2][v1]=1

	def remEdge(self,v1,v2):
		if self.containsEdge is False:
			return
		self.adjMatrix[v1][v2]=0
		self.adjMatrix[v2][v1]=0

	def conatinsEdge(self,v1,v2):
		return True if self.adjMatrix[v1][v2] >0 else False

	def __str__(self):
		return str(self.adjMatrix)
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

g=Graph(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(1,4)
#g.addEdge(2,4)
#g.DFS()
print(g.Get_path_dfs(1,3))
#print(g.getpath_bfs(1,3))
#print(g.connected())