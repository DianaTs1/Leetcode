class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_value_1 = nums.pop(nums.index(max(nums)))
        max_value_2 = nums.pop(nums.index(max(nums)))
        
        return (max_value_1-1)*(max_value_2-1)
