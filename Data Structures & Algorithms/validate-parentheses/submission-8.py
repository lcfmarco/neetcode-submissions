class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []

        valid_brackets = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        for i in s:
            if i in valid_brackets:
                if len(bracket_stack) == 0:
                    return False
                elif bracket_stack.pop() != valid_brackets[i]:
                    return False
            else:
                bracket_stack.append(i)
        
        return len(bracket_stack) == 0