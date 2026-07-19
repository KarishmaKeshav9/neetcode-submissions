class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            while l < r and not self.is_alpha_num(s[l]):
                l+=1
            while r > l and not self.is_alpha_num(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1
        return True

    def is_alpha_num(self, letter):
        return (ord('A') <= ord(letter) <= ord('Z') or ord('a') <= ord(letter) <= ord('z') or ord('0') <= ord(letter) <= ord('9'))        
    