class Node:
    def __init__(self, data):
        self.data = data

    def insert(self, data):
        if data <= self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def contains(self, data):
        if self.data == data:
            return true
        if data < self.data:
            if self.left == None:
                return False
            else:
                return self.left.contains(data)
        if data > self.data:
            if self.right == None:
                return False
            else:
                return self.right.contains(data)

    def print_in_order(self):
        if self.left is not None:
            self.left.print_in_order()
        print(self.data)
        if self.right is not None:
            self.right.print_in_order()
