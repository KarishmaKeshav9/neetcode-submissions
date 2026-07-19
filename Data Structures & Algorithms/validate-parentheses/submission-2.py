class Solution:
    def isValid(self, s: str) -> bool:
        CloseToOpen = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in CloseToOpen:
                if not stack or stack[-1]!= CloseToOpen[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        return False if stack else True

        