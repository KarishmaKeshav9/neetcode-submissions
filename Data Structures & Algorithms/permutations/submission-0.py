class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrace():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for n in nums:
                if n in path:
                    continue
                
                path.append(n)
                backtrace()
                path.pop()
        
        backtrace()
        return res