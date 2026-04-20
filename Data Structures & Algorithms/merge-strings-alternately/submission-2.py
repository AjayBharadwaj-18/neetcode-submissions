class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        n, s = len(word1), len(word2)
        a, b = min(n,s), max(n,s)
        res = ""
        for i in range(a):
            tmp = word1[l] + word2[r]
            l += 1
            r += 1
            res += tmp
        for j in range(a, b):
            if n>s:
                res += word1[j]
            else:
                res += word2[j]
        return res        