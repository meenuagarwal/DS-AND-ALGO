class Node:
	def __init__(self,data,next=None):
		self.data = data
		self.next = next

class Linkedlist:
	def __init__(self,head = None):
		self.head = head

	def push(self,data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node


	def is_cycle(self):
		fast_runner = slow_runner = self.head
		while fast_runner is not None and fast_runner.next is not None:
			slow_runner = slow_runner.next
			fast_runner = fast_runner.next.next

			if fast_runner == slow_runner:
				print "Loop Detected"
				return

		print "No Loop"


if __name__ == '__main__':
	llist = Linkedlist()
	llist.push(20)
	llist.push(4)
	llist.push(15)
	llist.push(10)
	 
	# Create a loop for testing
	llist.head.next = llist.head
	llist.is_cycle()
