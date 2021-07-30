class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numsDict = {}
        for elem in nums: 
            numsDict[elem] = nums.count(elem)
        for key, values in numsDict.items():
            if(numsDict[key] == 1):
                return key
