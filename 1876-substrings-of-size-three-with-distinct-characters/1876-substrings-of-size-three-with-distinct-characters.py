class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c=0
        for i in range(len(s)-2):
            s1=s[i:i+3]
            if(s1.count(s1[0])==1 and s1.count(s1[1])==1 and s1.count(s1[2])==1):
                print(s1)
                c+=1
        return c
        