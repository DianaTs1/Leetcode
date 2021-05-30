class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        result = 0

        for start in range(1, len(arr)+1, 2):
            for end in range(start, len(arr)+1):
                sublist = arr[end-start:end]
                sum_of_sublist = sum(sublist)
                result += sum_of_sublist

        return result