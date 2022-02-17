class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=[]
        for i in nums1:
            if(i in nums2):
                s.append(i)
        k=[]
        for j in s:
            if(j not in k):
                k.append(j)
        return k
                
        