class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        g=sum(nums)
        for i in range(len(nums)):
            a=nums[:i]
            
            if(sum(a)==(g-sum(a)-nums[i])):
                return i
        return -1
        