class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list1 = nums[:n]
        list2 = nums[n:]
        final_list = []
        
        for i in range(len(list1)):
            final_list.append(list1[i])
            final_list.append(list2[i])
            
        return final_list