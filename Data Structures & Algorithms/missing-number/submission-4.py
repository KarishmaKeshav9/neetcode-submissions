class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res

        map_nums = set(nums)

        for n in range(len(nums)+1):
            if n not in map_nums:
                return n