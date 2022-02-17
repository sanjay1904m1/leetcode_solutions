class Solution:
    def isHappy(self, n: int) -> bool:
        while(n!=1):
            if(len(str(n))==1 and n!=7 or len(str(n**2))==1):
            
                return False
                break
                
                
        
            else:
        
                a=0
                for i in str(n):
                    a+=int(i)**2
                n=a
        return True