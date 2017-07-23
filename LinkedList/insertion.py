class LinkedList:
	def __init__(self):
		self.head = None

	def front_insertion(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		temp = self.head
		while (temp):
			print temp.data,
			temp = temp.next
	
	def insertafter(self, prev_node, new_data):
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def last_insertion(self, new_data):
		new_node = Node(new_data)
		#if list is empty, head will point to new node
		if self.head is None:
			self.head = new_node
			return

		temp = self.head
		while (temp.next):
			temp = temp.next
		temp.next = new_node

class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


if __name__ == '__main__':
	#Creting a linkedlist and nodes
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	#connecting them
	llist.head.next = second
	second.next = third

	# List Traversal
	llist.printList()

	#adding node at front
	llist.front_insertion(4)	

	# List Traversal
	llist.printList()	

	#inserting after node2
	llist.insertafter(second,5)

	llist.last_insertion(6)
	# List Traversal
	llist.printList()

	
