class Node:
	def __init__(self,data=None):
		self.data = data
		self.right = None
		self.left = None	


class Tree:
	
	def __init__(self,data=None):
		self.root = None

	def insert_node(self,data):
		if self.root == None:
			self.root = Node(data)
		else:
			current = self.root
			while 1:
				if data < current.data:
					if current.left:
						current = current.left
					else:
						current.left = Node(data)
						break
				elif data > current.data:
					if current.right:
						current = current.right
					else:
						current.right = Node(data)
						break
				else:
					break

	def search(self,root,key):
		if key == root.data:
			return root
		if key > root.data and root.right is not None:
				return self.search(root.right,key)
		if key < root.data and root.left is not None:
				return self.search(root.left,key)
		return "not found"
	
	def preorder_trav(self,root):
		if root is not None:
			print root.data
			self.preorder_trav(root.left)
			self.preorder_trav(root.right)

	def inorder_trav(self,root):
		if root is not None:
			self.inorder_trav(root.left)
			print root.data
			self.inorder_trav(root.right)

	def postorder_trav(self,root):
		if root is not None:
			self.postorder_trav(root.left)
			self.postorder_trav(root.right)
			print root.data




if __name__ == '__main__':
	t = Tree()
	t.insert_node(20)
	t.insert_node(30)
	t.insert_node(15)
	t.insert_node(25)



