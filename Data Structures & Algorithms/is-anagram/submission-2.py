class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s)==Counter(t)

        counterS, counterT = {}, {}
        if len(s)!=len(t):
            return False

        for i in range(0,len(s)):
            counterS[s[i]] = 1 + counterS.get(s[i],0)
            counterT[t[i]] = 1 + counterT.get(t[i],0)

        for char, count in counterS.items():
            if count != counterT.get(char,0):
                return False
        return True

        