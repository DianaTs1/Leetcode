class Solution:
    def sortSentence(self, s: str) -> str:
        
        temp_list = s.split(" ")
        temp_dict = {}
        list_of_nones = []

        for elem in temp_list:
            list_of_nones.append(None)

        for elem in temp_list:
            index = int(elem[int(len(elem) - 1)]) - 1
            temp_dict[index] = index, elem[:int(len(elem) - 1)]

        sorted_list = sorted(temp_dict.values())

        final_string = sorted_list[0][1]

        for elem in range(1, len(sorted_list)):
            final_string += " " + sorted_list[elem][1]


        return final_string
        
        
