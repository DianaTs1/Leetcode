class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        num = 0
        lst = []

        for i in range(len(nums)):
            num += nums[i]
            lst.append(num)

        return lst