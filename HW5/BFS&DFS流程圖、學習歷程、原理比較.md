--------------------------------------------------學習歷程------------------------------------------------------------------------

一開始的時候，把BFS想得很簡單，但實際操作卻有點難度，後來是參考網路上的做法寫出來的。

創了三個LIST，一個確認有沒有走訪過(CHECK)，一個放QUEUE，一個放要RETURN的LIST。

原本是想要用看CHECK裡面還有沒有False來決定是否要繼續進行

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/hw5.jpg)

不過不知道為什麼，只有回傳一個值，後來還是用網路上搜到的方式寫。

在DFS的部分，我是直接用的程式碼做更改，因為他們的差別就只是在Stack跟Queue，一個是先進先出，一個是先進後出

不過在更改的時候，只有改
```Python
s=Q.pop(0)    =>    s=Q.pop(-1)
```
沒有改到p的部分，導致出來的答案跟BFS一模一樣。

剛開始還不知道是怎麼回事，後來檢查時才發現，在BFS時，是直接在for迴圈裡面append進去p
```Python
while Q:
            s=Q.pop(0)
            for i in self.graph[s]:
                if check[i] ==False:
                    Q.append(i)
                    p.append(i)
                    check[i]=True
            
        return p
```
但是DFS是要在for迴圈執行完之後才要將s append進去p
```Python
while S:
            s=S.pop(-1)
            for i in self.graph[s]:
                if check[i] ==False:
                    S.append(i)
                    check[i]=True
            p1.append(s)
            
        return p1
```
不過我發現，若是要按照思考的邏輯，在BFS的時候，應該也要將"s append進去p"這段放到for迴圈外面，雖然不影響答案。


--------------------------------------------------BFS流程圖-----------------------------------------------------------------------

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/HW5-BFS.JPG)

--------------------------------------------------DFS流程圖-----------------------------------------------------------------------

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/HW5-DFS.JPG)

--------------------------------------------------原理比較-----------------------------------------------------------------------

--------------------------------------------------參考資料-----------------------------------------------------------------------

參考網址1:https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2

參考網址2:https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

參考網址3:https://zh.wikipedia.org/wiki/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2
