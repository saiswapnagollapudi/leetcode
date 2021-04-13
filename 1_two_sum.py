class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dct:
                return([dct[complement],i])
            else:
                dct[nums[i]] = i
