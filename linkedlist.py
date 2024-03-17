"""
ArrayLists: Store items in continous memory e.g.
Index: 0 1 2 3 4 5 6
Items: A B C E F G H

Problem: If we want to inser D at index 3 we need to shift the index to store D in that memory location.
Another Problem: Need to shift when data is deleted to close the gap.
"""

"""
LinkedLists: Solves problems by having pointers that point to data, so pointers can be reassigned when memory is deleted.

A node that will have data e.g. "A", an address e.g. "101", and a pointer. The data is the element of interest, the address is the location in memeory the data is stored, 
and the pointer points from the address to the data to access the element in memeory. The benefit of linked lists is that the data can be stored anywhere in memeory. When
a element is removed or added instead of shifting the entire list we reassign pointers.

Problem with LinkedList: Because the items are stored randomly, you need to search the list to find specific items which in on O(n) time where a array is O(1)
"""

"""
Singly vs Doubly Linked List

Singly: One address one pointer, can only go forward
Pro: Less memory then doubly
Con: Go only move head to tail

Doubly: Two addresses, two pointers, can move forward and backwards
Pro: Can move head to tail and tail to head
Con: More memory
"""

from queue import Queue

# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the LinkedList class inheriting from Queue
class LinkedList(Queue):
    def __init__(self):
        super().__init__()

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            removed_item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return removed_item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.front.data

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count