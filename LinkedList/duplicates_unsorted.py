''' Removes Duplicates from an unsorted LinkedList 
	Using a dictionary 'seen' which keeps track of 
	data(key) and nodes(values) which is already seen.'''


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
		seen = {}
		current = self.head
		prev = None
		while(current):
			if current.data not in seen:
				seen[current.data] = current
				prev = current
			else:
				prev.next = current.next
			current = prev.next	


if __name__ == '__main__':
	llist = LinkedList()
	llist.insert(4)
	llist.insert(4)
	llist.insert(4)
	llist.insert(2)
	llist.insert(4)
	llist.insert(4)
	llist.print_list()
	print("changed")
	llist.remove_duplicates()
	llist.print_list()