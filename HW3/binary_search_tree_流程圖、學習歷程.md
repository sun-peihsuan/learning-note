---------------------------------------------------------學習歷程----------------------------------------------------------

-----Insert-----
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

-----Search-----

-----Delet-----

-----Modify-----

----------------------------------------------------------流程圖------------------------------------------------------------

參考網址:https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
