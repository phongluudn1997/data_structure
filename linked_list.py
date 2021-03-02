"""
    LINKED LIST:
    
    Cons: Get access to element in linear time O(n) while with array is constant time O(1).
    Cause you have to walk all the way through every element to the expected element

    Adv: Insert and delete in constant time O(n)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def append(self, data):
        if head == None:
            self.head = Node(data)
            return
        current = this
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def delete_with_value(self, data):
        if self.head == None:
            return
        if self.head.data = data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data = data:
                current.next = current.next.next
                return
            current = current.next
