class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x=bin(x).replace("0b","")
        y=bin(y).replace("0b","")
        if(len(x)>len(y)):
            y=("0"*(len(x)-len(y)))+y
        elif(len(x)<len(y)):
            x=("0"*(len(y)-len(x)))+x
        print(x,y)
        
        
        a1=0
        
        for i in range(len(x)):
            if(x[i]!=y[i]):
                a1+=1
                
        
        return a1
            
        
        