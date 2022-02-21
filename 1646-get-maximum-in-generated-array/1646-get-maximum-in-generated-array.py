class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums=[0]*(n+5)
        nums[0]=0
        nums[1]=1
        for i in range(1,(n//2)+1):
            nums[2 * i] = nums[i] 
            nums[2 * i + 1] = nums[i] + nums[i + 1]
        print(nums)
        return max(nums[:n+1])
        
        