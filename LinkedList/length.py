class Node:
	def __init__(self,data = None,next = None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	#Iterartive solution
	def LengthList(self):
		count = 0
		temp = self.head
		while temp is not None:
			count += 1
			temp = temp.next
		return count

	#Recursive solution
	def recLengthrec(self, node):
		if (not node):
			return 0
		else:
			return 1 + self.recLengthrec(node.next)

	#Wrapper around recLengthrec() function
	def recLength(self):
		return self.recLengthrec(self.head)


if __name__=='__main__':
	#Creting a linkedlist and nodes
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	#connecting them
	llist.head.next = second
	second.next = third

	#List Traversal
	print (llist.LengthList())
	print (llist.recLength())