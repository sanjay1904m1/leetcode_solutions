class Solution:
    def climbStairs(self, n: int) -> int:
        s=[1,1]
        for i in range(2,n+1):
            s.append(s[i-1]+s[i-2])
        return s[n]
        