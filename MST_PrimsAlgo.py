import queue
import sys
class Graph:
	def __init__(self,nVertices):
		self.nVertices=nVertices
		self.adjMatrix=[[0 for i in range(nVertices)] for j in range(nVertices)]
	
	def getMinVertex(self,visited,Weight):
		min_vertex=-1
		for i in range(self.nVertices):
			if(visited[i] is False and (min_vertex==-1 or Weight[min_vertex]>Weight[i])):
				min_vertex=i
		return min_vertex

	def addEdge(self,v1,v2,wt):
			self.adjMatrix[v1][v2]=wt
			self.adjMatrix[v2][v1]=wt

	def Prims(self):
		visited=[False for i in range(self.nVertices)]
		Parent=[-1 for i in range(self.nVertices)]
		Weight=[sys.maxsize for i in range(self.nVertices)]
		Weight[0]=0
		for i in range(self.nVertices-1):
			min_vertex=self.getMinVertex(visited,Weight)
			visited[min_vertex]=True
			
			#explore neighbour of min vertex which id not visited
			# and update the weight corresponding to them

			for j in range(self.nVertices):
				if(self.adjMatrix[min_vertex][j]>0 and visited[j] is False):
					if(Weight[j]>self.adjMatrix[min_vertex][j]):
						Weight[j]=self.adjMatrix[min_vertex][j]
						Parent[j]=min_vertex

		for i in range(1,self.nVertices):
			if i<Parent[i]:
				print(str(i)+" "+str(Parent[i])+" "+str(Weight[i]))
			else:
				print(str(Parent[i])+" "+str(i)+" "+str(Weight[i]))
				

li=[int(el) for el in input().split()]
nv=li[0]
ne=li[1]
g = Graph(nv)
for i in range(ne):
	curr_inp=[int(el) for el in input().split()]
	g.addEdge(curr_inp[0], curr_inp[1], curr_inp[2])

g.Prims()
