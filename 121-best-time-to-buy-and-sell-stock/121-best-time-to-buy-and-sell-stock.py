class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=prices[0]
        mx=0
        for i in range(len(prices)):
            m=min(m,prices[i])
            bt=prices[i]-m
            mx=max(mx,bt)
        return mx
            
                
            
        