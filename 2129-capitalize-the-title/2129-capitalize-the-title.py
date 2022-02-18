class Solution:
    def capitalizeTitle(self, t: str) -> str:
        t=t+" "
        p=""
        g=[]
        f=""
        for i in t:
            if(i==" "):
                g.append(f)
                f=""
            else:
                f=f+i
        for i in g:
            if(len(i)>2):
                if(i[0].isupper()):
                    p=p+i[0]
                else:
                    p=p+i[0].upper()
                p=p+i[1:len(i)].lower()
                p=p+" "
            else:
                p=p+i.lower()
                p=p+" "
        
        return p.rstrip()
                
        
                
                
        
        
                
        