from doubly_linked_list import DoublyLinkedList

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  # max number of nodes it can hold
  # current number of nodes being held
  # DLL (import this)
  # storage dict 
  def __init__(self, limit=10):    
    self.size = 0    
    self.storage = DoublyLinkedList()    
    self.cache = LRUCache()              
  

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  # returns value associated with given key
  # returns None if key does not exist
  # move key-value pair to end of the order

  def get(self, key):
    if self.key in self.storage:                     # check if the key exists
      value = self.storage.node.value                # if yes, return its value
      self.storage.move_to_end(self.storage.node)    # and move the pair to the end
      return value
    else:                                            # if key does not exist, return None
      return None

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    pass
