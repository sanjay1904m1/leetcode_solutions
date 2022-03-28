def ma(mat,n):
    for i in range(n):
        for j in range(i):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    return mat
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
    
        for i in range(4):
            mat.reverse()
            for i in range(len(mat)):
                for j in range(i):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            print(mat)
            if(mat==target):
                return True
        return False
                    
        