class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c=0
        n=len(nums)
        k=target
        lst=nums
        m=[]
        for i in range(n):
            b=k-lst[i]
            v=lst[i]
            del(lst[i]) 
            if(b in lst):
                o=i
                m.append(i)
                break
            else:
                lst.insert(i,v)
                pass
        lst.insert(i,v)
        for i in range(n):
            if(lst[i]==b and i!=o):
                m.append(i)
                break
        return m