class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[0]
        for i in range(1,n+1):
            c=0
            while(i!=0):
                i=i&(i-1)
                c+=1
            l.append(c)
        return l
            
        