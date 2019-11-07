---學習歷程----------

對於merge sort我的理解是，將一串list從中間分半，一直重複這這個動作，直到list的長度為1，接著將左右邊的list進行比大小，邊排序邊合併，一層一層進行上去。
```Python
def m(gg):
    n=len(gg)
    mid=n//2
    l=gg[0:mid]
    r=gg[mid:n+1]
    if len(l)>1:
        l=m(l)
    if len(r)>1:
        r=m(r)
```      
這一段就是在進行list分半的程式碼。

---流程圖----------

參考網站(1): https://www.geeksforgeeks.org/merge-sort/
參考網站(2): https://www.geeksforgeeks.org/python-program-for-merge-sort/
