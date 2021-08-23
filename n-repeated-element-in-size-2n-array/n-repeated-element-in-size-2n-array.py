class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        
        for elem in nums:
            if nums.count(elem) == n:
                return elem 
