# STACK

It is an abstarct data type which can be implemented using both array and linked list. It can be visualised as a stack of books. Each element can be considered as a book and you can insert elements on top of previous one. It is also called LIFO(Last In First out) as the last element that was inserted is the first elemnet out. Most common uses of stacks include check for paranthesis balancing in compilers or the "undo" operation.

## OPERATIONS
- Push(Key) - Push element to the stack
- Top() - Returns the top(recently added) element
- Pop() - Pops the top(recently added) element
- Boolean IsEmpty() - Check if stack is empty

# QUEUES

It is also an abstract data type like stacks but as the name suggests they are similar to waiting in a line. So you can add elements to the queue and first element that was inserted is the first element out. Hence they are also called FIFO(First In First Out). They can also be implemented using arrays or linked lists. They are used in scheduling process due to the first-come-first-serve principle.

## OPERATIONS
- Enqueue(Key) - Push element to the queue
- Dequeue() - Remove and returns the least recently added element
- Boolean IsEmpty() - Check if queue is empty 
