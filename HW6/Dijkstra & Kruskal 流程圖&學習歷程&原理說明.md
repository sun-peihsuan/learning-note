--------------------------------------------------------學習歷程--------------------------------------------------------

這是一開始的想法，按照上一次做BFS時的概念去改，設一個CHECK，但是後來發現這個方式太複雜，直接將助教給的側直格式改成跟Kruskal類似
```Python
def Dijkstra(self, s): 
        n=len(self.graph)
        p=[False]*n
        check=[False]*n
        check2=[False]*n
        p[s]=0
        check[s]=True
        while check2:
            q=check2.pop(0)
            a=self.graph[s]                                #找到目標點跟其他點之間的距離
            a1=max(a)+1                                    #將與其他點中的最大距離+1
            b = [a1 if x == 0 else x for x in a]           #用a1取代list中的0
            nss=b.index(min(b))                            #找最小值的位置
            nsv=min(b)                                     #找最小值
            p[nss]=nsv                                     #將最小值放到p的nss位置
            check[nss]=True
        return p,check
```

在 Kruskal 的部分，一開始想說用hash table的方式做，以距離當作抽屜名稱。但後來嘗試的過程中覺得太複雜，放棄了。

後來是用多個list來做。

先在__init__裡面加入
```Python
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.list1=[]
        self.list2=[]
```
後來按照老師推薦的背一集訓影片內容的方式，去確認有沒有形成迴圈。

不過在寫的過程中，因為不熟悉dictionary的格式，一直出錯。
正確應該這麼寫
```Python
dict[str(c)+'-'+str(d)]=a
```
但是我一直寫這樣
```Python
dict[c'-'d]=a
```
或是這樣
```Python
dict[str(c)'-'str(d)]=a
```
那後來為了形成迴圈，讓程式可以跑到結束，我先是了while迴圈，讓只要某一個list裡面只要不是只剩一個-1就一直跑下去

但是為了保險起見，我用for迴圈，因為有n個點就一定有n-1條邊，所以程式只要跑n-1次就可以結束

```Python
 for i in range(n):
 ......
  i+1
```
---------------------------------------------------------流程圖---------------------------------------------------------

Dijkstra 流程圖

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/%E6%8A%95%E5%BD%B1%E7%89%871.JPG)

Kruskal 流程圖

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/hw6-K.jpg)
--------------------------------------------------------原理說明--------------------------------------------------------

Dijkstra algorithm

是用来求單元最短路徑，確定哪個是原點之后，可以得到從原點到其餘所有頂點之間的最短路徑和最短距離。

不過限制就是只適用於非負值的距離。

Kruskal算法運用的貪心算法的方式進行求解，貪心算法是每步都取最優，最后使整體最優。

且不形成迴圈，也就是生成一個最小生成樹。



--------------------------------------------------------參考網址--------------------------------------------------------

1. https://wenyuangg.github.io/posts/python3/python-set.html

2.https://blog.kdchang.cc/2017/08/11/learning-programming-and-coding-with-python-variable/

3.https://www.youtube.com/watch?v=wuU4DDEUu1w

4.https://zh.wikipedia.org/wiki/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95

5.https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95

6.https://blog.csdn.net/Xyc19930930/article/details/77862422

7.https://blog.csdn.net/qq_23014515/article/details/51253949

8.https://docs.google.com/presentation/d/e/2PACX-1vTgHO5AkHJS6iN6bnnBMMdHv6E4rabnrC0KwyTRfjad8Ab3IQjbnGvZuQOjDC9t7nKqeroiwcuasJrI/pub?start=false&loop=false&delayms=3000&slide=id.g7b9afdb0e7_0_88
