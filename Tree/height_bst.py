''' The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. 
	You are given a pointer, root , pointing to the root of a binary search tree. '''

class Node:
	def __init__(self,data):
		self.right = self.left = None
		self.data = data

class Tree:
	def insert(self,root,data):
		if root == None:
			return Node(data)

		if data <= root.data:
			current = self.insert(root.left,data)
			root.left = current

		else:
			current = self.insert(root.right,data)
			root.right = current

		return root

	def getHeight(self,root):
		if root is None:
			return -1
		else:
			return (1 + max(self.getHeight(root.left),self.getHeight(root.right)))

if __name__ == '__main__':
	myTree = Tree()
	root = None
	data = [3,2,5,1,4,6,7]
	for i in xrange(len(data)):
		root = myTree.insert(root,data[i])

	height = myTree.getHeight(root)
	print height

