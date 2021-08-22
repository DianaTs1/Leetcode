class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = -sys.maxsize
        maxsum = -sys.maxsize
        for i in range(len(nums)):
            currentSum = max(nums[i],nums[i]+currentSum)
            maxsum = max(maxsum,currentSum)
        return maxsum