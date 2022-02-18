class Solution:
    def calPoints(self, ops: List[str]) -> int:
        k=-1
        l=[]
        for i in ops:
            if(i=="+"):
                l.append(l[k]+l[k-1])
                k+=1
            elif(i=="C"):
                l.pop(k)
                k-=1
            elif(i=="D"):
                l.append(l[k]*2)
                k+=1
            else:
                l.append(int(i))
                k+=1
        return sum(l)
                
        