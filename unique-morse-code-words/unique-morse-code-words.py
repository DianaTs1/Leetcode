import string

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        english_alphabet = list(string.ascii_lowercase)
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        ## Create a dictionary with the keys of english letters and value of morse codes
        alphabet_dictionary = {}
        
        for letter in range(len(english_alphabet)):
            alphabet_dictionary[english_alphabet[letter]] = morse_code[letter]
        
        ## Create a list that only contains unique transformations  of words
        temp_list = []
        for word in words:
            temp_morse_code = ""
            for letter in word:
                temp_morse_code += alphabet_dictionary[letter]
            if temp_morse_code not in temp_list: 
                temp_list.append(temp_morse_code)
                        
        return len(temp_list)
