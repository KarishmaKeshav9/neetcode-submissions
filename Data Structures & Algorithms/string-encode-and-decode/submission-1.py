class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        d_res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            word_len = int(s[i:j])
            d_res.append(s[j+1:j+1+word_len])
            i = j+1+word_len
        return d_res
