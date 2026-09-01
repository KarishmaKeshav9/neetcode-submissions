class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                sub_str = ""
                while stack[-1] != "[":
                    sub_str = stack.pop() + sub_str
                stack.pop()

                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                stack.append(int(digit)*sub_str)
        return "".join(stack)