from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = Counter(nums)
        for key, values in nums.items():
            if(nums[key] == 1):
                return key