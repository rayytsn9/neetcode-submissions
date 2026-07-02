import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_new = re.sub(r'[^0-9a-zA-Z]', '', s)
        s_new = s_new.lower()

        t = s_new[::-1]

        if s_new == t:
            return True

        return False
        