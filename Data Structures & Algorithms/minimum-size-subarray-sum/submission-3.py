class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        length = (n + 1)
        total = 0

        for r in range(n):
            total += nums[r]
            while total >= target:
                length = min( r - l + 1, length)
                total -= nums[l]
                l += 1
        return 0 if length == (n+1) else length
        