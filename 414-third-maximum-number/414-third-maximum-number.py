class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if( i not in l):
                l.append(i)
        a=sorted(l)
        if(len(a)>=3):
            return a[len(a)-3]
        else:
            return a[-1]
        
        
        
        