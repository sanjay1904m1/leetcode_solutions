class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<0):
            if((3**19)/-1*n==0):
                return True
            else:
                return False
        elif(n!=0 and(3**19)%n==0):
            return True
        else:
            return False
        