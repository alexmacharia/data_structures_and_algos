class Node:

    def __init__(self, data):
        """
        Initialize the class values of data and next
        """
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        """
        Add a node to the end of the linked list
        """
        if not self.head:
            self.head = Node(data)

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    def prepend(self, data):
        """
        Add node at the begining of linked list
        """
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def delete(self, data):
        """
        Delete node with value in data
        """
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next.data != data:
            current = current.next
        current.next = current.next.next
