class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=[]
        g=[]
        f=[]
        for i in range(len(nums)):
            if(nums[i]%2==0):
                l.append(nums[i])
            else:
                g.append(nums[i])
        
        
        return l+g
        