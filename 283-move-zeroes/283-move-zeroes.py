class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=nums.count(0)
        for i in range(a+1):
            if(0 in nums):
                nums.remove(0)
        for j in range(a):
            nums.append(0)
        
        