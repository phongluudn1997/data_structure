# First In, First Out FIFO

class Queue:
    def __init__(self):
        self.queue = []

    def peek(self):
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)
