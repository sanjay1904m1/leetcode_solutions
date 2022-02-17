class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s=""
        c='0'
        if(len(b)<len(a)):
            b=(len(a)-len(b))*"0"+b
        elif(len(a)<len(b)):
            a=(len(b)-len(a))*"0"+a
        for i in range(len(a)-1,-1,-1):
            if(a[i]=='0'  and b[i]=='0' ):
                if(c=='0'):
                    s=s+"0"
                    c="0"
                else:
                    s=s+"1"
                    c="0"
            elif(a[i]=='0' and b[i]=='1'):
                if(c=='0'):
                    s=s+"1"
                    c="0"
                else:
                    s=s+"0"
                    c="1"
            elif(a[i]=='1' and b[i]=='0'):
                if(c=='0'):
                    s=s+"1"
                    c="0"
                else:
                    s=s+"0"
                    c="1"
            elif(a[i]=='1' and b[i]=='1'):
                if(c=='0'):
                    s=s+"0"
                    c="1"
                else:
                    s=s+"1"
                    c="1"
        if(c=="1"):
            g=s+c
            f=g[::-1]
        else:
            g=s
            f=g[::-1]
        return(f)
            
            
                
                
                
                
                    
        
        