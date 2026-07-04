class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {')': '(', ']': '[', '}': '{'}

        stack = deque()

        for key in s:
            
            if key in pairs:
                if stack and stack[-1] == pairs[key]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(key)

        if not stack:
            return True
        else:
            return False

                
