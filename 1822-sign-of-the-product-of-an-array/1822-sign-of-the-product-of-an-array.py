class Solution:
    def arraySign(self, nums: List[int]) -> int:
        a=nums[0]
        for i in range(1,len(nums)):
            a=a*nums[i]
        if(a==0):
            return 0
        elif(a>0):
            return 1
        else:
            return -1
        