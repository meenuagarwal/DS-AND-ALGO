# Python program to count the number of time a given
# int occurs in a linked list
 
# Node class 
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Counts the no . of occurances of a node
    # (seach_for) in a linkded list (head)
    def count(self, search_for):
        # Dict to keep count of every int in linked list
        freq = {}
        current = self.head
        while current:
            if current.data in freq:
                freq[current.data] += 1
            else:
                freq[current.data] = 1
            current = current.next
        return freq[search_for]
       
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next
 
 
# Driver program
llist = LinkedList()
llist.push(1)
llist.push(3)
llist.push(1)
llist.push(2)
llist.push(1)
 
# Check for the count function
print "count of num is %d" %(llist.count(3))
