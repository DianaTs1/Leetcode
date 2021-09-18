class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        position = word.index(ch) + 1 
                
        temp_word = word[0: position]
        
        res = temp_word[: : -1] + word[position::]
        
        return res
			