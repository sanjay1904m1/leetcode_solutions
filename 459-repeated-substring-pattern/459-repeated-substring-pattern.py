class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(2,len(s)+1):
            k=int(len(s)/i)
            a=s[0:k]
            if(i*a==s):
                return True
                break
            elif(i!=len(s)):
                pass
            else:
                return False
                break
            
            
            
                
        