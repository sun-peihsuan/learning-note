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
```Python
def ms(ld,rd):
        if len(ld)==0:
            return rd
        if len(rd)==0:
            return ld
        if ld[0]<rd[0]:
            return [ld[0]]+ms(ld[1:]+rd)    <------
        if ld[0]>rd[0]:
            return [rd[0]]+ms(rd[0]+ld) <------
```
這部分就是排序並合併的動作，一開始我並沒有考慮到，若是左邊或是右邊其中一個的長度較短，造成沒辦法比較的情況。

還有就是在箭頭的部分，因為int無法和str加在一起。

解決方式就是在前方加上a=l[0](r[0])   b=[int(i) for i in str(a)]去將int轉成str。變成下列樣子。
```Python
def ms(self, l,r):
        if len(l)==0:
            return r
        if len(r)==0:
            return l
        if l[0]<r[0]:
            a=l[0]
            b=[int(i) for i in str(a)]
            return b+self.ms(l[1:],r)
        if l[0]>r[0]:
            a=r[0]
            b=[int(i) for i in str(a)]
            return b+self.ms(r[1:],l)
```

---流程圖----------

參考網站(1): https://www.geeksforgeeks.org/merge-sort/

參考網站(2): https://www.geeksforgeeks.org/python-program-for-merge-sort/
