(1) 

heap sort 跟 merge sort 兩者在時間複雜度上，不管是在 best case、average case、worst case上，都是 NlogN。

(2) 

heap sort是 unstable sorting(不穩定)。

merge sort 是 stable sorting(穩定)。

(3)

heap sort 的空間複雜度為Ο(1)，原地置換。

merge sort 的空間複雜度為Ο(n)，需要暫時性的暫列存放每回合Merge後的結果。

(4)

merge sort 較常用於 External sort(外部排序)。


在我查到的資料來說，merge sort 相較 heap sort，處理的資料量較為龐大(第四點)，但是在嘗試寫這兩種排序時，heap sort較為直覺，比較好想出來，花費的時間較少，但在寫 merge sort 的時候，前半部分的拆開比較容易，但在後半部排序並合併這部分，花費了較多的時間，去修正缺少的條件。

----------------------------------------------------------------------------------------------------------------------------
參考網站(1):http://spaces.isu.edu.tw/upload/18833/3/web/sorting.htm#_Toc229730284

參考網站(2):http://notepad.yehyeh.net/Content/Algorithm/Sort/Sort.php
