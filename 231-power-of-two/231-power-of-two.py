class Solution:
    def isPowerOfTwo(self, ele: int) -> bool:
        c=0
        while(ele!=0):
            ele=(ele & (ele-1))
            c=c+1
            if(c>1):
                break
        if(c==1):
            return True
        else:
            return False
        