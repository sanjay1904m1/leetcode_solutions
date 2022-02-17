class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=nums.count(val)
        for i in range(a+1):
            if(val in nums):
                nums.remove(val)
        b=len(nums)  
        return b
        