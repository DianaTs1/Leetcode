class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 0
        for ele in nums:
            if count == 0:
                res = ele
                count = 1
            elif res == ele:
                count += 1
            else:
                count -= 1
        return res