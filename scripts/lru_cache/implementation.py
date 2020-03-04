class LRUCache:
    hsmap=dict()
    capacity=count=0
    head=tail=None
    lru=[]
        
    def __init__(self,cap):
        self.capacity = cap
        
    #This method works in O(1)
    def get(self, key):
        found = self.hsmap.get(key, -1)
        if found != -1:
            self.lru.remove(key)
            self.lru.insert(0, key)
        
        return found
        
        
    #This method works in O(1)   
    def set(self, key, value):
        lru_exists = self.exists(key)
        if lru_exists:
            # no encontro
            self.lru.remove(key)
            del self.hsmap[key]
        elif self.capacity == len(self.lru):
            ex = self.lru.pop()
            del self.hsmap[ex]
            
        self.lru.insert(0, key)
        self.hsmap[key] = value
            
            
    def exists(self, key):
        return key in self.lru

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry = int(input())  #number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list
        
        lru = LRUCache(cap)
        
       
        i = 0
        q = 1
        while q <= qry:
            qtyp = a[i]
            
            if qtyp == 'SET':
                lru.set(int(a[i+1]), int(a[i+2]))
                i += 3
            elif qtyp == 'GET':
                print(lru.get(int(a[i+1])), end=' ')
                i += 2
            q += 1
        print()