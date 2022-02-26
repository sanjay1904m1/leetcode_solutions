class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        l=["a","c","e","g"]
        if(coordinates[0] in l):
            if(int(coordinates[1])%2==0):
                return True
            else:
                return False
        else:
            if(int(coordinates[1])%2==0):
                return False
            else:
                return True
        