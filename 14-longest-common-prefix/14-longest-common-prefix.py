class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=strs[0]
        c=len(s)
        for i in range(c):
            for j in strs:
                if(s==j[0:len(s)]):
                    pass
                else:
                    s=s[0:len(s)-1]
                    break
        
        return s
        
        
        