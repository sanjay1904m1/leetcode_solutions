class Solution:
    def isPalindrome(self, x: int) -> bool:
        b=str(x)
        c=b[::-1]
        if(b==c):
            return True
        return False
    
        
            
        