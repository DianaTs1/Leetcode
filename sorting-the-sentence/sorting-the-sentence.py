class Solution:
    def sortSentence(self, s: str) -> str:
        
        temp_list = s.split(" ")
        temp_dict = {}

        for elem in temp_list:
            index = elem[-1]
            temp_dict[index] = index, elem[:-1]

        sorted_list = sorted(temp_dict.values())

        final_string = ""

        for index, word in sorted_list:
            final_string += " " + word

        return final_string.strip()
        
        
