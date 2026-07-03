class Solution:
    import re

    def isPalindrome(self, s: str) -> bool:
        # 2 pointers approach

        s_new = re.sub(r'[^a-zA-Z0-9]', '', s)

        l, r = 0, len(s_new) - 1

        while l < r:
            if s_new[l].lower() != s_new[r].lower():
                return False

            l, r = l + 1, r - 1

        return True

