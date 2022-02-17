class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l=len(nums)
        ans=nums[0]
        for i in range(1,l):
            ans=ans^nums[i]
        return ans
            
        