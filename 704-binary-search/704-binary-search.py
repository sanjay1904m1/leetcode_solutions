class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l=0
        h=len(nums)-1
        while(l<=h):
            m=(l+h)//2
            if(nums[m]<t):
                l=m+1
            elif(nums[m]>t):
                h=m-1
            elif(nums[m]==t):
                return m
        return -1