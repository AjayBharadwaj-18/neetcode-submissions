class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l = 0
        n = len(nums)
        for r in range(1, n):
            if nums[l] == nums[r]:
                return True
            else:
                l += 1
        return False
        

        