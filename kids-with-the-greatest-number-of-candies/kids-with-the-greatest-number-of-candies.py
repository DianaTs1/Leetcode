class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest_number_of_candies = max(candies)
        
        output = []
        
        for i in range(len(candies)):
            output.append(candies[i] + extraCandies >= greatest_number_of_candies)
        return output