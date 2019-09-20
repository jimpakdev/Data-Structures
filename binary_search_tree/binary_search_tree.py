import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

# Questions:
# Only ints? 
# Negative numbers?

# Observations
# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent


class BinarySearchTree:
  def __init__(self, value): # We're just using value, so key is value
    self.value = value
    self.left = None
    self.right = None
    self.queue = Queue()
    self.stack = Stack()

  # * `insert` adds the input value to the binary search tree, adhering to the
  # rules of the ordering of elements in a binary search tree.
  # Need to traverse to find spot to insert
  def insert(self, value):

    if self.value >= value:
      if self.left == None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)

    else:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

    

  # * `contains` searches the binary search tree for the input value, 
  # returning a boolean indicating whether the value exists in the tree or not.
  # Start from root and traverse the tree
  # We can stop at the first instance of a value
  # We know it's not found if we get to a node that doesn't have children
  def contains(self, target):
    if self.value == target:
      return True
    
    elif self.value > target:
      if self.right == None:
        return False
      else:
        return self.right.contains(target)
    
    else:
      if self.left == None:
        return False
      else:
        return self.right.contains(target)


  # * `get_max` returns the maximum value in the binary search tree.
  def get_max(self):
    current = self

    while current.right:
      current = current.right
    return current.value
      
  # * `for_each` performs a traversal of _every_ node in the tree, executing
  # the passed-in callback function on each tree node value. There is a myriad of ways to
  # perform tree traversal; in this case any of them should work. 
  def for_each(self, cb):
    current = self 
    cb(current.value)    #### perform callback on root first

    if current.left != None:
      current.left.for_each(cb)
      
    if current.right != None:
      current.right.for_each(cb)


# DAY 2 Project -----------------------

# Print all the values in order from low to high
# Hint:  Use a recursive, depth first traversal
  def in_order_dft(self, node):
    if node:
      self.in_order_dft(node.left)
      print(node.value)
      self.in_order_dft(node.right)

# Print the value of every node, starting with the given node,
# in an iterative breadth first traversal

# Breadth first search - queue / check each level one at a time 
# create a queue
# put root in queue
# while queue is not empty
# pop first item in queue
# check left and right add to queue
# shift 
# go to head of queue and continue 
  def bft_print(self, node):
    self.queue.enqueue(node)
    
    while self.queue.size != 0:
      current = self.queue.dequeue()
      print(current.value)
      if current.left:
        self.queue.enqueue(current.left)
      if current.right:
        self.queue.enqueue(current.right)
        


# Print the value of every node, starting with the given node,
# in an iterative depth first traversal

# DFT
# create a stack
# put root in stack
# while stack is not empty
# pop first item in stack
# check root.left and put it in stack
# check root.right and put it in stack
# go to top of stack and continue
  def dft_print(self, node):
    self.stack.push(node)
    
    while self.stack.size != 0:
      current = self.stack.pop()
      print(current.value)
      if current.left:
        self.stack.push(current.left)        
      if current.right:
        self.stack.push(current.right)

    
    
# STRETCH Goals -------------------------
# Note: Research may be required

# Print In-order recursive DFT
  def pre_order_dft(self, node):
    pass

# Print Post-order recursive DFT
  def post_order_dft(self, node):
    pass
