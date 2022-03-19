class Solution:
    def wateringPlants(self, p: List[int], c: int) -> int:
        
        d=0
        ac=c
        i=0
        while(i<len(p)):
            if(c>=p[i]):
                d+=1
                c-=p[i]
                i+=1
            else:
                c=ac
                d+=2*(i)
        return d
            
                
                
            
        