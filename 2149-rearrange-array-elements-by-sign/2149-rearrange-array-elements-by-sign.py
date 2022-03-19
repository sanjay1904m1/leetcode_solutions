class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l=[]
        g=[]
        f=[]
        for i in range(len(nums)):
            if(nums[i]<0):
                l.append(nums[i])
            else:
                g.append(nums[i])
        for i in range(len(nums)//2):
            f.append(g[i])
            f.append(l[i])
        return f
            
                
        