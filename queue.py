"""
Idea: First in, First Out
"""

"""
Uses: Keyboard buffer, Printer queue, LinkedLists, Priority Queues, BFS
"""

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    # Adds to tail of the queue
    def enqueue(self, item):
        self.items.append(item)

    # Removes from head of the queue
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None

    # See next element to be removed
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
            return None

    def size(self):
        return len(self.items)
    

class PriorityQueue(Queue):
    """
    Higher priority elements are served first.
    """

    def __init__(self):
        super().__init__()

    def enqueue(self, item, priority):
        # Insert the item at the correct position based on priority
        index = 0
        while index < len(self.items) and priority >= self.items[index][1]:
            index += 1
        self.items.insert(index, (item, priority))

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)[0]
        else:
            print("PriorityQueue is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0][0]
        else:
            print("PriorityQueue is empty")
            return None


def main():

    # Creates a Queue
    queue = Queue()

    # Add elements to queue
    queue.enqueue("Karen")
    queue.enqueue("Chad")
    queue.enqueue("Steve")
    queue.enqueue("Will")

    print(queue.items)

    # Removes head of queue "Karen"
    queue.dequeue()

    print(queue.items)

    # See who is on the head
    print(queue.peek())

    # Create a priority queue
    priority_queue = PriorityQueue()

    # Add to queue
    priority_queue.enqueue(3.0, 2)
    priority_queue.enqueue(2.5, 3)
    priority_queue.enqueue(2.2, 4)
    priority_queue.enqueue(1.5, 5)
    priority_queue.enqueue(4.0, 1)


    while (priority_queue.is_empty() == False):
        print(priority_queue.dequeue())
    
    
    print(priority_queue.is_empty())

if __name__ == "__main__":
    main()