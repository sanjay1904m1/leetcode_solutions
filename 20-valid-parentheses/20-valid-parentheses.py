class Solution:
    def isValid(self, s: str) -> bool:
        t=s
        for i in range(int(len(s)/2)):
            if("()" in t):
                t=t.replace("()","")
            elif("{}" in t):
                t=t.replace("{}","")
            elif("[]" in t):
                t=t.replace("[]","")
        if(t==""):
            return True
        else:
            return False
            
        