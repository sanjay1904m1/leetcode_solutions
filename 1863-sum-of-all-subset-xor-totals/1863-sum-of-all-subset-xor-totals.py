class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        s=0
        for i in range(2**n):
            f=[]
            for j in range(n):
                if((i>>j & (1))==1):
                    f.append(nums[j])
            print(f)
            if(len(f)==1):
                    s+=f[0]
            elif(len(f)==0):
                pass
            else:
                d=f[0]
                for g in range(1,len(f)):
                    
                    d=d^f[g]
                s+=d
        return s
                    
                
        