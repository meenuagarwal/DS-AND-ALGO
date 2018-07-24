# SINGLY LINKED LIST

Every node in a singly linked list consists of a key and a next pointer pointing to next node in the list. It starts with a head node pointing to the beginning of list and it may or may not have a tail pointer pointing to the end node.
## OPERATIONS
- PushFront(Key) - Add node with given key to front in O(1) time
- TopFront() - Return the front key in O(1) time
- PopFront() - Remove the front item from list in O(1) time
- PushBack(Key) - Add node with given key at the end in O(n) time with no tail pointer and O(1) time with tail pointer
- TopBack() - Return the last key in O(n) time with no tail pointer and O(1) time with tail pointer
- PopBack() - Remove the last item in O(n) time
- AddBefore(Node,key) - Add key before given Node in O(n) time
- AddAfter(Node,key) - Add key after given Node in O(n) time
- Boolean Find(Key) - Check if given key exists in the list in O(n) time
- Erase(Key) - Remove node with given key from the list in O(n) time
- Boolean IsEmpty() - Check if list is empty in O(1) time

All of these functions are implemented in singly_linked_list.py file.

# DOUBLY LINKED LIST

Every node in doubly linked list contains an extra pointer pointing to previous element in the list along with a key and next pointer.
## OPERATIONS
All operations are same as singly linked list except the time taken changes for two operations. Now since we have a previous pointer too, it takes O(1) time for
- AddBefore(Node,key)
- PopBack()

It is implemented in doubly_linked_list.py file.
