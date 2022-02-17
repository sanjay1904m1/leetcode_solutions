class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h=haystack
        n=needle
        a=len(n)
        c=0
        for i in range(len(h)):
            if(n==h[i:a+i]):
                c+=1
                break
            elif(i!=len(h)-1):
                pass
            else:
                return "-1"
        if(n==h):
            return "0"
        if(c>=1):
            return i
        else:
            return "-1"
        