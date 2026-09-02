class Solution:
    def climbStairs(self, n: int) -> int:
        onestep, twostep = 1,1
        for i in range(n-1):
            temp = onestep
            onestep = onestep + twostep
            twostep = temp
        return onestep
        