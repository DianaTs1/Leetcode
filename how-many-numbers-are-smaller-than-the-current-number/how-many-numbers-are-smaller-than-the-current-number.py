class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        final_list = []
        for i in range(len(nums)):
            quantity_of_smaller_numbers = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    quantity_of_smaller_numbers +=1
            final_list.append(quantity_of_smaller_numbers)
        return final_list
                    