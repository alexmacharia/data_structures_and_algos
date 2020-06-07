class Node:
    '''Binary Tree implementation
    '''
    def __init__(self, data):
        '''Initialize node instance with value and empty pointers
           for left and right nodes
        '''
        self.value = data
        self.left = None
        self.right = None

    def insert(self, data):
        '''Insert value into tree
        '''
        if data <= self.value:
            if not self.left:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def contains(self, data):
        '''Check if tree contains value. Returns True if exists
           and False if not
        '''
        if data == self.value:
            return True
        else:
            if data < self.value:
                if not self.left:
                    return False
                else:
                    return self.left.contains(data)
            else:
                if not self.right:
                    return False
                else:
                    return self.right.contains(data)

    def print_left_right(self):
        '''Prints the values of the tree from left to right
        '''
        if self.left is not None:
            self.left.print_inplace()
        print(self.value)
        if self.right is not None:
            self.right.print_inplace()

    def print_right_left(self):
        '''Prints the values of the tree from right to left
        '''
        if self.right is not None:
            self.right.print_right_left()
        print(self.value)
        if self.left is not None:
            self.left.print_right_left()
