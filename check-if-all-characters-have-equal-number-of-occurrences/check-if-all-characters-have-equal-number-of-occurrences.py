class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        dic = {}

        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
                
        number_of_occurances = dic.get(s[0])
        
        for key, val in dic.items():
            if val != number_of_occurances:
                return False

        return True