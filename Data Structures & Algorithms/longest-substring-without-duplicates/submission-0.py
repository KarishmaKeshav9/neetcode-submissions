class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        sub_str = set()

        for r in range(len(s)):
            while s[r] in sub_str:
                sub_str.remove(s[l])
                l+=1
            sub_str.add(s[r])
            res = max(res, r-l+1)
        return res
        