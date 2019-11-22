class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):
        if root is None:
            root.val=TreeNode(val)
            return root.val
        else:
            if val <= root.val:
                if root.left is None:
                    root.left=TreeNode(val)
                    return root.left
                else:
                    return self.insert(root.left,val)
            if val > root.val:
                if root.right is None:
                    root.right=TreeNode(val)
                    return root.right
                else:
                    return self.insert(root.right,val)
            
    def delete(self, root, target):
        
   def search(self, root, target):
        if target is None :
            return None
        if target==root.val:
            return root
        if target<root.val:
            if root.left is None:
                return None
            if root.left.val==target:
                return root.left
            if root.left.val>target or root.left.val<target:            
                return self.search(root.left,target)
        if target>root.val:
            if root.right is None:
                return None
            if root.right.val==target:
                return root.right
            if root.right.val>target or root.right.val<target:          
                return self.search(root.right,target)
        
    def modify(self, root, target, new_val):
