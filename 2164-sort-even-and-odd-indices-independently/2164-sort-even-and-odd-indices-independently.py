class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        l=[]
        g=[]
        f=[]
        for i in range(len(nums)):
            if(i%2==0):
                l.append(nums[i])
            else:
                g.append(nums[i])
        l.sort()
        g.sort(reverse=True)
        for i in range(0,len(nums)//2):
            f.append(l[i])
            f.append(g[i])
        if(len(l)>len(nums)//2):
            f.append(l[-1])
        elif(len(g)>len(nums)//2):
            f.append(g[-1])
        return f
        