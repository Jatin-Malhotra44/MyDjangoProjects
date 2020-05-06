class Edge:
	def __init__(self,src,dest,wt):
		self.src=src
		self.dest=dest
		self.wt=wt
li=[int(el) for el in input().split()]
nv=li[0]
ne=li[1]
edges=[]

def getParent(v,Parent):
	if v==Parent[v]:
		return v
	return getParent(Parent[v],Parent)

def Kruskal(edges,nv):
	Parent=[i for i in range(nv)]
	edges=sorted(edges,key=lambda edge:edge.wt)
	count=0
	output=[]
	i=0
	while(count<nv-1):
		currEdge=edges[i]

		srcParent=getParent(currEdge.src,Parent)
		destParent=getParent(currEdge.dest,Parent)

		if srcParent!=destParent:
			output.append(currEdge)
			count+=1
			Parent[srcParent]=destParent
		i+=1
	return output

for i in range(ne):
	curr_inp=[int(el) for el in input().split()]
	src=curr_inp[0]
	dest=curr_inp[1]
	wt=curr_inp[2]
	edge=Edge(src,dest,wt)
	edges.append(edge)
output=Kruskal(edges,nv)
for edge in output:
	if edge.src<edge.dest:
		print(str(edge.src)+" "+str(edge.dest)+" "+str(edge.wt))
	else:
		print(str(edge.dest)+" "+str(edge.src)+" "+str(edge.wt))
		
















