class Node:
	
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None

class Tree:

	def __init__(self):
		self.root = None

	def insert(self,key):
		if (self.root == None):
			self.root = Node(key)
			return

		current = self.root
		while(current):
			if (key > current.data):
				if (current.right is not None):
					current  = current.right
				else:
					current.right = Node(key)
					return
			else:
				if (current.left is not None):
					current = current.left
				else:
					current.left = Node(key)
					return

	def level_order(self,node):
		if node is Node:
			return

		queue  = []
		queue.append(node)
		while (len(queue)>0):
			print queue[0].data,
			n = queue.pop(0)

			if n.left:
				queue.append(n.left)

			if n.right:
				queue.append(n.right)

if __name__ == '__main__':
	tree = Tree()
	tree.insert(4)
	tree.insert(6)
	tree.insert(3)
	tree.insert(8)
	tree.insert(1)
	tree.level_order(tree.root)