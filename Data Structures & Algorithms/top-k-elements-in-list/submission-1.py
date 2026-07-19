class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_map = [[] for i in range(len(nums) + 1)]
        counter = {}
        res = []
        
        for n in nums:
            counter[n] = 1 + counter.get(n,0)
        
        for num, count in counter.items():
            res_map[count].append(num)
        
        for i in range(len(res_map) -1, 0, -1):
            for n in res_map[i]:
                res.append(n)
                if len(res)==k:
                    return res
