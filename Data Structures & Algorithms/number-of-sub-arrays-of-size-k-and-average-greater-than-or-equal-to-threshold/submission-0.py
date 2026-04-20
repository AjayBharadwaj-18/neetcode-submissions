class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        l = 0
        n = len(arr)
        current_sum = 0
        target_sum = k * threshold
        for r in range(n):
            current_sum += arr[r]
            if r - l + 1 > k:
                current_sum -= arr[l]
                l += 1
            
            if r - l + 1 == k:
                if current_sum >= target_sum:
                    total += 1
        return total