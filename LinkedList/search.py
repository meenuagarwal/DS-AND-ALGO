class Node:
	def __init__(self,data = None,next = None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def searchList(self,key):
		temp = self.head
		while(temp is not None):
			if (temp.data == key):
				return True
			temp = temp.next
		return False

if __name__=='__main__':
	#Creting a linkedlist and nodes
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	#connecting them
	llist.head.next = second
	second.next = third

	print (llist.searchList(5))