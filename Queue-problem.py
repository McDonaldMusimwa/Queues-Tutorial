class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    """
    Problem 1 
    Add items to the queue
    """
    def enqueue(self, item):
        pass



    """
    Problem 2
    Remove items from the queue
    """
    def dequeue(self):
        pass

    """
    Problem 3
    display size of the queue
    """
    def size(self):
        pass

    def display(self):
        print("Queue:", self.items)


# Example usage:

# Create a queue
queue = Queue()

# Enqueue elements
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

# Display the queue
queue.display()  # Output: Queue: [10, 20, 30, 40]

# Dequeue elements
print(queue.dequeue())  # Output: 10
print(queue.dequeue())  # Output: 20

# Display the updated queue
queue.display()  # Output: Queue: [30, 40]
