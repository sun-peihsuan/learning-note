from collections import defaultdict 

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.list1=[]
        self.list2=[]
    
    def addEdge(self,u,v,w): 
        
        self.list1.append(w)
        self.list2.append(u)
        self.list2.append(v)
        return self.list1,self.list2
   
    def Dijkstra(self, s): 
        
        n=len(self.graph)
        p=[False]*n
        check=[False]*n
        check2=[False]*n
        p[s]=0
        check[s]=True
        dict={}
        while check2:
            q=check2.pop(0)
            a=self.graph[s]                                #找到目標點跟其他點之間的距離
            a1=max(a)+1                                    #將與其他點中的最大距離+1
            b = [a1 if x == 0 else x for x in a]           #用a1取代list中的0
            nss=b.index(min(b))                            #找最小值的位置
            nsv=min(b)                                     #找最小值
            p[nss]=nsv                                     #將最小值放到p的nss位置
            check[nss]=True
            dict[str(s)]=0
            dict[str(nss)]=nsv
        return dict
    
    def Kruskal(self):
        list3=set(self.list2)
        list4=[-1]*len(list3)
        n=len(list3)
        dict={}
        
        for i in range(n):
            a=min(self.list1)
            b=self.list1.index(min(self.list1))
            c=self.list2[b*2]
            d=self.list2[(b*2)+1]
            if list4[c]==-1 and list4[d]==-1: 
                dict[str(c)+'-'+str(d)]=a
                list4[d]=c
                self.list1.pop(b)
                self.list2.pop(b*2+1)
                self.list2.pop(b*2)
                
            elif list4[c]==-1 and list4[d]!=-1:
                if list4[d]==c:
                    self.list1.pop(b)
                    self.list2.pop(b*2+1)
                    self.list2.pop(b*2)
                    
                else:
                    dict[str(c)+'-'+str(d)]=a
                    list4[c]=list4[d]
                    self.list1.pop(b)
                    self.list2.pop(b*2+1)
                    self.list2.pop(b*2)
                   
            elif list4[c]!=-1 and list4[d]==-1:
                if list4[c]==d:
                    self.list1.pop(b)
                    self.list2.pop(b*2+1)
                    self.list2.pop(b*2)
                    
                else:
                    dict[str(c)+'-'+str(d)]=a
                    list4[d]=list4[c]
                    self.list1.pop(b)
                    self.list2.pop(b*2+1)
                    self.list2.pop(b*2)
  
            i+1  
        
        return dict
        
        
   
