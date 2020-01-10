Dijkstra

  <原理>
  
    找到兩個頂點之間的最短路徑，更常見的方式是，固定了一個頂點作為原節點然後找到該頂點到圖中所有其它節點的最短路徑，產生一個最短路徑樹。
  
  <流程圖>
    ![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/%E6%8A%95%E5%BD%B1%E7%89%871.JPG)
    
Kruskal

  <步驟>
  
    1.建新的圖中擁有原圖中相同的節點，但沒有邊
    2.將原圖中所有的邊按距離從小到大排序
    3.從距離最小的邊開始，如果這條邊連接的兩個節點在圖中不會形成迴圈，添加這條邊到新的圖中
    4.重複3，直至新的圖中所有的節點都連在一起
  
  <流程圖>
  ![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/hw6-K.jpg)
  
