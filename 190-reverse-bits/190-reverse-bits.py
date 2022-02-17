class Solution:
    def reverseBits(self, n: int) -> int:
        b=str(bin(n).replace("0b", ""))
        c=len(b)
        k=b[::-1]+str(("0"*(32-c)))
        m=int(k,2)
        return m
        