class Solution:
    def isValid(self, s: str) -> bool:
        CloseToOpen = {")":"(", "]":"[", "}":"{"}
        stack = []
        for i in range(len(s)):
            if stack and s[i] in CloseToOpen:
                if stack[-1] != CloseToOpen[s[i]]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        
        if stack:
            return False
        else:
            return True