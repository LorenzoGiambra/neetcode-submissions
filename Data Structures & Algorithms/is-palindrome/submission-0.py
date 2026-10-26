class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = "".join(char for char in s if char.isalnum())
        ns = ns.lower()
        n = len(ns)
        hn = len(ns)//2
        for i in range(hn):
            if ns[i] != ns[n-1-i]:
                return False
        return True