class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1=s[::-1]
        s2=s1.lstrip()
        c=0
        for i in s2:
            if(i!=" "):
                c+=1
            else:
                break
        return c
        