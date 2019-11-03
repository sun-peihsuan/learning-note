我對Heap sort的理解是(最小的當root)，將父節點與子節點做比較，若是父節點比子節點大，交換，若是父節點比子節點小則不變。
總結來說就是每次排完序後，最小的一定在最上面，將root提出後，把尾端的拉到root的位置，在重新做一次排序，一直做到結束就完成了。

第一張和第二張圖，是初期時的想法，但是在把gg裡的數字加到s裡時，沒有想到最後gg裡面會是空值，導致錯誤。

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/1.jpg?)

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/2.jpg?)

在第三張圖的部分，回傳gg，確認gg到最後會是空值，並且對將gg裡的數加進s時多加了一個"gg的長度大於1"條件，

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/3.jpg?)

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/4.jpg?)

參考網站: https://www.geeksforgeeks.org/python-program-for-heap-sort/
