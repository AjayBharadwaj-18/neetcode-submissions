class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        w = set()
        n = len(nums)
        l = 0

        for r in range(n):
            if abs(r - l) > k:
                w.remove(nums[l])
                l += 1

            if nums[r] in w:
                return True

            w.add(nums[r])
        return False
        