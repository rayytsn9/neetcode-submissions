class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {')': '(', ']': '[', '}': '{'}

        stack = []

        for key in s:
            
            if key in pairs:
                if stack and stack[-1] == pairs[key]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(key)

        return True if not stack else False

                
