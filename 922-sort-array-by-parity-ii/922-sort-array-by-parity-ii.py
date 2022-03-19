class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l=[]
        g=[]
        f=[]
        for i in range(len(nums)):
            if(nums[i]%2==0):
                l.append(nums[i])
            else:
                g.append(nums[i])
        for i in range(len(nums)//2):
            f.append(l[i])
            f.append(g[i])
        return f
        