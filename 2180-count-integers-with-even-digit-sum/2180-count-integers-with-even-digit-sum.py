class Solution:
    def countEven(self, num: int) -> int:
        c=0
        for i in range(2,num+1):
            l=[]
            for j in str(i):
                l.append(int(j))
            if(sum(l)%2==0):
                c+=1
        return c
        