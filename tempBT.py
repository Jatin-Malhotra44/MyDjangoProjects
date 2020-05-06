class newNode:  
  
    # Construct to create a newNode  
    def __init__(self, key):  
        self.key = key 
        self.left = None
        self.right = None
def inp():
	rootData=int(input())
	if rootData==-1:
		return None
	root=newNode(rootData)
	leftN=inp()
	rightN=inp()
	root.left=leftN
	root.right=rightN
	return root
  
# This function prints all paths 
# that have sum k  
def printPathsUtil(curr_node, sum,  
                   sum_so_far, path):  
  
    # empty node  
    if (not curr_node) : 
        return
    sum_so_far += curr_node.key 
      
    # add current node to the path  
    path.append(curr_node.key)  
  
    # prthe required path  
    if (sum_so_far == sum ) : 
      
        print("Path found:", end = " ")  
        for i in range(len(path)): 
            print(path[i], end = " ")  
  
        print()  
      
    # if left child exists  
    if (curr_node.left != None) : 
        printPathsUtil(curr_node.left, sum,  
                       sum_so_far, path)  
  
    # if right child exists  
    if (curr_node.right != None) : 
        printPathsUtil(curr_node.right, sum,  
                       sum_so_far, path) 
  
    # Remove the 	current element  
    # from the path  
    path.pop(-1)  
  
# A wrapper over printKPathUtil()  
def printPaths(root, sum): 
  
    path = [] 
    printPathsUtil(root, sum, 0, path)  
  
root=inp()  
printPaths(root, 6) 
  