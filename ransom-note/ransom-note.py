class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
            d = {}
            for letter in magazine:
                if letter not in d:
                    d[letter] = 1
                else:
                    d[letter] +=1

            for char in ransomNote:
                if char not in d:
                    return False
                if char in d:
                    if d[char] > 1:
                        d[char] -=1
                    else:
                        del d[char]
            return True