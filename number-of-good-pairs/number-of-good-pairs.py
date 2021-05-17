class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        
        for i in range(len(nums)):
            start_point = i+1
            for j in range(start_point, len(nums)):
                if nums[i] == nums[j]:
                    good_pairs +=1
        return good_pairs