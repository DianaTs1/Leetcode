class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd =  [num for num in nums if num % 2 == 1 ]
        even = [num for num in nums if num % 2 == 0]
        
        return even + odd
       