class Solution:
    def sortSentence(self, s: str) -> str:
        
        s = s.split(' ')
        temp_list = []
        answer = ""
        
        for part in s:
            temp_list.append((part[-1], part[:-1]))
            
        temp_list.sort(key=lambda x: x[0])
        
        for part1, part2 in temp_list:
            answer += ' '
            answer += part2
            
        return answer.strip()
