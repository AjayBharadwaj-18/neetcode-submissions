class Solution:
    def scoreOfString(self, s: str) -> int:
        l = 0
        r = 1
        sum = 0

        for i in range(len(s)):

            if l<r and r<len(s) :
                sum += abs(ord(s[l]) - ord(s[r]))
            l += 1
            r += 1
        return sum


        