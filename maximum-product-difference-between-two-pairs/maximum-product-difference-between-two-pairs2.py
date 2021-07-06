class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        temp_nums = nums.copy()
        temp_nums.sort(reverse=True)

        result = (temp_nums[0] * temp_nums[1]) - (temp_nums[len(temp_nums)-1] * temp_nums[len(temp_nums)-2])
        return result
