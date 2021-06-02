class Solution:
    def replaceDigits(self, s: str) -> str:
        
        final_string = ""
        
        def shift(char, num):
            return chr(ord(char) + int(num))
                    
        for elem in range(len(s)):
            final_string += shift(s[elem-1], s[elem]) if elem % 2 else s[elem]

        return final_string
