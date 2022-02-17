class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a=num**(1/2)
        b=int(a)
        if( a%b==0):
            return True
        else:
            return False
            
        