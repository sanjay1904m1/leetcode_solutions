class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in t:
            if(i not in s):
                t=t.replace(i,"")
        print(t)
        if(s==t or s in t):
            return True
        for i in t:
            for j in range(t.count(i)):
                if(t.count(i)>s.count(i)):
                    t=t.replace(i,"",1)
                    if(s==t):
                        return True
            print(t)
        
        else:
            return False
        