from collections import defaultdict 
  
class Graph:
    
    def __init__(self):  
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        n=len(self.graph)
        check=[False]*n
        Q=[]
        p=[]
        Q.append(s)
        p.append(s)
        check[s]=True
    
        while check.count(False)>0:
            s=Q.pop(0)
            for i in self.graph[s]:
                if check[i] ==False:
                    Q.append(i)
                    p.append(i)
                    check[i]=True
            
        return p
        
    
    def DFS(self, s):
        n1=len(self.graph)
        check=[False]*n1
        S=[]
        p1=[]
        S.append(s)
        check[s]=True
    
        while check.count(False)>0:
            s=S.pop(-1)
            for i in self.graph[s]:
                if check[i] ==False:
                    S.append(i)
                    check[i]=True
            p1.append(s)
            if check.count(False)==0:
                s=S.pop(-1)
                p1.append(s)
            
        return p1

        
