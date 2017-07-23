class Node:
	def __init__(self, data=None, next = None):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	#function to print all the nodes in a list: List Traversal
	def printList(self):
		temp = self.head
		while (temp):
			print temp.data,
			temp = temp.next

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
	llist.printList()