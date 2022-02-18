class Solution:
    def matrixReshape(self, mat: List[List[int]], m: int, n: int) -> List[List[int]]:
        original=[]
        for i in mat:
            for j in i:
                original.append(j)
        if(m*n!=len(original)):
            return mat
        a=0
        k=[]
        for i in range(m):
            l=[]
            for j in range(n):
                
                l.append(original[a])
                a+=1
            k.append(l)
        return k
        
                
        