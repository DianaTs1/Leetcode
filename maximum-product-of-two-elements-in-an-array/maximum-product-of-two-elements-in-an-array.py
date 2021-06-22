class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        first_max_value = max(nums)
        
        if nums.count(list) > 1:
            return (first_max_value-1) * 2
        else: 
            nums.remove(first_max_value)
            second_max_value = max(nums)
            return (first_max_value-1) * (second_max_value -1)
        
        
        
        