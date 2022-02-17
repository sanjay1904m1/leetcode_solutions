# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n+1

        while start <= end:
            mid = (start+end) // 2

         

            if isBadVersion(mid) == False:
                start = mid + 1

            else:
                end = mid - 1

        

        if isBadVersion(mid) == True:
            return mid
        else:
            return mid + 1
        