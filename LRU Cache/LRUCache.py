from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False) 
        else:
            self.cache.move_to_end(key) 
        
        self.cache[key] = value


lRUCache = LRUCache(2);
print(lRUCache.put(1, 1)) 
print(lRUCache.put(2, 2))
print(lRUCache.get(1))
print(lRUCache.put(3,3)) 
print(lRUCache.get(2))
print(lRUCache.put(4, 4)) 
print(lRUCache.get(1)) 
print(lRUCache.get(3))
print(lRUCache.get(4))