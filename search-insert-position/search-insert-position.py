class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, x in enumerate(nums):
            if target <= x:
                return i
        return len(nums)