class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a=max(nums)
        k=[]
        c=[0]*(a+1)
        for i in nums:
            c[i]+=1
        b=c.index(max(c))
        k.append(b)
        for i in range(1,len(nums)+1):
            if(i not in nums):
                k.append(i)
                break
        return k
            
        