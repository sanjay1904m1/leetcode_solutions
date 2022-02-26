class Solution:
    def convertToTitle(self, c: int) -> str:
        s=""
        i=1
        while(c>26):
            rem=c%(26)
            
            
            i+=1
            
            if(rem==0):
                c=c-26
                s=s+'Z'
                
            else:
                s=s+chr(rem+64)
            print(c)
            c=c//(26)
        s=s+chr(c+64)
        return s[::-1]
            
            
        