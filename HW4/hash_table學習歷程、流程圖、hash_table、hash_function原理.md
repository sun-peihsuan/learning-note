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
還有
```Python
def contains(self, key):
        h=MD5.new()
        h.update("key".encode("utf-8"))          ####
        h=h.hexdigest()
        x=int(h,16)
        y=x%self.capacity
        node=self.data[y]
        
        c=ListNode(h)
        d=self.data[y]
        while node:
            if c==d:
                return True
            else:
                d.next=d
        while node is None:
            return False
```
###的地方將key包在雙引號內，所以不管我有沒有放值進去，key永遠在裡面。
後來將雙引號拿掉後，變成
```Python
h.update(key.encode("utf-8")) 
```
就成功了
不過在remove的時候就出現問題

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/hw4-p.jpg)

![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/hw4-p2.jpg)

以這兩個方式去刪除指定的值時，按照邏輯來說是沒有問題的，但是不知道為什麼不是跳到無限迴圈裏面，就是無法移除指定值。
後來參考網路上面的方式
```Python
while head is not None and head.val==val:    #保證連結串列第一個節點的值不等於val
            head=head.next
        if not head:         #判斷連結串列是否為空
            return None
        headNode = head     #頭節點
        while head.next is not None:
            if head.next.val==val:
                head.next = head.next.next
            else:
                head=head.next
        return headNode
```
再下去加以修改
```Python
def remove(self, key):
        h=MD5.new()
        h.update("key".encode("utf-8"))
        h=h.hexdigest()
        x=int(h,16)
        y=x%self.capacity
        node=self.data[y]
        
        c=self.data[y]        
        
        if c.next == None:
            if c.val==h:
                self.data[y]=None
          
        while c.next:
            if c.next.val==h:
                c.next = c.next.next
            if c.next.val!=h:
                c=c.next
```
不過依舊和add還有contains一樣，不管怎麼移除，都無法移除指定值。

後來發現是重複了上述的錯誤，在複製轉碼的過程中，將key包括在雙引號裡面，導致不管怎麼查找，都不會是key，所以也就不會將key刪掉。

但是因為發現錯誤的時間太晚的關係，沒辦法試試我之前照自己邏輯打出來的程式碼是否能夠正確的運作。

便先將從網路上修改來的，確認跑程式時不會出錯的程式碼先放上來了。

----------------------------------------------------流程圖----------------------------------------------------

---add---
![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/%E6%8A%95%E5%BD%B1%E7%89%871.JPG)

---contains---
![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/%E6%8A%95%E5%BD%B1%E7%89%872.JPG)

---remove---
![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/%E6%8A%95%E5%BD%B1%E7%89%873.JPG)

因為流程圖是事先照我原本的邏輯思路下去畫的，時間上來不及做修正。

但是後來程式碼上傳部分的邏輯是
        
        先看c的下一個值存不存在，如果不存在，且c的值跟目標值一致，便將c的值改成None。
        
        那如果c的下一個值存在，且跟目標值一致，c的下一個值就等於c的下下一個值。
                             
                             如果c的下一個值不等於目標值，c等於c的下一個值。
        

--------------------------------------------------hash table-------------------------------------------------

雜湊表（Hash table，也叫哈希表），是根據Key查詢在內存存儲位置的資料結構。

它通過計算一個關於key的函數，將所需查詢的數據投射到表中一個位置來查詢記錄。

-------------------------------------------------hash function-----------------------------------------------

雜湊函數（英語：Hash function）又稱雜湊演算法，是一種從任何一種數據中建立小的數字「指紋」的方法。

雜湊函數把訊息或數據壓縮成摘要，使得數據量變小，將數據的格式固定下來。

該函數將數據打亂混合，重新建立一個叫做雜湊值的指紋。

雜湊值通常用一個短的隨機字母和數字組成的字串來代表。

-------------------------------------------------參考網址-----------------------------------------------

參考網址1:https://www.youtube.com/watch?v=7C5f2ttq79Y&feature=youtu.be

參考網址2:https://www.itread01.com/content/1549716855.html

參考網址3:https://zh.wikipedia.org/wiki/%E5%93%88%E5%B8%8C%E8%A1%A8

參考網址4:https://www.wikiwand.com/zh-mo/%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B8
