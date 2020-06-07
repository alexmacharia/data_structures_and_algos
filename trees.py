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

    def delete(self, data):
        '''Delete a value from the tree
        '''
        pass

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

    def print_preorder(self):
        '''Prints the values of the tree from left to right
        '''
        if self.left is not None:
            self.left.print_preorder()
        print(self.value)
        if self.right is not None:
            self.right.print_preorder()

    def print_postorder(self):
        '''Prints the values of the tree from right to left
        '''
        if self.right is not None:
            self.right.print_postorder()
        print(self.value)
        if self.left is not None:
            self.left.print_postorder()

    def print_inorder(self):
        '''Print the values of the tree from root to children
        '''
        print(self.value)
        if self.left is not None:
            self.left.print_inorder()
        if self.right is not None:
            self.right.print_inorder()
