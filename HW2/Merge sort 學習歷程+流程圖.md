-------------------------------------------------------------學習歷程------------------------------------------------------------------

對於merge sort，我的理解是將一串list從中間分半，再分半，一直重複著這個動作，直到list的長度為1。

接著將左右邊的list進行比大小，邊排序邊合併，一層一層進行上去。

--第一部分:分半--
```Python
def merge_sort(self,nums):
        n=len(nums)
        mid=n//2
        l=nums[0:mid]
        r=nums[mid:n+1]
        if len(l)>1:
            l=merge_sort(l)
        if len(r)>1:
            r=merge_sort(r)
```      
這一段就是在進行list分半的程式碼。先取一個中間數，再將左邊的list分成從第0位到(不包括)中間數的list，右邊的list分成從中間數到最後一位的list。

但是會出現一個超過範圍的錯誤，還有l跟r重複設定的錯誤，所以在取中間數前再加了一個條件以及另一個l跟一個r的空list。改成下列模樣。箭頭是新增的部分。

```Python
def merge_sort(self,nums):
        n=len(nums)
        l=[]    <<<
        r=[]    <<<
        if n>1:     <<<
            mid=n//2
            l=nums[0:mid]
            r=nums[mid:n+1]
        if len(l)>1:
            l=self.merge_sort(l)
        if len(r)>1:
            r=self.merge_sort(r)
```
--第二部分:排序並合併--
```Python
def ms(ld,rd):
        if ld[0]<rd[0]:
            return [ld[0]]+ms(ld[1:]+rd)    <<<
        if ld[0]>rd[0]:
            return [rd[0]]+ms(rd[1:]+ld)     <<<
```
這部分就是排序並合併的動作，一開始我並沒有考慮到，若是左邊或是右邊其中一個的長度較短，造成沒辦法比較的情況。

還有就是在箭頭的部分，因為int無法和str加在一起，造成錯誤。

解決方式就是在前方加上a=l[0] (r[0])   b=[int(i) for i in str(a)]將int轉成str。變成下列樣子。箭頭是新增的部分。
```Python
def ms(self, l,r):
        if len(l)==0:   <<<
            return r
        if len(r)==0:   <<<
            return l
        if l[0]<r[0]:
            a=l[0]      <<<
            b=[int(i) for i in str(a)]      <<<
            return b+self.ms(l[1:],r)
        if l[0]>r[0]:
            a=r[0]      <<<
            b=[int(i) for i in str(a)]      <<<
            return b+self.ms(r[1:],l)
```

-------------------------------------------------------------流程圖--------------------------------------------------------------------

參考網站(1): https://www.geeksforgeeks.org/merge-sort/

參考網站(2): https://www.geeksforgeeks.org/python-program-for-merge-sort/
