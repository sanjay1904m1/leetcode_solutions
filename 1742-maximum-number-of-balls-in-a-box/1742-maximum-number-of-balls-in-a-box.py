class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        h={}
        for i in range(lowLimit,highLimit+1,1):
            l=[]
            for j in str(i):
                l.append(int(j))
            s=sum(l)
            print(s)
            if(s in h):
                h[s]+=1
            else:
                h[s]=1
        
        a=-2**31
        for i in h:
            a=max(a,h[i])
        return a
            
        