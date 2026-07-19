class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s)==Counter(t)

        #return sorted(s) == sorted(t)

        counterS, counterT = {}, {}
        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            counterS[s[i]] = 1 + counterS.get(s[i],0)
            counterT[t[i]] = 1 + counterT.get(t[i],0)

        return counterS == counterT

        