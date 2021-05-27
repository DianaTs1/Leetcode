class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        for elem in alphabet:
            if elem not in sentence:
                return False
        return True