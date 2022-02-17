class Solution:
    def hammingWeight(self, N: int) -> int:
        c=0
        while (N > 0):
            if((N & 1)==1):
                c+=1
            N=N>>1
        return(c)
        