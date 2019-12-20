--------------------------------------------------學習歷程------------------------------------------------------------------------

一開始的時候，把BFS想得很簡單，但實際操作卻有點難度，後來是參考網路上的做法寫出來的。

創了三個LIST，一個確認有沒有走訪過(CHECK)，一個放QUEUE，一個放要RETURN的LIST。

原本是想要用看CHECK裡面還有沒有False來決定是否要繼續進行

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/hw5.jpg)

不過不知道為什麼，只有回傳一個值，後來還是用網路上搜到的方式寫。

之後因為不死心，再試了一次

```Python
while Q:                =>                      while False in check:
```
不過還是一樣，後來將False in check令成a，放在while外面

```Python
a=False in check
while a==True:
```
本來以為可以了，但是又跑出

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/ERROR.jpg)

增加Q的長度不為空值這個條件後
```Python 
a=False in check
while a==True and len(Q)!=0:
```
也不行。

後來改成
 ```Python
 while check.count(False)>0:
 ```
BFS就可以成功。

在DFS的部分，我是直接用BFS的程式碼做更改，因為他們的差別就只是在Stack跟Queue，一個是先進先出，一個是先進後出

不過第一次在做更改的時候，只有改
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

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/BFS.JPG)

--------------------------------------------------DFS流程圖-----------------------------------------------------------------------

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/DFS.JPG)

--------------------------------------------------原理、比較-----------------------------------------------------------------------

BFS是從根節點開始，沿著樹的寬度遍歷樹的節點，也就是說，要先走訪完一層之後才會往下一層走訪。如果所有節點均被存取，則演算法中止。

沿著樹的深度遍歷樹的節點，儘可能深的搜尋樹的分支。當節點v的所在邊都己被探尋過，搜尋將回溯到發現節點v的那條邊的起始節點。這一過程一直進行到已發現從源節點可達的所有節點為止。

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/HW5-1.jpg)

--------------------------------------------------參考資料-----------------------------------------------------------------------

參考網址1:https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2

參考網址2:https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

參考網址3:https://zh.wikipedia.org/wiki/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2

參考網址4:https://www.itread01.com/content/1541297601.html
