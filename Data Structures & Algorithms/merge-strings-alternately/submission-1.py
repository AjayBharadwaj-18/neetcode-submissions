class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        n = len(word1)
        s = len(word2)
        res = ""
        if n<s:
            a = n
        else:
            a = s
        for i in range(a):
            b = word1[l] + word2[r]
            l += 1
            r += 1
            res += b
        c = max(n,s)
        for j in range(a, c):
            if n>s:
                res += word1[j]
            else:
                res += word2[j]
        return res        