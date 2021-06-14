class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels= ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        ## split the word
        half = len(s)//2
        part_a = s[:half]
        part_b = s[half:]
        
        ##  count vowels in each part
        count_a = 0
        count_b = 0
        
        for elem in range(len(part_a)):
            if part_a[elem] in vowels:
                count_a += 1
            if part_b[elem] in vowels:
                count_b += 1
        
        return count_a == count_b
            
