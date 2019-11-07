---學習歷程----------

我對Heap sort的理解是(最小的當root)，將父節點與子節點做比較，若是父節點比子節點大，交換，若是父節點比子節點小則不變。
總結來說就是每次排完序後，最小的一定在最上面，將root提出後，把尾端的拉到root的位置，在重新做一次排序，一直做到結束就完成了。

第一張和第二張圖，是初期時的想法，但是在把gg裡的數字加到s裡時，沒有想到最後gg裡面會是空值，導致錯誤。

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/1.jpg?)

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/2.jpg?)

在第三張圖的部分，回傳gg，確認gg到最後會是空值，並且對gg要再跑一次排序時多加了一個"gg的長度大於1"條件，

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/3.jpg?)

最後一張圖，是將第三張圖，回傳gg部分改成回傳s，但是卻只有回傳第一個值。

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/4.jpg?)

後來將s=[]這部分提到def之外，就解決了最後一張圖只能回傳一個值的問題。

但是會有個小問題，就是跑完一次就得重新跑一次def跟s=[ ]，不然在s=[ ]這部分會一直將前面的跑過一次的數字加下去。

之後因為要改成規定的格式，沒有辦法直接在def之外加一個s=[ ] ，所以上網查後有人建議用再多加一個_ _int_ _在前方。
解決了上述問題

---流程圖----------

參考網站(1): https://www.geeksforgeeks.org/python-program-for-heap-sort/

參考網站(2): https://stackoverflow.com/questions/46299570/nameerror-name-s-is-not-defined/46299673

