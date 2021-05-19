class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        decompressed_list = []
        
        for i in range(0, len(nums), 2):
            sub_list = []
            for j in range(nums[i]):
                sub_list.append(nums[i+1])
            decompressed_list += sub_list
            
        return decompressed_list