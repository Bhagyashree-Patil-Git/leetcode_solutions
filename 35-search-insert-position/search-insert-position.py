class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif target > nums[mid]:
                l=mid+1
            else:
                r=mid-1
        m=0
        n=m+1
        for i in range(0,len(nums)):
         if nums[m]>target:
            return m
         if n==len(nums):
            return n
         if nums[m]<=target & target<=nums[n]:
          return n
         else:
            m+=1
            n+=1
         
         


