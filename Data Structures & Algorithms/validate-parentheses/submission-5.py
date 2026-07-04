class Solution:
    def isValid(self, s: str) -> bool:

        # check valid length
        if len(s) % 2 != 0:
            return False

        # opening
        o = ['(', '[', '{']

        # closing
        c = [')', ']', '}']

        # valid pair
        oc = ['()', '[]', '{}']

        # init stack
        stack = deque()

        for val in s:

            if val in o:
                stack.append(val)
            elif val in c:
                if not stack:
                    return False
                
                if stack[-1] + val in oc:
                    stack.pop()
                else:
                    return False
                               
        if not stack:
            return True
        else:
            return False

