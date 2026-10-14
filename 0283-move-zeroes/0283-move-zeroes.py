class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        temp=[]
        for i in range(0,n):
         if nums[i]!=0:
           temp.append(nums[i])

        n1=len(temp)
        for i in range(0,n1):
          nums[i]=temp[i]
        for i in range(n1,n):
          nums[i]=0
        print(nums)
