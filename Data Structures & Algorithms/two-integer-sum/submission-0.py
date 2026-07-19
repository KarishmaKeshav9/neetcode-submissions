class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_sum = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map_sum:
                return [map_sum[diff], i]
            else:
                map_sum[n] = i