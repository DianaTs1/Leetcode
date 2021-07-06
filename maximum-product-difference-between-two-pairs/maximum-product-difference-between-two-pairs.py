class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        temp_nums = nums.copy()
        max_number_1 = max(temp_nums)
        temp_nums.remove(max_number_1)
        max_number_2 = max(temp_nums)
        temp_nums.remove(max_number_2)
        min_number_1 = min(temp_nums)
        temp_nums.remove(min_number_1)
        min_number_2 = min(temp_nums)
        temp_nums.remove(min_number_2)

        return (max_number_1 * max_number_2) - (min_number_1 * min_number_2)