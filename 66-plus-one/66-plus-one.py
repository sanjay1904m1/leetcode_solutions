class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        c=[]
        for i in digits:
            s=s+str(i)
        b=int(s)+1
        for i in str(b):
            c.append(int(i))
        return c
        