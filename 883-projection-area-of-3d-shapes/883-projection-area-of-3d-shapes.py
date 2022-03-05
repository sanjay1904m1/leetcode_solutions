class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        l=0
        for j in range(len(grid[0])):
            mx=-2**31
            for i in range(len(grid)):
                mx=max(mx,grid[i][j])
            l+=mx
        c=0    
        for i in grid:
            l+=max(i)
            c+=i.count(0)
        l+=len(grid)*len(grid[0])-c
        return l
        
            
                
            
        