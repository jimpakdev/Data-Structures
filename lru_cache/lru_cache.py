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
    # self.limit = limit 
    # self.size = 0
    # self.cache = {}         


    # Brian's way
    self.limit = limit 
    self.size = 0
    self.storage = {}   
    self.order = DoublyLinkedList()
  

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

    # if key in self.cache:                         
    #   val = self.cache[key]   
    #   self.cache.pop(key)  
    #   self.cache[key] = val                     
    #   return self.cache[key]                                                                                
    # else:                                              
    #   return None

    # Brian's way
    if key in self.storage:
      node = self.storage[key]
      self.order.move_to_front(node)
      return node.value[1]
    else:
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

    # if len(self.cache) == self.limit and self.get(key) == None:
    #   self.cache.pop(list(self.cache)[0])
    #   self.size -= 1
    # self.cache[key] = value  
    # self.size += 1


    # Brian's way
    # If already exist, overwrite value
    if key in self.storage:
    # update dict
      node = self.storage[key]
      node.value = (key, value)
      # Mark as most recently used, put in the head of DLL
      self.order.move_to_front(node)
      return
    # If at max capacity, dump oldest - remove from tail of DLL
    if self.size == self.limit:
      del self.storage[self.order.tail.value[0]]
      self.order.remove_from_tail()
      self.size -= 1
    # Add pair to the cache - add to dict and add it to nodes/DLL
    self.order.add_to_head((key, value))
    self.storage[key] = self.order.head
    self.size += 1


    
    
      

        

    

