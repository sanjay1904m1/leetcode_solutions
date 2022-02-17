class Solution:
    def reverseVowels(self, s: str) -> str:
        l=['a', 'e', 'i', 'o','u','A', 'E', 'I', 'O','U']
        v=[]
        
        for i in s:
            if(i in l):
                v.append(i)
                s=s.replace(i,"*")
        f=v[::-1]
        
        for i in range(len(f)):
            s=s.replace("*",f[i],1)
        t=s
        return t
                
        