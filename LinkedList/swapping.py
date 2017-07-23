''' Given a linked list and two keys in it, swap nodes for two given keys. 
	Nodes should be swapped by changing links. '''

class Node:
	def __init__(self,data = None,next = None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def swapping(self, key1, key2):
		xp,xc = self.findNode(key1)
		yp,yc = self.findNode(key2)

		if xp != None:
			xp.next = yc
		else:
			self.head = yc

		if (yp != None):
			yp.next = xc
		else:
			self.head = xc

		temp = xc.next
		xc.next = yc.next
		yc.next = temp


	def findNode(self,key):
		prev = None
		curr = self.head
		while curr is not None and curr.data is not key:
			prev = curr
			curr = curr.next
		return (prev,curr)


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

	llist.swapping(1,3)
	# List Traversal
	llist.printList()	



			
