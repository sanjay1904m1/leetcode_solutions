class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l={}
        for i in nums:
            if(i not in l):
                l[i]=1
            else:
                l[i]+=1
        for j in l:
            if(l[j]>len(nums)/2):
                return j
        
            