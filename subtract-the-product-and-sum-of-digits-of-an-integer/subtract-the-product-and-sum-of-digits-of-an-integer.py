class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = str(n)
        sum_of_digits = 0
        product_of_digits = 1
        
        for elem in nums:
            sum_of_digits += int(elem)
            product_of_digits *= int(elem)
        
        return product_of_digits - sum_of_digits