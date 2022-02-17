class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1=list(s)
        t1=list(t)
        s2=0
        t2=0
        for i in s:
            s2+=ord(i)
        for j in t:
            t2+=ord(j)
        a=t2-s2
        b=(chr(a))
        return b


    
        
