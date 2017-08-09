class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self,data):
		if self.head == None:
			self.head = Node(data)

		else:
			current = self.head
			while(current):
				previous = current
				current = current.next

			previous.next = Node(data)

	def print_list(self):
		if self.head == None:
			print ("Empty List")

		current = self.head
		while(current):
			print current.data
			current = current.next

	def remove_duplicates(self):
		if self.head == None:
			return head
		
		current = self.head
		while(current.next):
			if (current.data == current.next.data):
				next_node = current.next
				current.next = next_node.next
			else:
				current = current.next
		


if __name__ == '__main__':
	llist = LinkedList()
	llist.insert(1)
	llist.insert(2)
	llist.insert(2)
	llist.insert(3)
	llist.print_list()
	print("changed")
	llist.remove_duplicates()
	llist.print_list()