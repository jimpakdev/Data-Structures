from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  def enqueue(self, value):
    self.size += 1
    self.storage.add_to_tail(value)
  
  def dequeue(self):
    if self.size > 0:
      self.size -= 1
      value = self.storage.remove_from_head()
      return value
    else:
      return None

  def len(self):
    return self.size
