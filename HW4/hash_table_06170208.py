from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        h=MD5.new()
        h.update(key.encode("utf-8"))
        h=h.hexdigest()
        x=int(h,16)
        y=x%self.capacity
        node=self.data[y]
        
        a=ListNode(h)
        a.next=self.data[y]
        self.data[y]=a
        
     
    def remove(self, key):
        h=MD5.new()
        h.update(key.encode("utf-8"))
        h=h.hexdigest()
        x=int(h,16)
        y=x%self.capacity
        node=self.data[y]
        print(y)
        
        c=self.data[y]        
        
        if c.next == None:
            if c.val==h:
                self.data[y]=None
          
        while c.next:
            print(5)
            if c.next.val==h:
                print(2)
                c.next = c.next.next
            if c.next.val!=h:
                print(3)
                c=c.next

    
    def contains(self, key):
        h=MD5.new()
        h.update(key.encode("utf-8"))
        h=h.hexdigest()
        x=int(h,16)
        y=x%self.capacity
        node=self.data[y]
        
        c=ListNode(h)
        d=self.data[y]
        
        while d:
            if c.val==d.val:
                return True
                break
            else:
                d=d.next
        while d is None:
            return False

