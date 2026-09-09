class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        def dfs(s1p, s2p, s3p):
            if s3p == len(s3):
                return (s1p == len(s1)) and (s2p == len(s2))

            if (s1p, s2p) in dp:
                return dp[(s1p, s2p)]

            result = False

            if s1p < len(s1) and s1[s1p] == s3[s3p]:
                result = dfs(s1p + 1, s2p, s3p + 1)

            if not result and s2p < len(s2) and s2[s2p] == s3[s3p]:
                result = dfs(s1p, s2p + 1, s3p + 1)

            dp[(s1p, s2p)] = result
            return result

        return dfs(0, 0, 0)