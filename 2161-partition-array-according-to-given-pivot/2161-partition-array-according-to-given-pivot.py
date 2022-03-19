class Solution:
    def pivotArray(self, nums: List[int], p: int) -> List[int]:
        l=[]
        k=[]
        c=0
        for i in range(len(nums)):
            if(nums[i]<p):
                l.append(nums[i])
            elif(nums[i]==p):
                c+=1
            else:
                k.append(nums[i])
        
        return l+[p]*c +k
        