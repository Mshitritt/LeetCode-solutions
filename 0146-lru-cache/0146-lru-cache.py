class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # pointers to head and tail of DDL
        self.lru, self.mru = Node(0, 0), Node(0, 0)
        self.lru.next, self.mru.prev = self.mru, self.lru
        # pointers to head and tail of DDL
        self.lru, self.mru = Node(0, 0), Node(0, 0)
        self.lru.next, self.mru.prev = self.mru, self.lru
    
    def remove(self, node: Node):
        # remove element from list
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
    
    def insertMRU(self, node: Node):
        # insert new item to the head
        mru = self.mru
        mru_prev = mru.prev
        mru_prev.next = node
        mru.prev = node
        node.prev = mru_prev
        node.next = mru


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.remove(self.cache[key])
            self.insertMRU(self.cache[key])
            # return the value
            return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        # insert to LRU
        self.cache[key] = Node(key, value)  #!!
        self.insertMRU(self.cache[key])

        if len(self.cache) > self.cap:
            # remove LRU item
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]

            


            
            
            


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)