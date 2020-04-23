import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # recursive inner function to find correct location
        # if empty new = head
        # if new < node.value => !left ? create left : insert left
        # if >= => !right ? create right : insert right
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if node none => false
        # 
        if self.value == target:
            return True
        if target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
            if self.right is None:
                return self.value
            else:
                return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
            cb(self.value)
            if self.left is not None:
                self.left.for_each(cb)
            if self.right is not None:
                self.right.for_each(cb)

            


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
        # DFS => begin with the root node then transver its children 
    def in_order_print(self, node):
        if node is None:
            return
        if self.left is not None:
            self.left.in_order_print(self.left)
            
        print(self.value)

        if self.right is not None:
            self.right.in_order_print(self.right)
            



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
        # BFS starts at root , explors neighbour nodes at present depth BEFORE moving on
    def bft_print(self, node):
        ## tree hight counter
        ## queue print data
        q = []
        q.append(node)
        while len(q):
            curr_node = q.pop(0)
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
            print(curr_node.value)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(self.value)
        if self.left is not None:
            self.left.bft_print()
        elif self.right is not None:
            self.right,bft_print()

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
