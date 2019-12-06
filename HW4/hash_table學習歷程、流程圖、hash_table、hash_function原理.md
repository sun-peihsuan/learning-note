---------------------------------------------------學習歷程---------------------------------------------------

在一開始的時候，雖然聽得懂老師講的概念，但因為寫不太出來，所以參考了老師的程式碼。

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/1575439085702.jpg)

不過後來我認為在while迴圈這部分是不需要的，所以直接刪除，再來因為有充分理解大致走訪的方式，在contains的地方很順利的寫了出來。

但是不管怎麼測試，甚至在沒有放任何值的情況下，依舊跑出Ture。

後來發現是因為我在

```Python
def add(self, key):
        h=MD5.new()
        h.update("key".encode("utf-8"))       ###
        h=h.hexdigest()
        x=int(h,16)
        y=x%self.capacity
        node=self.data[y]
        
        a=ListNode(h)
        self.data[y]=a
        a.next=self.data[y]
```
###的地方將key包在雙引號內，所以不管我有沒有放值進去，key永遠在裡面。

----------------------------------------------------流程圖----------------------------------------------------

---add---
![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/%E6%8A%95%E5%BD%B1%E7%89%871.JPG)

---contains---
![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/%E6%8A%95%E5%BD%B1%E7%89%872.JPG)

---remove---
![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/%E6%8A%95%E5%BD%B1%E7%89%873.JPG)

--------------------------------------------------hash table-------------------------------------------------

-------------------------------------------------hash function-----------------------------------------------
