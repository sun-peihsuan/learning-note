from collections import defaultdict 
  
class Graph:
    
    def __init__(self):  
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
