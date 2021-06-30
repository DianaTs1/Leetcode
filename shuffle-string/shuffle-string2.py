class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        temp_list = list(s)
        
        for i in range(len(s)):
            index = indices[i]
            elem = s[i]
            temp_list[index] = elem
        
        return "".join(temp_list)
