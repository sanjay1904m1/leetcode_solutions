class Solution:
    def countSegments(self, s: str) -> int:
        d=[]
        if(len(s)*" "==s):
            return 0
        s=s+" "
        s1=""
        c=0
        for i in s:
            if(i!=" "):
                s1=s1+i
            else:
                if(s1 != ""):
                    d.append(s1)
                    
                s1=""
        return len(d)
                
        