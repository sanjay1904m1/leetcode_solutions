class Solution:
    def minimumSum(self, num: int) -> int:
        d=[]
        for i in str(num):
            d.append(int(i))
        s=""
        t=""
        a=min(d)
        if(a!=0):
            s=s+str(a)
        d.remove(a)
        b=min(d)
        if(b!=0):
            t=t+str(b)
        d.remove(b)
        s=s+str(d[0])
        t=t+str(d[1])
        return (int(s)+int(t))
        
            
        