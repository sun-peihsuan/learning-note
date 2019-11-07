###### merge_sort_06170208.py

class Solution(object):
    def merge_sort(self,nums):
        n=len(nums)
        l=[]
        r=[]
        if n>1:
            mid=n//2
            l=nums[0:mid]
            r=nums[mid:n+1]
        if len(l)>1:
            l=self.merge_sort(l)
        if len(r)>1:
            r=self.merge_sort(r)
        return self.ms(l,r)    
    def ms(self, l,r):
        if len(l)==0:
            return r
        elif len(r)==0:
            return l
        elif l[0]<r[0]:
            a=l[0]
            b=[int(i) for i in str(a)]
            return b+self.ms(l[1:],r)
        else:
            a=r[0]
            b=[int(i) for i in str(a)]
            return b+self.ms(r[1:],l)
