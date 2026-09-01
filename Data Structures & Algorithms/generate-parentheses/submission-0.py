class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrace(openb, closeb):
            if openb == closeb == n:
                res.append("".join(stack))
                return
            
            if openb < n:
                stack.append("(")
                backtrace(openb+1, closeb)
                stack.pop()

            if closeb < openb:
                stack.append(")")
                backtrace(openb, closeb+1)   
                stack.pop()

        backtrace(0,0)
        return res  