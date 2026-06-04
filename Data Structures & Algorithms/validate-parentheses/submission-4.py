class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_dict = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        open_bracket = ['{', '[', '(']
        close_bracket = ['}', ']', ')']

        for c in s:
            if c in open_bracket:
                stack.append(c)
            elif c in bracket_dict:
                if len(stack) > 0 and stack.pop() == bracket_dict[c]:
                    continue
                else:
                    return False

        return len(stack) == 0
        
