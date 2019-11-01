 question
  
    push(x) ## Push element x to the back of queue.
    pop() ## Removes the element from in front of queue.
    peek() ## Get the front element.
    empty() ## Return whether the queue is empty.
  
 answer
    
    class MyQueue:

    def __init__(self):
        self.items =[]
    def push(self, item):
        self.items.append(item)      
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def empty(self):
        if len(self.items)==0:
            return True
        else:
            return False

    
question
   
    push(x) ## Push element x onto stack.
    pop() ## Removes the element on top of the stack.
    top() ## Get the top element.
    getMin() ## Retrieve the minimum element in the stack.
    
answer
  
    class MinStack:

    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)     
    def pop(self): 
        return self.items.pop()        
    def top(self):
        if len(self.items)!=0:
            return self.items[len(self.items)-1]       
    def getMin(self):
        return min(self.items)
