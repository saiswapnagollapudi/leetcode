 class Solution(object):
     def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_n = nums[0]
        sum_n = 0
        for i in nums:
            sum_n += i
            max_n = max(sum_n, max_n)
            sum_n = max(sum_n,0)
        return(max_n)
