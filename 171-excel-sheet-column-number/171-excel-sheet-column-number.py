class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        c=columnTitle[::-1]
        s=0
        l=len(c)
        for i in range(l):
            d=ord(c[i])-64
            e=d*((26)**i)
            s+=e
        return s
            