class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        first_array_of_words = s.split(" ")
        final_array_of_words = first_array_of_words[:k]
        
        return " ".join(final_array_of_words)