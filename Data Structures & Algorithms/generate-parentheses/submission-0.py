class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Stack to keep track of our current parenthesis
        stack = []
        # Result list that has all our valid parenthesis
        res = []

        # Recursive function that will be used to generate our string
        def backtrack(openN, closedN):
            if openN == closedN == n:
                # Joins everything in the stack into a string
                res.append("".join(stack))
                return
            
            # 
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()
            if openN > closedN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res

