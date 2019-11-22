---------------------------------------------------------學習歷程----------------------------------------------------------

-----Insert-----

簡單來說，Insert的想法是，先看root存不存在，如果不存在就把插入的值當作root，存在就先跟root的比大小，比root大就往右走，比root小往左走。
再來就是看root.left或是root.right存不存在，如果不存在就把插入的值當作root.left或是root.right，大概是照這個概念一直揍下去，直到可以把值插入為止
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
從一開始的格式開始改，另開一個class，將"##1"的val改成TreeNode(val)，"##2"及"##3"改成val < root及val > root。
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
            if val < root.val:
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

-----Search-----

-----Delet-----

-----Modify-----

----------------------------------------------------------流程圖------------------------------------------------------------

參考網址:https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
