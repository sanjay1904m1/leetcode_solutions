class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        else:
            j = 0
            i = 1
            while i < len(nums):
                if nums[j] == nums[i]:
                    i += 1
                else:
                    j += 1
                    nums[j] = nums[i]
                    i += 1
            return j+1
        