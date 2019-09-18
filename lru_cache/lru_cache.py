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
    self.limit = limit 
    self.cache = {}         
  

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
    if key in self.cache:                         
      val = self.cache[key]   
      self.cache.pop(key)  
      self.cache[key] = val                      # check if the key exists
      return self.cache[key]                           # if yes, return its value
                                                       # and move the pair to the end
    else:                                              # if key does not exist, return None
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
    # check if it is already in cache, overwrite with new value
    # if not in the cache, add to the end 
    # if cache is at max, remove oldest entry (the head)
    if len(self.cache) == self.limit:
      self.cache.pop(list(self.cache)[0])
    self.cache[key] = value  
    
    
      

        

    

