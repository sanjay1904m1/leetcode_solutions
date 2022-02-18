class Solution:
    def findComplement(self, num: int) -> int:
        a=bin(num).replace("0b","")
        s=""
        for i in a:
            if(i=="0"):
                s+="1"
            else:
                s+="0"
        d=int(s,2)
        return d
        