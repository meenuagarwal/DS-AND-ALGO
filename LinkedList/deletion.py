class Node:
	def __init__(self,data=None, next=None):
		self.data = data
		self.next = None

class LinkedList:
	
	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		while (temp):
			print temp.data,
			temp = temp.next
	
	# Find if a particular key exist and delete it
	def deleteKey(self,key):
		# Store head node
		temp = self.head		

		# If head node itself holds the key to be deleted
		if (temp is not None): #if list is not empty
			if (temp.data == key):
				self.head = temp.next
				temp = None
				return

		# Search for the key to be deleted, keep track of the
		# previous node as we need to change 'prev.next'
		while(temp is not None): #traverse the list untill last node is reached
			if temp.data == key: #check if present node holds the key, if yes, loop breakes
				break
			prev = temp  # prev hold the value of previous node
			temp = temp.next #temp holds the value of present node
 
		# if key was not present in linked list
		if(temp == None):
			print "key not present"
			return
 
		# Unlink the node from linked list
		prev.next = temp.next 
 
		temp = None
	
	#Given a singly linked list and a position, delete a linked list node at the given position
	def delete_from_pos(self,pos):
		#stores position of current node
		index = 0
		# Store head node
		temp = self.head
		#Traverse the whole list
		while(temp is not None):
			#if present node position is required position, delete the node
			if index == pos: 
				self.deleteKey(temp.data) 
				return
			#move to next node and increment the position variable
			else:
				index += 1
				temp = temp.next
 
 		if (temp == None):
 			print "position doesn't exist"


if __name__=='__main__':
	#Creting a linkedlist and nodes
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	#connecting them
	llist.head.next = second
	second.next = third

	llist.delete_from_pos(2)

	#List Traversal
	llist.printList()