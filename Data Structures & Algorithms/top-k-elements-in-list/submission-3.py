class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_map = [[] for i in range(len(nums) + 1)]
        count = {}
        res = []

        for n in nums:
            count[n] = 1+ count.get(n, 0)
        
        for n, val in count.items():
            res_map[val].append(n)
        
        for i in range(len(res_map) -1, 0, -1):
            for n in res_map[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
