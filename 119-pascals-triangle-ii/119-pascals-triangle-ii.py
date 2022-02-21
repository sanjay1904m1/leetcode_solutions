class Solution:
    def getRow(self, n: int) -> List[int]:
        h=[]
    
        for i in range(1, int(n+2)):
            c=[]
            C = 1
            for j in range(1, int(i+1)):
                c.append(C)
                C = C * (i - j) // j
            h.append(c)
        return h[n]
    
        