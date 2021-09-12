class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        n = len(nums)
        quadruplets_count = 0
        
        for c in range(2,n): 
            b = c-1
            for a in range(c-1):
                dic[nums[a] + nums[b]] += 1
            for d in range(c+1,n):
                quadruplets_count += dic[nums[d] - nums[c]]
        return quadruplets_count
