class Solution:
    def longestPalindrome(self, s: str) -> int:
        h={}
        f=len(s)
        for i in s:
            if(i not in h):
                h[i]=1
            else:
                h[i]+=1
        for i in h:
            if(h[i]%2!=0):
                f-=1
        if(f<len(s)):
            return f+1
        return f
                
            
        