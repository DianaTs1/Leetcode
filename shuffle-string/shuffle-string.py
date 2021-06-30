class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dict = {}
        
        for i in range(len(s)):
            key = indices[i]
            value = s[i]
            dict[key] = value
            
        
        sorted_dict = OrderedDict(sorted(dict.items()))
        

        final_string = ""
        for elem in sorted_dict.values():
            final_string += elem
        
        return final_string