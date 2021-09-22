class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: 
            return []
        result = []
        temp_str = ''
        
        for i in range(len(nums)-1):
            if not temp_str and nums[i+1]-nums[i] > 1:    # if 
                result.append(str(nums[i]))
                temp_str = ''
            elif not temp_str:
                temp_str += str(nums[i]) + '->'
            elif temp_str and nums[i+1]-nums[i] == 1:
                continue
            elif temp_str:
                temp_str += str(nums[i])
                result.append(temp_str)
                temp_str = ''
                
        if not temp_str: result.append(str(nums[-1]))
        elif temp_str: 
            temp_str += str(nums[-1])
            result.append(temp_str)
            
        return result