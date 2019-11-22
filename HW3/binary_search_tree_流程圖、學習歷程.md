---------------------------------------------------------學習歷程----------------------------------------------------------

-----Insert-----

簡單來說，Insert的想法是，先看root存不存在，如果不存在就把插入的值當作root，存在就先跟root的比大小，比root大就往右走，比root小往左走。
再來就是看root.left或是root.right存不存在，如果不存在就把插入的值當作root.left或是root.right，大概是照這個概念一直走下去，直到可以把值插入為止
```Python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def insert(root,node):
    if root is None:
        root=node
    else:
        if root<node:
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)
        if root>node:
            if root.left is None:
                root.left=node
            else:
                insert(root.left,node)
```
這是一開始聽完老師講解後，再參考網路上的資料寫出來的，但為了要符合格式，要做調整
```Python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
def insert(self, root, val):
        if root is None:
            return root=TreeNode(val)                           ##1
        else:
            if val < root:                                      ##2
                if root.left is None:
                    root.left=TreeNode(val)
                else:
                    self.insert(root.left,val)
            if val > root:                                      ##3
                if root.right is None:
                    root.right=TreeNode(val)
                else:
                    self.insert(root.right,val)

```
從一開始的格式開始改，另開一個class，將"##1"的val改成TreeNode(val)，"##2"及"##3"改成"val < root"及"val > root"。
```Python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):
        if root is None:
            root.val=TreeNode(val)                          ##1
            return root.val
        else:
            if val <= root.val:                              ##4
                if root.left is None:
                    root.left=TreeNode(val)                 ##2
                    return root.left
                else:
                    return self.insert(root.left,val)
            if val > root.val:
                if root.right is None:
                    root.right=TreeNode(val)                ##3
                    return root.right
                else:
                    return self.insert(root.right,val)
```
後來出現error，因為不管是root、root.left或是root.right都是節點，沒辦法比較，所以都在後面加了".val"讓他們可以跟int比較("##2"和"##3"也一樣)

在"##1"的地方原本的程式碼出現格式錯誤，所以改成先將root.val這個值另成TreeNode(val)，再return root.val

那又因為作業規定若是有相同的值一律往左邊走，在"##4"的地方改成"<="

-----Search-----

Search的概念是，將要尋找的值跟root做比較，一樣就是root，不一樣的時候，比大小，比較大往右邊找，比較小往左邊找，一直用這個方式去尋找
```Python
def search(self, root, target):
        if target<self.val:
            if self.left is None:
                return "The target"+str(target)+"is not find"
            else:
                "The target"+str(target)+"is find"
        if target>self.val:
            if self.right is None:
                return "The target"+str(target)+"is not find"
            else:
                "The target"+str(target)+"is find"
```
這是一開始聽完老師講解後，再參考網路上的資料寫出來的，但為了要符合格式，要做調整，而且測試的方式是要看找到的值有沒有符合位置
```Python
  def search(self, root, target):
        if target is None or target==root.val:
            return root
        if target<root.val:
            if root.left is None:
                return root
            if root.left.val==target:
                return root.left
            if root.left.val>target or root.left<target:            ##1
                return self.search(root.left,target)
        if target>root.val:
            if root.right is None:
                return root
            if root.right.val==target:
                return root.right
            if root.right.val>target or root.right<target:          ##2
                return self.search(root.right,target)
```
後來改成這樣，一樣因為root、root.left或是root.right都是節點，沒辦法比較，所以都在後面加了".val"

還有，因為是上面的程式碼只有跑一次，那麼root.left或是root.right之後的子節點沒有被搜尋到，所以增加了"##1"和"##2"兩個條件

並且因為回傳target是否有沒有找到並不符合作業要求，所以改成回傳找到得target的位置，若是沒有找到就回傳root

-----Delete-----

Delete的概念是，先找到想刪除的節點a，再看那個節點有沒有子節點，若是沒有，直接刪除即可。

若是有一個子節點，則是將其子節點向上移動，取代刪除的節點位置。

若是有兩個子節點，則是將左邊的子節點a1取代取代刪除的節點位置(這是我的想法，但是其他人的做法不是，不過這是我目前想到最不會出錯的方式)。

但後來想了一下，若是a1之後還有子節點，我沒辦法將剩下的一起往上提，原本a1的位置未出現None或是a1的值，到不如直接往a1之後的最右邊節點，取代a的位置，這樣就不會出錯了，不過好像就是網路上其他人的想法。

-----Modify-----

把指定修改的數字的節點刪除並加入指定的值，並且不能改變原本的高度。

----------------------------------------------------------流程圖------------------------------------------------------------
-----Insert-----
![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/insert.JPG)
-----Search-----
![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/search.JPG)
-----Delete-----

沒有子節點時
![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/delete-0.JPG)
有一個子節點時
![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/delete-1.JPG)
有兩個子節點時
![image](https://github.com/sun-peihsuan/learning-note/blob/master/image/delete-2.JPG)
-----Modify-----

參考網址1:https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

參考網址:2https://www.laurentluce.com/posts/binary-search-tree-library-in-python/


