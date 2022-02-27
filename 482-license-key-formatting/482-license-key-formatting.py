class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s1=s[::-1]
        c=0
        s2=""
        s3=""
        
        for i in s1:
            if(i!="-" and c!=k):
                if(i.isalpha()):
                    if(i.islower()):
                        s2=s2+chr(ord(i)-32)
                    else:
                        s2=s2+i
                else:
                    s2=s2+i
                c+=1
            elif(c==k and i!="-"):
                c=1
                s2=s2+"-"
                s3=s3+s2
                s2=i.upper()
        s3=s3+s2
        return s3[::-1]
                
        