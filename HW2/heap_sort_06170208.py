class Solution(object):
    def __init__(self):
        self.s = []
    def heap_sort(self,nums):
        global s
        n=len(nums)
   
        for i in range(n,-1,-1):
            f=i
            l=(i*2)+1
            r=(i*2)+2
            if l<len(nums):
                if nums[f]>nums[l]:
                    nums[f],nums[l]=nums[l],nums[f]
            if r<n:
                if nums[f]>nums[r]:
                    nums[f],nums[r]=nums[r],nums[f]
        self.s.append(nums[0])
        nums[0]=nums[-1]
        nums.pop(-1)
        if len(nums)>0:
            nums=self.heap_sort(nums)
        
        return self.s
