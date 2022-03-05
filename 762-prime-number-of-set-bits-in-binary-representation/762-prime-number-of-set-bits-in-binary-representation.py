def prime(n):
    if(n==0 or n==1):
        return False
    if(n==2 or n==3):
        return True
    for i in range(2,n):
        if(n%i==0):
            return False
    return True


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        c1=0
        for i in range(left,right+1):
            c=bin(i).replace("0b","")
            if(prime(c.count("1"))):
                c1+=1
        return c1
        