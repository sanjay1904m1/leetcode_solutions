class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        a=bin(n).replace("0b","")
        if((a.count("1")==1 and  a[0:3]=="100" and a.count("0")%2==0) or a=="1"):
            return True
        else:
            return False
        
        