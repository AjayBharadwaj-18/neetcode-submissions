class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "".join(char.lower() for char in s if char.isalnum())
        n = len(a)
        l = 0
        r = n-1
        while l<r:
            if a[l] != a[r]:
                return False
            l += 1
            r -= 1
        return True
        
        