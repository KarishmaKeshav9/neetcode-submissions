class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        in_set = set()
        for n in nums:
            if n in in_set:
                return True
            else:
                in_set.add(n)
        return False